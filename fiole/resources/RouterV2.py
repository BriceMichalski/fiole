from fiole.model.framework.Container import Container
from fiole.model.framework.Controller import Controller
from fiole.resources.Logger import Logger
from fiole.utils.ListUtils import ListUtils
from fiole.web.ActuatorController import ActuatorController
from flask import Blueprint, Flask


class RouterV2:
    
    def __init__(self) -> None:
        self.app :Flask = Container.retrieve(Flask)
        self.logger :Logger = Container.retrieve(Logger)


    def routeRegistration(self): 
        self.staticRouteRegistration()
        self.dynamicRouteRegistration()


    def staticRouteRegistration(self): 
        self.logger.trace("Static routes registration")
        self.handleController(ActuatorController)


    def dynamicRouteRegistration(self):
        self.logger.trace("Dynamic routes registration")
        controllers = Container.instanceOf(Controller)

        controller :Controller
        for controller in controllers:
            self.handleController(controller)


    def handleController(self,controllerClass):
        if issubclass(controllerClass,Controller): 
            existingBp = self.getBpByPrefix(controllerClass.BLUEPRINT_PREFIX)

            if existingBp == None:
                ctrlBp = Blueprint(controllerClass.__name__,controllerClass.__name__,url_prefix=controllerClass.BLUEPRINT_PREFIX)
                ctrlBp.add_url_rule("/<path:path>",view_func=controllerClass.as_view("path"))
                    
                self.app.register_blueprint(ctrlBp,url_prefix=controllerClass.BLUEPRINT_PREFIX)

            else: 
                self.logger.error("A blueprint for prefix {} already in use by {}".format(
                    controllerClass.BLUEPRINT_PREFIX,
                    existingBp.import_name
                ))
        else:
            self.logger.error("Can't register route, argument is not an instance of `fiole.model.framework.Controller`")


    def getBpByPrefix(self,prefix) -> Blueprint:
        return ListUtils.uniqByAttr(self.app.iter_blueprints(),"url_prefix",prefix)
