from typing import List
from fiole.model.metaclass.Singleton import Singleton 
from fiole.model.framework.ContainerItem import ContainerItem
from fiole.resources.Logger import Logger

class Container(metaclass=Singleton):

    def __init__(self) -> None:
        self._registry = []
        self.logger = Logger()
    
    def findOne(self, qualifier):
        item: ContainerItem
        for item in self._registry:
            if item.getQualifier() == qualifier:
                return item.getObj()
        return None

    def newItem(self, object,cls =None, qualifier :str =None) -> None:
        newItem = ContainerItem(object, cls, qualifier)
        existOne = self.findOne(newItem.getQualifier())
        if existOne is None:
            self._registry.append(newItem)
            self.logger.trace("New ContainerItem with id {id}".format(id=newItem.getQualifier()))
        else:
            errorMessage = "ContainerItem with same qualifier already exist. [{}]".format(newItem.getQualifier())
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
    def register(object, cls =None, qualifier :str =None):
        return Container.instance().newItem(object, cls, qualifier)

    @staticmethod
    def retrieve(qualifier):
        return Container.instance().findOne(qualifier)

    @staticmethod
    def instanceOf(cls) -> List:
        return Container.instance().find(cls)
