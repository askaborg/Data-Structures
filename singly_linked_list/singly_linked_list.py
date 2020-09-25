class Node:

    def __init__(self, value=None, next_node=None):
        # data value
        self.value = value
        # next data reference
        self.next_node = next_node

    # get the node value
    def get_value(self):
        return self.value

    # get the next node reference
    def get_next(self):
        return self.next_node

    # update the node's next reference to a new node
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    # check for an empty list
    def list_is_empty(self):
        if self.head is None and self.tail is None:
            return True

    # check for a loner list
    def single_node(self):
        if self.head == self.tail:
            return True

    # return the head value and empty the list
    def empty_the_list(self):
        value = self.head.get_value()
        self.__init__()
        return value

    # add a new node to the last node
    def add_to_tail(self, value):
        # wrap the value in a new node
        new_node = Node(value)

        # case for an empty list
        if self.list_is_empty():
            self.head = self.tail = new_node
        # case for a non-empty list
        else:
            self.tail.set_next(new_node)
            new_node.set_next(self.head)
            self.tail = new_node

    # remove the first node
    def remove_head(self):
        # case for an empty list
        if self.list_is_empty():
            return None

        # case for a single element list
        if self.single_node():
            return self.empty_the_list()
        # case for two or more elements
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value

    # remove the last node
    def remove_tail(self):
        # case for an empty list
        if self.list_is_empty():
            return None

        # case for a single element list
        if self.single_node():
            return self.empty_the_list()
        # case for two or more elements
        else:
            value = self.tail.get_value()
            current_node = self.head
            while current_node.get_next() != self.tail:
                current_node = current_node.get_next()
            self.tail = current_node
            self.tail.set_next(None)
            return value