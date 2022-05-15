// H-Index: https://programmers.co.kr/learn/courses/30/lessons/42747
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> citations) {
    int answer = 0, h, idx;
    sort(citations.begin(), citations.end());

    int max = citations[citations.size() - 1] / 2;
    for (h = 0; h < max; h++)
    {
        idx = 0;
        for (int x : citations) if (x >= h) idx++;
        if (idx >= h) answer = h;
    }

    return answer;
}