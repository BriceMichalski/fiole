
from fiole.model.framework.Controller import Controller
from fiole.model.web.MimeType import MimeType


class RestController(Controller):
    
    ACCEPT :str = MimeType.JSON
    CONTENT_TYPE :str = MimeType.JSON

    def __init__(self) -> None:
        super().__init__()

    def prefilledResponse(self):
        return super().prefilledResponse().jsoninfy()
