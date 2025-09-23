# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def recur(n1, n2, carry):
            if not n1 and not n2 and carry == 0:
                return None
            
            val1 = 0
            val2 = 0
            if n1:
                val1 = n1.val
            if n2:
                val2 = n2.val
            total = val1 + val2 + carry

            node = ListNode(total % 10)
            node.next = recur(n1.next if n1 else None, n2.next if n2 else None, total // 10)
            return node


        
        return recur(l1, l2, 0)
    
if __name__ == "__main__":
    test = Solution()

    node3 = ListNode(3)
    node2 = ListNode(4, node3)
    llist1 = ListNode(2,node2)

    node3 = ListNode(4)
    node2 = ListNode(6, node3)
    llist2 = ListNode(5,node2)

    node3 = ListNode(8)
    node2 = ListNode(0, node3)
    sumllist1 = ListNode(7,node2)



    assert test.addTwoNumbers(llist1, llist2) == sumllist1
    # node3 = ListNode(2)
    # tree2 = ListNode(1,None,node3)
    # assert test.maxDepth(tree2) == 2