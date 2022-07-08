
from fiole.model.web.RestController import RestController
from fiole.resources.HealthChecker import HealthChecker

class HealthController(RestController):

    def __init__(self) -> None:
        self.healthChecker = HealthChecker()

    def get(self):
        return self.healthChecker.getHealth()