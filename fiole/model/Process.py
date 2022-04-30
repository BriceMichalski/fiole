from abc import abstractmethod
from fiole.model.Component import Component

class Process(Component):

    def __init__(self) -> None:
        super().__init__()
        self.threadName = ""

    def setName(self,threadName :str):
        self.threadName = threadName
        pass

    @abstractmethod
    def start(self):
        pass