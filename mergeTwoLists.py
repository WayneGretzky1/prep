# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head = ListNode()
        current = head
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1 != None:
            current.next = list1
        else:
            current.next = list2
        # current.next = list1 or list2
        return head.next

def print_list(node):
    while node:
        print(node.val, end=" → ")
        node = node.next
    print("None")

if __name__ == "__main__":


    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3


    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6


    linkedlist = Solution()
    merged = linkedlist.mergeTwoLists(node1, node4)
    print_list(merged)
