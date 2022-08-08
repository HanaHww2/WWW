class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 프림
        dic = {(x,y):float('inf') if i else 0 for i,(x,y) in enumerate(points)}
        # print(dic)
        result = 0 
        while dic :
            x,y = min(dic,key = dic.get) 
            # dic 의 value 값중에 가장 작은 값 가진 키 찾기
            # min(dic.keys(), key=lambda x : dic[x]) == min(dic,key = dic.get) 
            result += dic.pop((x,y))
            for a,b in dic : 
                dic[(a,b)] = min(dic[(a,b)],abs(a-x) + abs(b-y))
            # print(dic)
        return result
