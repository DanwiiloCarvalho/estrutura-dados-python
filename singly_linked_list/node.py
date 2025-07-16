class Node[T]:
    def __init__(self, data: T):
        self.__data: T = data
        self.__next = None

    @property
    def data(self) -> T:
        return self.__data

    @data.setter
    def data(self, data: T) -> None:
        self.__data = data
