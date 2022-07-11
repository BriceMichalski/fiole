
from dataclasses import dataclass
from os import path
from typing import Callable, List


@dataclass
class Route:
    path    :str
    handler :Callable
    methods :List
    
    def __init__(self,path,handler,methods) -> None:
        self.path = path
        self.handler = handler
        self.methods = methods


    def pathMatch(self,path :str) -> bool:
        result =  True if path == self.path else False
        return result

    def methodMatch(self,method) -> bool:
        result = True if method in self.methods else False
        return result

    def isMatchingRequest(self,path :str, method :str) -> bool:
        return self.pathMatch(path) & self.methodMatch(method)

