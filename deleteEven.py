def deleteEven(head):
    while head and head.val % 2 == 0:
        head = head.next
    curr = head
    while curr and curr.next:
        if curr.next.val % 2 == 0:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head