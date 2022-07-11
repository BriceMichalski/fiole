
from typing import Any

from flask import jsonify


class Response():
    
    _body :Any = ""
    _headers :dict = {}
    _status :int = 0
    _jsonify = False

    def body(self, body :Any):
        self._body = body
        return self

    @staticmethod
    def body(body :Any):
        resp = Response()
        resp._body = body
        return resp

    def status(self, status :int):
        self._status = status
        return self

    @staticmethod
    def status(status :int):
        resp = Response()
        resp._status = status
        return resp

    def header(self,key,value):
        self._headers[key] = value
        return self
    
    @staticmethod
    def header(key,value):
        resp = Response()
        resp._headers[key] = value
        return resp

    def jsoninfy(self):
        self._jsonify = True
        return self

    def send(self):
        if self._jsonify:
            self._body = jsonify(self.body)
            
        return self._body,self._status,self._headers

    def __init__(self) -> None:
        pass
