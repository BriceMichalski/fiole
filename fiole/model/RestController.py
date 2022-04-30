
from flask_restful import Resource
from fiole.model.Controller import Controller

class RestController(Resource,Controller):
    
    def __init__(self) -> None:
        super().__init__()