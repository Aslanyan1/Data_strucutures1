class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None

    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, index, element):
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        pos = 0
        while current and pos < index - 1:
            current = current.next
            pos += 1
        if current is None:
            print("Index out of bounds")
            return
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


    def remove(self, value):
        if self.head is None:
            print("List is empty")
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        print("Value not found in the list")

    def pop(self, index = None):
        if self.head is None:
            print("List is empty")
            return None
        if index == None:
            



ll = Linked_List()
ll.append(1)
ll.append(2)
ll.insert(1, 100)
ll.remove(2)
ll.print_list()
