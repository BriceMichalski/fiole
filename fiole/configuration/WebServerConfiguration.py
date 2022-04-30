import os
import time
from fiole.model.LogLevel import LogLevel 
from fiole.model.metaclass.Singleton import Singleton

class WebServerConfigutation(metaclass=Singleton):
    def __init__(self) -> None:
        self._port = os.getenv("SERVER_PORT") if os.getenv("SERVER_PORT") is not None else 8080
        self._host = os.getenv("SERVER_HOST") if os.getenv("SERVER_HOST") is not None else "0.0.0.0"
        self._logLevel = LogLevel.__dict__.get(os.getenv("LOG_LEVEL")) if os.getenv("LOG_LEVEL") is not None else LogLevel.INFO
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