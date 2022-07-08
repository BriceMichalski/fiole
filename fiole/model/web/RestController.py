
from flask_restful import Resource
from fiole.model.web.Controller import Controller

class RestController(Resource,Controller):
    
    def __init__(self) -> None:
        super().__init__()