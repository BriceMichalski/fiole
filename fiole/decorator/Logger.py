import inspect
from fiole.resources.Logger import Logger as FioleLogger
from fiole.resources.Container import Container

"""  Decorator that add logger in your class"""
def Logger(cls):
    def addLoggerAttribute():
        if inspect.isclass(cls):
            setattr(cls, "logger", FioleLogger())
        return cls
    return addLoggerAttribute()
