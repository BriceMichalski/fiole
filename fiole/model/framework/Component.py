from fiole.resources.Logger import Logger
from fiole.model.framework.Container import Container

class Component:
    def __init__(self) -> None:
        self.logger :Logger = Container.retrieve(Logger)
