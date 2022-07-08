from fiole.model.threading.Process import Process

class DaemonProcess(Process):

    def __init__(self) -> None:
        super().__init__()