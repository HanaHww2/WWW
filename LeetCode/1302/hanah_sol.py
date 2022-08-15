# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        arr = []  # 최대 레벨에 존재하는 노드(리프노드) 배열

        def dfs(node, depth):
            nonlocal arr
            nonlocal max_depth

            if not node: # 탈출 조건 1
                return

            if not node.left and not node.right: # 탈출 조건2
                if max_depth > depth:
                    return
                if max_depth == depth:
                    arr.append(node.val)
                elif max_depth < depth:
                    arr = [node.val]
                max_depth = depth
            else:
                dfs(node.left, depth+1)
                dfs(node.right, depth+1)

        dfs(root, 0)

        return sum(arr)
