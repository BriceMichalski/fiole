from flask import Flask

from fiole.configuration.WebServerConfiguration import WebServerConfigutation
from fiole.resources.AutoLoader import AutoLoader
from fiole.resources.Logger import Logger

class WebServer():   

    def __init__(self) -> None:
        """Fiole server constructor"""
        self.app = Flask(__name__)
        self.autoloader = AutoLoader()

        self.logger = Logger()
        self.config = WebServerConfigutation()

    def run(self):
        """ Start fiole server """
        
        self.logger.info("Starting {} application".format(self.config.appName))
        self.autoloader.load(self.app)
        
        self.logger.info("Server listen on {host}:{port}".format(               
            host=self.config.host,
            port=self.config.port
        ))
        self.logger.debug("Server running in DEBUG mode")

        self.app.run(
            host=self.config.host,
            port=self.config.port,
            threaded=False
        )


if __name__ == "__main__":
    WebServer().run()