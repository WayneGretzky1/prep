# Two pointers
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ptr1 = head
        ptr2 = head
        while ptr2 and ptr2.next:
            # check node references
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if ptr2 == ptr1:
                return True

        return False
    

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    llist1 = node1

    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node2
    llist2 = node1


    linkedlist = Solution()
    assert linkedlist.hasCycle(llist1) == False
    assert linkedlist.hasCycle(llist2) == True