from node import Node


class LinkedList[T]:
    def __init__(self) -> None:
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None

    @property
    def head(self) -> Node[T] | None:
        return self.__head

    @property
    def tail(self) -> Node[T] | None:
        return self.__tail

    def insert_at_beginning(self, data: T) -> None:
        new_node: Node[T] = Node[T](data)
        if self.__head and self.__tail:
            new_node.next = self.__head
            self.__head = new_node
        else:
            self.__tail = new_node
            self.__head = new_node

    def insert_at_end(self, data: T) -> None:
        new_node: Node[T] = Node[T](data)
        if self.__tail:
            self.__tail.next = new_node
            self.__tail = new_node
        else:
            self.__tail = new_node
            self.__head = new_node

    def remove_at_beginning(self) -> Node[T] | None:
        if self.__head:
            head_value: Node[T] = self.__head
            self.__head = self.__head.next
            return head_value
        return None

    def remove_at_end(self) -> Node[T] | None:
        if not self.__head:
            return None
        else:
            current_node: Node[T] | None = self.__head
            previous_node: Node[T] | None = None
            while current_node != self.__tail and current_node != None:
                previous_node = current_node
                current_node = current_node.next

                if current_node == self.__tail:
                    previous_node.next = None
                    self.__tail = previous_node

                    return current_node

            self.__head = None
            self.__tail = None
            return current_node

    def search(self, data: T) -> bool:
        if self.__head:
            current_node: Node[T] | None = self.__head
            while True:
                if current_node:
                    if current_node.data == data:
                        return True
                    current_node = current_node.next
                if not current_node:
                    break
        return False

    def print_linked_list(self) -> None:
        print('-' * 5 + 'Linked List' + '-' * 5)
        current_node: Node[T] | None = self.__head

        if not self.__head:
            print('Lista vazia!')
        else:
            while True:
                if current_node != None:
                    print(f'{current_node.data}')
                    current_node = current_node.next
                else:
                    break
