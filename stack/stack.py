from singly_linked_list.node import Node


class Stack[T]:
    def __init__(self) -> None:
        self.__top: Node[T] | None = None

    def push(self, data: T) -> None:
        new_node = Node[T](data)
        if self.__top:
            new_node.next = self.__top
        self.__top = new_node

    def pop(self) -> T | None:
        if self.__top:
            popped_node: Node[T] = self.__top
            self.__top = self.__top.next
            popped_node.next = None
            return popped_node.data
        return None

    def peek(self) -> T | None:
        if self.__top:
            return self.__top.data
        return None
