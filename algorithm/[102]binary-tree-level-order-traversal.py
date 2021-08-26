# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层序遍历结果： 
# 
#  
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 二叉树 
#  👍 967 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def levelOrderDFS(self, root: TreeNode) -> List[List[int]]:
        res = []

        def dfs(root: TreeNode, level):
            if root:
                if level == len(res):
                    res.append([])
                res[level].append(root.val)
                if root.left:
                    dfs(root.left, level + 1)
                if root.right:
                    dfs(root.right, level + 1)

        dfs(root, 0)
        return res
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        res = []
        if not root:
            return res
        q = [root]
        while q:
            child = []
            nodes = []
            for n in q:
                child.append(n.val)
                if n.left:
                    nodes.append(n.left)
                if n.right:
                    nodes.append(n.right)
            res.append(child)
            q = nodes
        return res


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().BinaryTreeLevelOrderTraversal)
