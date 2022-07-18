// 탐욕법_큰 수 만들기: https://programmers.co.kr/learn/courses/30/lessons/42883
#include <string>
#include <vector>
using namespace std;

string solution(string number, int k) {
    string answer = "";
    int i, j, maxidx; char num;
    int len = number.length() - k, start = 0;
    for (i = 0; i < len; i++)
    {
        num = number[start];
        for (j = start; j <= k + i; j++)
        {
            if (num < number[j])
            {
                num = number[j];
                maxidx = j;
            }
        }
        start = ++maxidx;
        answer += num;
    }
    return answer;
}