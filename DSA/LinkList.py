class LinkedList():
    def __init__(self,head=None):
        self.head=head
        def append(self,new_node):
            Current=self.head
            if Current:
                while Current.next:
                    Current= Current.next
                Current.next=new_node
            else:
                self.head=new_node
e1=Node(1)
e2=Node(2)
ll = LinkedList(e1)
