from html2text import re
from fiole.model.RestController import RestController
from fiole.resources.HealthChecker import HealthChecker

class HealthController(RestController):

    def __init__(self) -> None:
        self.healthChecker = HealthChecker()

    def get(self):
        return self.healthChecker.getHealth()