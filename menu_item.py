
class MenuItem:
    def __init__(self, name : str, composition : str, price : float):
        if (name is None or composition is None or price <= 0.0):
            raise ValueError("Arguments Invalides")
        self.__name = name
        self.__composition = composition
        self.__price = price

    def getComposition(self) -> str:
        return self.__composition

    def __str__(self) -> str:
        return f"{self.__name}\t{self.__composition}\t{self.__price}"

    def getPrice(self) -> float:
        return self.__price

    def getName(self) -> str:
        return self.__name

    