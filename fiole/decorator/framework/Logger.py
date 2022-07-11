import inspect
from fiole.resources.Logger import Logger as FioleLogger

"""  Decorator that add logger in your class"""
def Logger(cls):
    def addLoggerAttribute():
        if inspect.isclass(cls):
            setattr(cls, "logger", FioleLogger())
        return cls
    return addLoggerAttribute()
