from threading import current_thread
from abc import abstractmethod
from fiole.model.framework.Component import Component

class Process(Component):

    def __init__(self) -> None:
        super().__init__()
        self.threadName = ""

    def setName(self,threadName :str):
        self.threadName = threadName

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        current_thread()._stop()