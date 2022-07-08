
from flask_restful import Api

from fiole.model.web.Controller import Controller
from fiole.resources.Logger import Logger
from fiole.model.framework.Container import Container
from fiole.web.HealthController import HealthController


class Router:

    def __init__(self, api: Api) -> None:
        self.api = api
        self.logger :Logger = Container.retrieve(Logger)
        self.routes = []

    def routeRegistration(self): 
        self.staticRouteRegistration()
        self.dynamicRouteRegistration()

    def staticRouteRegistration(self): 
        self.logger.trace("Static routes registration")
        self.registerRoute(HealthController, "/actuator/health")

    def dynamicRouteRegistration(self):

        controllers = Container.instanceOf(Controller)

        controller :Controller
        for controller in controllers:
            self.registerRoute(controller,controller._PATH)

    def registerRoute(self, cls ,path :str) -> None:
        if any(r["path"] == path for r in self.routes):
            for r in self.routes:
                if r["path"] == path:
                    existingController = r["controller"]

            self.logger.trace("Cannot register {path} with controller {newController}, path it's already in use by {existingOne}".format(
                path=path,
                newController=cls.__module__,
                existingOne=existingController
            ))

            pass
        self.api.add_resource(cls, path)
        self.routes.append({"controller":cls.__module__,"path":path})
        self.logger.trace("Endpoint {path} created and bind with {controller}".format(controller=cls.__module__,path=path) )
