from fiole.decorator.routing.RequestMapping import GetMapping
from fiole.decorator.routing.RequestPrefix import RequestPrefix
from fiole.model.framework.Container import Container
from fiole.model.framework.RestController import RestController
from fiole.resources.HealthChecker import HealthChecker


@RequestPrefix("/actuator")
class ActuatorController(RestController):

    def __init__(self) -> None:
        self.healthChecker :HealthChecker = Container.retrieve(HealthChecker)

    @GetMapping("/health")
    def health(self):
        return self.healthChecker.getHealth()
