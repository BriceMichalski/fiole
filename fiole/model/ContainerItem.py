from datetime import datetime

class ContainerItem():

    def __init__(self, obj, cls =None, identifier :str =None) -> None:
        self._obj = obj
        self._cls = type(obj) if cls is None else cls
        self._identifier = self._cls if identifier is None else identifier
        self._lastAccess = None
    
    def getObj(self):
        self._lastAccess = datetime.now()
        return self._obj

    def getClass(self):
        return self._cls

    def getIdentifier(self):
        return self._identifier
        