import os
from fiole.model.Component import Component

class Configuration(Component):

    def __init__(self) -> None:
        self.env = os.environ

        
