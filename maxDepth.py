# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth) 
                stack.append((node.left, depth+1))  
                stack.append((node.right, depth+1))               

        return max_depth
        
if __name__ == "__main__":
    test = Solution()

    node2 = TreeNode(9)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node3 = TreeNode(20, node4, node5)
    tree1 = TreeNode(3,node2,node3)

    node3 = TreeNode(2)
    tree2 = TreeNode(1,None,node3)


    assert test.maxDepth(tree1) == 3
    assert test.maxDepth(tree2) == 2