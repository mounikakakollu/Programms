class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def swapAdjacentNodes(self, head):
        cur = head
        head = head.next
        prev = None
        while(cur and cur.next):
            next = cur.next.next
            cur.next.next = cur
            if(prev):
                prev.next = cur.next
            cur.next = next
            prev = cur
            cur = next
        return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head = head.swapAdjacentNodes(head)
while(head):
    print(head.data)
    head = head.next
