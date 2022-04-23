def Path(path):
    def deco(cls):
        def getAttr(self, attr_name="PATH"):
            return getattr(self, "_PATH")
        def setAttr(self, value, attr_name="PATH"):
            pass
        prop = property(getAttr, setAttr)
        setattr(cls, "PATH", prop)
        setattr(cls, "_PATH", path) 
        return cls
    return deco