// 기능 개발: https://programmers.co.kr/learn/courses/30/lessons/42586
#include <string>
#include <vector>
using namespace std;

vector<int> solution(vector<int> p, vector<int> s) {
    vector<int> answer;
    int i, n;
    while (p.size() > 0)
    {
        for (i = 0; i < p.size(); i++) p[i] += s[i];

        n = 0;
        // TODO: progress가 100이상인 것들을 검사해서 삭제, 그 개수를 answer에 push_back
        if (p[0] >= 100)
        {
            n++;
            for (i = 1; i < p.size(); i++)
            {
                if (p[i] >= 100) n++;
                else break;
            }
        }

        for (i = 0; i < n; i++)
        {
            p.erase(p.begin());  s.erase(s.begin());
        }

        if (n > 0) answer.push_back(n);
    }

    return answer;
}

/*
* 다른 풀이
* 
#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;

    int day;
    int max_day = 0;
    for (int i = 0; i < progresses.size(); ++i)
    {
        day = (99 - progresses[i]) / speeds[i] + 1;

        if (answer.empty() || max_day < day)
            answer.push_back(1);
        else
            ++answer.back();

        if (max_day < day)
            max_day = day;
    }

    return answer;
}
*/