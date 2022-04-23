from html2text import re
from fiole.importation.Controller import *
from fiole.model.Controller import Controller
from fiole.resources.Actuator import Actuator
import json

class HealthController(Controller):

    def __init__(self) -> None:
        self.actuator = Actuator()

    def get(self):
        return self.actuator.getHealth()