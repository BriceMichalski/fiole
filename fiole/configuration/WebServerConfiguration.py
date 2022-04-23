import os
import time
from fiole.model.LogLevel import LogLevel 
from fiole.model.metaclass.Singleton import Singleton

class WebServerConfigutation(metaclass=Singleton):
    def __init__(self) -> None:
        self._port = os.getenv("SERVER_PORT")
        self._host = os.getenv("SERVER_HOST")
        self._logLevel = LogLevel.__dict__.get(os.getenv("LOG_LEVEL"))
        self._appName = os.getenv("APP_NAME")

    @property
    def port(self):
        return self._port

    @property
    def host(self):
        return self._host

    @property
    def logLevel(self):
        return self._logLevel

    @property
    def appName(self):
        return self._appName