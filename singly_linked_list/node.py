from typing import Optional


class Node[T]:
    def __init__(self, data: T):
        self.__data: T = data
        self.__next: Optional['Node[T]'] = None

    @property
    def data(self) -> T:
        return self.__data

    @data.setter
    def data(self, data: T) -> None:
        self.__data = data

    @property
    def next(self) -> Optional['Node[T]']:
        return self.__next

    @next.setter
    def next(self, node: Optional['Node[T]']) -> None:
        self.__next = node
