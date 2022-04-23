import json
import sys 

from datetime import datetime

from fiole.model.metaclass.Singleton import Singleton
from fiole.model.LogLevel import LogLevel
from fiole.configuration.WebServerConfiguration import WebServerConfigutation

class Logger(metaclass=Singleton):

    def __init__(self) -> None:
            self.config = WebServerConfigutation()

    def write(self, level, msg):
        logLevel = LogLevel.__dict__.get(level)
        if self.config.logLevel >= logLevel:
            print(self.formatMessage(level,msg))



    def formatMessage(self, level, msg):
        now = datetime.now()
        formattedMessage = {
            "datetime": str(now),
            "level": level,
            "message": msg
        }

        return json.dumps(formattedMessage)

    def info(self, msg):
        self.write("INFO",msg)
        
    def debug(self, msg):
        self.write("DEBUG",msg)

    def error(self, msg):
        self.write("ERROR",msg)