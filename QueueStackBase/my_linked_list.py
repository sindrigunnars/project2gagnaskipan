class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        self.size = 0


class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.tail = head

    def __str__(self):
        ret_str = ''
        node = self.head
        while node != None:
            ret_str += str(node.data) + ' '
            node = node.next
        return ret_str
    
    def push_front(self, value):
        node = Node(value, self.head)
        self.head = node
        if self.tail == None:
            self.tail = node

    def pop_front(self):
        if self.head != None:
            ret_val = self.head.data
            self.head = self.head.next
            return ret_val
        else:
            return None

    def push_back(self, value):
        node = Node(value)
        if self.tail == None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def pop_back(self):
        if self.head.next != None:
            temp = self.head
            while temp.next != None:
                prev = temp
                temp = temp.next
            prev.next = None
            ret_val = self.tail.data
            self.tail = prev
            return ret_val
        else:
            ret_val = self.head.data
            self.head = None
            self.tail = None
            return ret_val

    def get_size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
