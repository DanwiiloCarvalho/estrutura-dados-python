from singly_linked_list.node import Node


class Queue[T]:
    def __init__(self) -> None:
        self.__start: Node[T] | None = None
        self.__end: Node[T] | None = None
        self.__size: int = 0

    @property
    def size(self) -> int:
        return self.__size

    def enqueue(self, data: T) -> None:
        new_node: Node[T] = Node[T](data)

        if not self.__start:
            self.__start = new_node
            self.__end = new_node
        elif self.__end != None:
            self.__end.next = new_node
            self.__end = new_node
        self.__size += 1

    def dequeue(self) -> T | None:
        if not self.__start:
            return None

        popped_node: Node[T] = self.__start
        self.__start = popped_node.next
        popped_node.next = None
        return popped_node.data

    def print_queue(self) -> None:
        print('---Impressão de fila---')
        if not self.__start:
            print('Fila vazia!')
        else:
            current_node: Node[T] | None = self.__start
            while current_node != None:
                print(current_node.data)
                current_node = current_node.next
