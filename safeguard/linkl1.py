class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


linked_list = LinList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.display()