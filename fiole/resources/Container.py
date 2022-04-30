from typing import List
from fiole.model.metaclass.Singleton import Singleton 
from fiole.model.ContainerItem import ContainerItem
from fiole.resources.Logger import Logger

class Container(metaclass=Singleton):

    def __init__(self) -> None:
        self._registry = []
        self.logger = Logger()
    
    def findOne(self, identifier):
        item: ContainerItem
        for item in self._registry:
            if item.getIdentifier() == identifier:
                return item.getObj()
        return None

    def newItem(self, object,cls =None, identifier :str =None) -> None:
        newItem = ContainerItem(object, cls, identifier)
        existOne = self.findOne(newItem.getIdentifier())
        if existOne is None:
            self._registry.append(newItem)
            self.logger.trace("New ContainerItem with id {id}".format(id=newItem.getIdentifier()))
        else:
            errorMessage = "ContainerItem with same identifier already exist. [{}]".format(newItem.getIdentifier())
            self.logger.error(errorMessage)
            raise(errorMessage)

    def find(self, cls):
        result = []

        item: ContainerItem
        for item in self._registry:
            if item.getClass() == cls:
                result.append(item.getObj())
        
        return result

    @staticmethod
    def instance():
        return Container()

    @staticmethod
    def register(object, cls =None, identifier :str =None):
        return Container.instance().newItem(object, cls, identifier)

    @staticmethod
    def retrieve(identifier):
        return Container.instance().findOne(identifier)

    @staticmethod
    def instanceOf(cls) -> List:
        return Container.instance().find(cls)
