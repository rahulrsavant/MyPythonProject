class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

root=Node()

class SingleLinkList(Node):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, pointer, data):
        if pointer is None :
            new_node = Node(data)
            root = new_node

        elif pointer.next is None:
            new_node = Node(data)
            pointer.next = new_node

        elif pointer.next is not None:
            return self.insert_at_end(pointer.next, data)


    def list_length(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next
        return count

    def print_list(self,current):
        print("List Start.")
        while current is not None:
            print(current.data)
            current = current.next

        print("List End.")


if __name__ == '__main__':
  #  root = Node()  cnage through github
    ll = SingleLinkList()
    ll.insert_at_end(root, 2)
    ll.insert_at_end(root, 3)
    ll.insert_at_end(root, 4)
    ll.insert_at_end(root, 5)
    ll.print_list(root)
    print(ll.list_length())
