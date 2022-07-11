from fiole.model.framework.Controller import Controller
from fiole.resources.Logger import Logger

"""  Decorator that add _PATH varaible on Controller"""
def Path(path):
    def pathDeco(cls):
        if issubclass(cls,Controller):
            setattr(cls, "_PATH", path)
        else:
            Logger().debug("Decorator Path it's made for fiole.model.Controller subclass only, {classname} isn't".format(classname=cls.__module__)) 
        return cls
    return pathDeco