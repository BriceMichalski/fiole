import json
import shutil

from fiole.model.metaclass.Singleton import Singleton
from healthcheck import HealthCheck


class HealthChecker(metaclass=Singleton):

    def __init__(self) -> None:
        self.healthcheck = HealthCheck()
        self.defaultHealthCheck()


    def defaultHealthCheck(self):
        self.addHealthCheck(self.freeSpace)

    def freeSpace(self):
        """free disk space"""
        hdd = shutil.disk_usage("/")
        if hdd.free > 0 : 
            return True, { "msg": "Free disk space: %d GiB" % (hdd.free // (2**30)) }
        else:
            return False, "No space left on device"

    def addHealthCheck(self, func) -> None:
        self.healthcheck.add_check(func)

    def getHealth(self):
        msg, code, header = self.healthcheck.run()
        health = json.loads(msg)
        health.pop("hostname")
        return health, code, header 
