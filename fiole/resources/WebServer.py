import logging
from posix import environ
import sys
import os
import inspect
from flask import Flask,g
from flask_restful import Api

from fiole.configuration.WebServerConfiguration import WebServerConfigutation
from fiole.resources.Logger import Logger
from fiole.resources.Router import Router

class WebServer():

    def __init__(self) -> None:
        """Fiole server constructor"""

        self.logger = Logger()
        self.config = WebServerConfigutation()
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.router = Router(self.api)
        
    def run(self):
        """ Start fiole server """
        self.init()
        with self.app.app_context():
            self.disableDefaultLogging()
            self.loadRouter()
            self.app.run(
                host=self.config.host,
                port=self.config.port
            )

    def loadRouter(self):
        """ Router loading """
        self.router.routeRegistration()

    def disableDefaultLogging(self):
        cli = sys.modules['flask.cli']
        cli.show_server_banner = lambda *x: None
        logging.getLogger('werkzeug').disabled = True
    
    def init(self):
        self.logger.info("Starting {} application".format(self.config.appName))
        self.logger.info("Server listen on {host}:{port}".format(               
            host=self.config.host,
            port=self.config.port
        ))
        self.logger.debug("Server running in DEBUG mode")
        