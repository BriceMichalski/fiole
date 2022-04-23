from datetime import datetime

class RegistryItem():

    def __init__(self, obj, identifier :str ="") -> None:
        self._obj = obj
        self._cls = type(obj).__name__
        self._lastAccess = None
        self._identifier = identifier
    
    def getObj(self):
        self._lastAccess = datetime.now()
        return self._obj

    def getClass(self):
        return self._cls

    def getIdentifier(self):
        return self._identifier
        