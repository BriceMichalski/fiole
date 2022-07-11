
from typing import Callable, List

from fiole.model.web.RequestMethod import RequestMethod
from fiole.model.web.Route import Route


def RequestMapping(path,methods :List[RequestMethod] =[RequestMethod.GET]):
    def addRouteAttribute(func :Callable):
        func_route = Route(path,func,methods)
        func._route = func_route
        return func
    return addRouteAttribute

def GetMapping(path):
    def addRouteAttribute(func :Callable):
        func_route = Route(path,func,[RequestMethod.GET])
        func._route = func_route
        return func
    return addRouteAttribute

def PostMapping(path):
    def addRouteAttribute(func :Callable):
        func_route = Route(path,func,[RequestMethod.POST])
        func._route = func_route
        return func
    return addRouteAttribute

def PutMapping(path):
    def addRouteAttribute(func :Callable):
        func_route = Route(path,func,[RequestMethod.PUT])
        func._route = func_route
        return func
    return addRouteAttribute

def DeleteMapping(path):
    def addRouteAttribute(func :Callable):
        func_route = Route(path,func,[RequestMethod.DELETE])
        func._route = func_route
        return func
    return addRouteAttribute
