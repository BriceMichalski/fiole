class A:
    def __init__(self) -> None:
        pass

class B(A):
    def __init__(self) -> None:
        pass

class C(B):
    def __init__(self) -> None:
        pass


foo = C()

print(issubclass(C,A))
