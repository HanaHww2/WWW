import sys
import heapq


class Solution:

    def manhattanDistance(self, a, b):
        # return sum([abs(z1 - z2) for z1, z2 in zip(a, b)])
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    # 조건을 잘 읽자!
    # 이미 한 번 계산한 거리는 두 번 계산하지 않도록 기록을 한다.
    # 거리 테이블 생성 (대칭 행렬), 상향식, 타뷸레이션

    # 가중치가 있는 무방향 싸이클이 없는 그래프(트리)
    # 최소 신장 트리 문제, 프림 알고리즘
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if len(points) < 2:
            return 0

        length = len(points)
        weight = collections.defaultdict(lambda: sys.maxsize)
        heap = []
        connected = {0}
        summation = 0
        i = 0

        while len(connected) < length:
            # 직전 연결된 정점 i 기준으로 순회
            j = -1
            while j < length-1:
                j += 1
                if j in connected:
                    continue  # 이미 연결된 정점 패스
                temp_d = self.manhattanDistance(points[i], points[j])
                if temp_d < weight[j]:
                    weight[j] = temp_d
                    # 힙 대신, bisect.insert()? 사용한 코드 확인해보기
                    heapq.heappush(heap, [temp_d, j])

            temp = heapq.heappop(heap)
            while temp[1] in connected:
                temp = heapq.heappop(heap)

            i = temp[1]  # 직전 연결된 정점 순회
            weight[i] = sys.maxsize
            connected.add(i)

            summation += temp[0]

        return summation
