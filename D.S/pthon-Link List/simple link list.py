class Node:
    def __init__(Self,key):
        Self.key = key
        Self.next = None
def traverse(head):
    curr = head
    while curr != None:
        print(curr.key,end=' ')
        curr = curr.next
def search(head,x):
    pos = 1
    curr = head
    while curr != None:
        if curr.key == x:
            return pos
        pos += 1
        curr = curr.next
    return -1
def inb(head,key):
    temp = Node(key)
    temp.next = head
    return temp
def ine(head,key):
    if head == None:
        return Node(key)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(key)
    return head
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
# traverse(head)
# print(search(head,x=10))
# head = inb(head,key = 40)
head = ine(head,key = 40)
traverse(head)