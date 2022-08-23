# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        length = len(voyage)
        arr = []
        flipped = []

        def makeTraversal(node):
            # 탈출 조건
            if not node or node.val != voyage[len(arr)]:
                return
            # 순회 경로 저장
            arr.append(node.val)

            # 플립 조건
            if node.left and node.left.val != voyage[len(arr)]:
                node.left, node.right = node.right, node.left
                flipped.append(node.val)

            makeTraversal(node.left)
            makeTraversal(node.right)

        if root.val != voyage[0]:  # 최초 시작 노드 조건 성립하는지 확인
            return [-1]

        makeTraversal(root)
        # 순회가 정상적인지 확인
        if len(arr) != length:
            return [-1]

        return flipped
