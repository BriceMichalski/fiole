
from typing import Callable, List

from fiole.model.framework.Component import Component
from fiole.model.web.HttpStatus import HttpStatus
from fiole.model.web.MimeType import MimeType
from fiole.model.web.RequestMethod import RequestMethod
from fiole.model.web.Response import Response
from fiole.model.web.Route import Route
from flask import request
from flask.views import View


class Controller(View,Component):
    
    BLUEPRINT_PREFIX :str = "/"
    ACCEPT :str = MimeType.ALL
    CONTENT_TYPE :str = MimeType.ALL

    methods = ["GET","POST","PUT","DELETE","HEAD","OPTIONS"]

    def __init__(self) -> None:
        super().__init__()

    def dispatch_request(self,*args,**kwargs):
        
        relative_path = "/" + kwargs.get('path')
        method = request.method

        response = self.prefilledResponse()
        handler :Callable = None        

        for route in self.routes:     
            if route.pathMatch(relative_path):
                if route.methodMatch(method):
                    handler = route.handler
                elif method == RequestMethod.OPTIONS:
                    return (
                        Response.header("Accept",self.ACCEPT)
                                .header("Allow",", ".join(route.methods))
                                .status(HttpStatus.OK)
                                .send()
                    )
                else:
                    return response.status(HttpStatus.METHOD_NOT_ALLOWED).send()
        
        if handler == None:
            return response.status(HttpStatus.NOT_FOUND).send()        
        
        kwargs.pop("path")
        resp = handler(self,*args, **kwargs)
        return resp


    def prefilledResponse(self):
        return  (   
            Response.header('Content-Type',self.CONTENT_TYPE)
                    .header('Accept',self.ACCEPT)
        )


    @property
    def routes(self) -> List[Route]:
        routeList = []
        methodList = self.getSelfRouteMethods()      
        for method in methodList:
            routeList.append(method._route)
        return routeList

    

    def getSelfRouteMethods(self):

        controllerMethod = dir(Controller)
        selfMethod = dir(self)
        selfSpesificMethod = list(set(selfMethod) - set(controllerMethod))

        methodList = []
        for methodName in selfSpesificMethod:
            method = getattr(self, methodName)
            if callable(method) and hasattr(method, '_route'):
                methodList.append(method)

        return methodList
