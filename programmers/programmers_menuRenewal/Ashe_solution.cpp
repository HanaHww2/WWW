// 2021 카카오_ 메뉴 리뉴얼: https://programmers.co.kr/learn/courses/30/lessons/72411
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

/*
* [Idea]
* for(i = 0; i<course.size(); i++) for(j = 0; j< orders.size(); j++) 
       2번 이상 주문된 course[i]개수의 메뉴 조합을 모두 찾는다.
* vector<Pair> ordered: 주문된 메뉴 course[i]개 조합 comb와 주문횟수 frequency의 배열
* 1. 각 주문을 돌면서 course[i]만큼 order을 자른다X  -> string menu;
*   1-1. 만약 ordered에 없으면: ordered.push_back(Pair(menu));
*   1-2. 있으면: 해당 Pair를 찾아서 frequency++;
* 2. ordered 에서 frequency가 가장 높은 Pair를 찾아 answer.push_back(comb); //여러 개일 수 있다
* 3. 오름차순 정렬하여 return: sort(answer.begin(), answer.end());
*/

vector<string> makeComb(string menu, int num)
{
    vector<string> combs;
    vector<char> arr;
    int r = menu.length() - num;
    if (r < 0) return combs;

    for (int i = 0; i < menu.length(); i++)
        arr.push_back(menu[i]);
    vector<bool> temp(arr.size(), true);

    for (int i = 0; i < r; i++)
        temp[i] = false;

    do {
        string comb = "";
        for (int i = 0; i < arr.size(); ++i)
        {
            if (temp[i]) comb += arr[i];
        }
        combs.push_back(comb);
    } while (next_permutation(temp.begin(), temp.end()));

    return combs;
}

class Pair
{
public:
    string comb; int frequency;
    Pair(string c)
    {
        comb = c; frequency = 1;
    }

};

struct isExist : public binary_function<Pair, string, bool>
{
public:
    bool operator()(const Pair a, string b) const
    {
        return (a.comb == b);
    }
};

bool compareFreq(Pair& a, Pair& b)
{
    return a.frequency > b.frequency;
};
vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    vector<Pair> ordered;
    int i, j, k;

    for (i = 0; i < course.size(); i++)
    {
        ordered = {};
        for (j = 0; j < orders.size(); j++)
        {
            sort(orders[j].begin(), orders[j].end());
            vector<string> combs = makeComb(orders[j], course[i]);

            for (k = 0; k < combs.size(); k++)
            {
                int idx = find_if(ordered.begin(), ordered.end(), bind2nd(isExist(), combs[k])) - ordered.begin();
                if (idx == ordered.size())
                    ordered.push_back(Pair(combs[k]));
                else
                    ordered[idx].frequency++;
            }
        }
        
        sort(ordered.begin(), ordered.end(), compareFreq);
        int max = ordered[0].frequency;
        if (max < 2) continue;
        for (j = 0; j < ordered.size(); j++)
        {
            if (ordered[j].frequency == max) answer.push_back(ordered[j].comb);
            else break;
        }
        
    }
    sort(answer.begin(), answer.end());
    return answer;
}