# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1 
            return 1 + max(left, right)
        return height(root) != -1


if __name__ == "__main__":
    test = Solution()

    node2 = TreeNode(9)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node3 = TreeNode(20, node4, node5)
    tree1 = TreeNode(3,node2,node3)

    node3 = TreeNode(2)
    tree2 = TreeNode(1,None,node3)


    assert test.isBalanced(tree1) == True
    # assert test.maxDepth(tree2) == 2