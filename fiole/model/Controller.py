from fiole.model.Component import Component

class Controller(Component):
    _PATH = "/"

    def __init__(self) -> None:
        super().__init__()