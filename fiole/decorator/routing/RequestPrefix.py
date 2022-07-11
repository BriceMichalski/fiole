from fiole.model.framework.Controller import Controller


def RequestPrefix(prefix):
    def definedBP(cls):
        if issubclass(cls,Controller):
            setattr(cls, "BLUEPRINT_PREFIX", prefix)
        return cls
    return definedBP
