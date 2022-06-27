// 타겟넘버: https://programmers.co.kr/learn/courses/30/lessons/43165?language=cpp
// 재귀로 처리
#include <vector>
using namespace std;

int solution(vector<int> numbers, int target) {
    if (numbers.size() == 0)
    {
        if (target == 0) return 1;
        else return 0;
    }
    else
    {
        vector<int> numbers0;
        numbers0.assign(numbers.begin() + 1, numbers.end());
        return solution(numbers0, target + numbers[0]) + solution(numbers0, target - numbers[0]);
    }
}
/*
* [다른 사람의 풀이]: DFS(깊이 우선 탐색) 사용 -> 훨씬 빨리 완료된다.
* 
#include <vector>
using namespace std;

int total;

void DFS(vector<int> &numbers, int &target,int sum,int n) {
    if(n >= numbers.size()){
        if(sum == target) total++;
        return;
    }

    DFS(numbers, target, sum + numbers[n], n+1);
    DFS(numbers, target, sum - numbers[n], n+1);
}

int solution(vector<int> numbers, int target) {

    DFS(numbers, target, numbers[0] , 1);
    DFS(numbers, target, -numbers[0], 1);

    return total;
}
*/