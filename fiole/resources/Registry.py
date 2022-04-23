from ast import Raise
from html2text import List
from fiole.model.metaclass.Singleton import Singleton 
from fiole.model.RegistryItem import RegistryItem

class Registry(metaclass=Singleton):

    def __init__(self) -> None:
        self._registry = [RegistryItem]

    def findOne(self, identifier :str):
        for item in self._registry:
            if item.getIdentifier() == identifier:
                return item.getObj()
        return None

    def register(self, object, identifier) -> None:
        newItem = RegistryItem(object,identifier)
        existOne = self.findOne(newItem.getIdentifier())
        if existOne is None:
            self._registry.append(newItem)
        else:
            Raise("RegistryItem with same identifier already exist. [{}]".format(newItem.getIdentifier()))

    def find(self, cls) -> List:
        result = []
        for item in self._registry:
            if item.getClass() == cls:
                result.append(item)
        
        if len(result) > 0:
            return result
        else:
            return None 
