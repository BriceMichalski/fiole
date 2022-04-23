import os
import importlib
import inspect
from pathlib import Path
from flask_restful import Api

from fiole.model.Controller import Controller
from fiole.web.HealthController import HealthController
from fiole.resources.Logger import Logger


ROUTE_FILE = ''

class Router:

    def __init__(self, api: Api) -> None:
        self.api = api
        self.routes = []
        self.logger = Logger()

    def routeRegistration(self): 
        self.staticRouteRegistration()
        self.dynamicRouteRegistration()

    def staticRouteRegistration(self): 
        self.registerRoute(HealthController, "/actuator/health")


    def dynamicRouteRegistration(self):
        """
            Find all file that match *Controller.py in parent module and load it with property
        """
        frame = inspect.stack()[-1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        appAbsPath = os.path.abspath(os.path.dirname(filename))
        mainPackage = appAbsPath.split("/")[-1]
        
        self.logger.debug("Recursive looking for file that match *Controller.py in {} module".format(mainPackage))
        
        for modulePath in Path(appAbsPath).rglob('*Controller.py'):
            monduleFile = str(modulePath).split("/")[-1]
            moduleName = monduleFile.replace(".py","")
            packageRelativePath = str(modulePath).replace(appAbsPath + "/","").replace("/" + monduleFile,"").replace("/",".")

            moduleString = "{package}.{packageRelativePath}.{moduleName}".format(
                package= mainPackage,
                packageRelativePath= packageRelativePath,
                moduleName= moduleName
            )

            module = importlib.import_module(moduleString)
            controller = getattr(module, moduleName)
            if issubclass(controller,Controller):
                self.registerRoute(controller,controller._PATH)
            else:
                self.logger.debug("{} is not a subclass of fiole.model.Controller, skip it.".format(moduleString))

    def registerRoute(self, cls ,path :str) -> None:
        if any(r["path"] == path for r in self.routes):
            for r in self.routes:
                if r["path"] == path:
                    existingController = r["controller"]

            self.logger.debug("Cannot register {path} with controller {newController}, path it's already in use by {existingOne}".format(
                path=path,
                newController=cls.__module__,
                existingOne=existingController
            ))

            pass

        self.api.add_resource(cls, path)
        self.routes.append({"controller":cls.__module__,"path":path})
        self.logger.debug("Endpoint {path} created and bind with {controller}".format(controller=cls.__module__,path=path) )
