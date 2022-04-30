import json
import inspect 
import threading

from datetime import datetime

from fiole.model.LogLevel import LogLevel
from fiole.model.metaclass.Singleton import Singleton
from fiole.configuration.WebServerConfiguration import WebServerConfigutation

class Logger(metaclass=Singleton):

    def __init__(self) -> None:
            self.config = WebServerConfigutation()

    def write(self, level, msg):
        logLevel = LogLevel.__dict__.get(level)
        if self.config.logLevel >= logLevel:
            log = self.formatMessage(level,msg)
            print(log)

    def formatMessage(self, level, msg):
        now = datetime.now()

        caller = inspect.stack()[3]
        moduleName = inspect.getmodule(caller[0]).__name__
        origin = moduleName
        if self.config.logLevel == LogLevel.TRACE:
            origin += ":" + caller.function + ":" + str(caller.lineno)

        threadName = threading.current_thread().name
        formattedMessage = {
            "datetime": str(now),
            "level": level,
            "message": msg,
            "origin": origin,
            "thread": threadName,
        }

        return json.dumps(formattedMessage)

    def info(self, msg):
        self.write("INFO",msg)
        
    def debug(self, msg):
        self.write("DEBUG",msg)

    def error(self, msg):
        self.write("ERROR",msg)

    def trace(self,msg):
        self.write("TRACE",msg)