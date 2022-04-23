from flask_restful import Resource

class Controller(Resource):

    def __init__(self) -> None:
        self._PATH = "/"

    def getRoutes(self) -> str:
        self._PATH