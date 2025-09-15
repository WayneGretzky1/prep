# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p and q:
            if p.val != q.val:
                return False
            if not self.isSameTree(p.left, q.left):
                return False
            if not self.isSameTree(p.right, q.right):
                return False
            
        if p == None and q != None:
            return False
        if p != None and q == None:
            return False

        return True


if __name__ == "__main__":
    test = Solution()

    node2 = TreeNode(2)
    node3 = TreeNode(3)
    tree1 = TreeNode(1,node2,node3)

    node2 = TreeNode(2)
    node3 = TreeNode(3)
    tree2 = TreeNode(1,node2,node3)

    node2 = TreeNode(2)
    tree3 = TreeNode(1,node2)

    node2 = TreeNode()
    node3 = TreeNode(2)
    tree4 = TreeNode(1,node2,node3)

    node2 = TreeNode(2)
    node3 = TreeNode(1)
    tree5 = TreeNode(1,node2,node3)

    node2 = TreeNode(1)
    node3 = TreeNode(2)
    tree6 = TreeNode(1,node2,node3)

    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, node6, node7)
    tree7 = TreeNode(1,node2,node3)

    node8 = TreeNode(8)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, node6, node8)
    tree8 = TreeNode(1,node2,node3)

    assert test.isSameTree(tree1, tree1) == True
    assert test.isSameTree(tree3, tree4) == False
    assert test.isSameTree(tree5, tree6) == False
    assert test.isSameTree(tree7, tree8) == False