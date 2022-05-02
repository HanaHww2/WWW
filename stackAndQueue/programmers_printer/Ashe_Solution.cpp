// 프린터: https://programmers.co.kr/learn/courses/30/lessons/42587
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> pr, int location) {
    int answer = 1, i;
    vector<int> printer;
    for (i = 0; i < pr.size(); i++) printer.push_back(i);
    while (pr.size() > 1)
    {
        if (pr[0] < *max_element(pr.begin() + 1, pr.end()))
        {
            pr.push_back(pr[0]); pr.erase(pr.begin());
            printer.push_back(printer[0]); printer.erase(printer.begin());
        }
        else
        {
            if (printer[0] == location) return answer;
            pr.erase(pr.begin()); printer.erase(printer.begin());
            answer++;
        }
    }
    return answer;
}
/*
* 
* [다른 사람 풀이]: Queue 사용
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int solution(vector<int> priorities, int location) {
    queue<int> printer; vector<int> sorted; //printer: queue에 index 삽입. sorted: 정렬된 결과 저장용
    for(int i=0; i<priorities.size(); i++) printer.push(i);
    
    while(!printer.empty()) {
        int now_index = printer.front();
        printer.pop();
        if(priorities[now_index] != *max_element(priorities.begin(),priorities.end())) 
            printer.push(now_index); //아닌경우 push
        else {
            sorted.push_back(now_index); priorities[now_index] = 0; //맞는경우
        }
    }
    for(int i=0; i<sorted.size(); i++) if(sorted[i] == location) return i+1; 
}

*/