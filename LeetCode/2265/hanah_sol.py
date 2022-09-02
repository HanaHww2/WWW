import collections
import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    # 최적화 -> 트리를 순회하며 각 노드의 서브트리 합/ 노드 갯수 값을 한번에 구한다.
    # 후위 순회 적용 (왼, 오, 루트)
    def post_order(self, node):
        result = 0
        temp_sum = cnt = 0

        if not node:
            return (temp_sum, cnt, result)

        s1, c1, r1 = self.post_order(node.left)
        s2, c2, r2 = self.post_order(node.right)

        temp_sum += s1 + s2 + node.val
        cnt += c1 + c2 + 1

        result += r1 + r2
        if node.val == math.floor(temp_sum/cnt):
            result += 1

        return temp_sum, cnt, result

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.post_order(root)[2]

    # bfs로 매번 각 노드를 탐색하며 합계를 계산

    def summation(self, node):
        temp_sum, cnt = 0, 0
        queue = collections.deque([node])

        while queue:
            node = queue.popleft()
            if not node:
                continue

            temp_sum += node.val
            cnt += 1

            queue.append(node.left)
            queue.append(node.right)

        return math.floor(temp_sum/cnt)

    # 전위순회 시행
    def pre_order(self, node):

        number = 0
        if not node:
            return number

        if node.val == self.summation(node):
            number += 1
        number += self.pre_order(node.left)
        number += self.pre_order(node.right)

        return number

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        return self.pre_order(root)
