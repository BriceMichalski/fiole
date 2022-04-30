import inspect

from fiole.resources.Container import Container

def Autowired(input):
    
    if callable(input):
        function = input
        def injected_function_argument(instance):
            signature = inspect.signature(function)
            params = []
            for param in signature.parameters.values():
                paramName = param.name
                paramType = param.annotation

                if paramName == "self":
                    params.append(instance)

                if paramName != "self":
                    paramInstance = Container.retrieve(paramType)
                    params.append(paramInstance)

            if signature.return_annotation is not None:
                return function(tuple(params))
            else:
                function(*params)
        output = injected_function_argument


        
    else:
        raise("Autowired decorator not allowed here")


    return output



