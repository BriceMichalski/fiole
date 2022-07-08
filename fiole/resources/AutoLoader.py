from os import name
import sys
import logging
import importlib

from flask import Flask
from pathlib import Path
from flask_restful import Api
from threading import Thread

from fiole.model.Configuration import Component
from fiole.model.threading.DaemonProcess import DaemonProcess
from fiole.model.web.Controller import Controller
from fiole.model.Configuration import Configuration
from fiole.model.threading.Process import Process

from fiole.resources.Logger import Logger
from fiole.resources.Router import Router
from fiole.model.framework.Container import Container
from fiole.resources.HealthChecker import HealthChecker
from fiole.utils.ModuleUtils import ModuleUtils


class AutoLoader():

    def __init__(self) -> None:
        self.logger = Logger()

    def load(self,app :Flask):
        
        self.logger.trace("Component container creation")
        Container.instance()
        Container.register(app)

        self.logger.trace("Loading fiole static component")
        self.loadStaticComponent()

        self.logger.trace("Loading dynamic component")
        self.dynamicLoading()
        
        self.logger.trace("Call router routes registration function")
        self.loadRoutes()
    
    """ Static loader"""
    def loadStaticComponent(self):
        self.loadLogger()
        self.loadHealthChecker()
        self.loadApi()
        self.loadRouter()

    def loadApi(self):
        api = Api(Container.retrieve(Flask))
        Container.register(api)
    
    def loadRouter(self):
        router = Router(Container.retrieve(Api))
        Container.register(router)

    def loadRoutes(self):
        router :Router = Container.retrieve(Router)
        router.routeRegistration()

    def loadHealthChecker(self):
        healthChecker = HealthChecker()
        Container.register(healthChecker)
    
    def loadLogger(self):
        cli = sys.modules['flask.cli']
        cli.show_server_banner = lambda *x: None
        logging.getLogger('werkzeug').disabled = True
        Container.register(self.logger)


    """ Dynamic loader"""
    def dynamicLoading(self):

        applicationAbsPath = ModuleUtils.getApplicationFolder()
        projectPythonFile = Path(applicationAbsPath).rglob('*.py')

        for file in projectPythonFile:
            if str(file) == ModuleUtils.getMainModuleAbsPath():
                self.logger.trace("Ignoring main module registration")
                continue

            moduleImportString, moduleName = ModuleUtils.getImportStringFromPath(file)

            module = importlib.import_module(moduleImportString)
            moduleClass = getattr(module, moduleName)

            if issubclass(moduleClass,Controller): 
                Container.register(moduleClass,cls=Controller,qualifier=moduleClass)
                continue
            
            if issubclass(moduleClass,Configuration):
                Container.register(moduleClass(),cls=Configuration,qualifier=moduleClass)
                continue

            if issubclass(moduleClass,Process):
                process :Process = moduleClass()
                threadName = "{}Thread".format(moduleClass.__name__)
                process.setName(threadName)

                if issubclass(moduleClass,DaemonProcess):
                    
                    processThread = Thread(target=process.start,name=process.threadName,daemon=True)
                    Container.register(process,cls=DaemonProcess,qualifier=moduleClass)
                else: 
                    processThread = Thread(target=process.start,name=process.threadName,daemon=False)
                    Container.register(process,cls=Process,qualifier=moduleClass)
                
                Container.register(processThread,cls=Thread,qualifier=processThread)
                processThread.start()
                self.logger.trace("Starting process named {name} in a new {optionnal} Thread".format(
                    name=moduleClass.__name__,
                    optionnal= "daemonic" if issubclass(moduleClass,DaemonProcess) else ''
                ))
                
                continue

            if issubclass(moduleClass,Component):
                Container.register(moduleClass(),cls=Component,qualifier=moduleClass)
                continue