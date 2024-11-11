class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)    

        
    
    def printLL(self):
        if self.head is None:
            print('Linked list is empty')
            return
        lnk = ''
        itr = self.head
        while itr:
            lnk += str(itr.data) + ' ---> '
            itr = itr.next
        lnk += 'None' 
        print(lnk)

ll = LinkedList()
#ll.insert_at_beginning(6)
#ll.insert_at_beginning(999)
ll.insert_at_end(8)
ll.printLL()
