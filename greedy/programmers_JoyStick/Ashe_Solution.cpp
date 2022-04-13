// 탐욕법_조이스틱: https://programmers.co.kr/learn/courses/30/lessons/42860
#include <string>
using namespace std;

int solution(string name) {
    /* [Idea]
    * 1. name[i]에서 가장 가까운 A가 아닌 문자 name[ind] 찾기
    * 2. 여기서 조이스틱을 움직이는 최단 경로는
    *   (1) 원점 –> i –> 원점 –> ind
    *   (2) 원점 –> ind –> 원점 –> i
    *   이렇게 두 가지이다.
    * 3. ∴ (i : 0 ~ name.length)에 대해 조이스틱을 움직이는 최소값을 구한다.
    */
    int answer = 0;
    int n = name.length();
    int turn = n - 1; // 조이스틱을 한 방향으로만 쭉 움직였을 때
    int turnif = 0;
    int i, ind;

    for (i = 0; i < n; i++)
    {
        if (name[i] - 'A' < 14) answer += name[i] - 'A';
        else answer += 'Z' - name[i] + 1;

        ind = i + 1;
        while (ind < n && name[ind] == 'A')ind++;

        turnif = i + n - ind + (i < n - ind ? i : n - ind);
        turn = turn < turnif ? turn : turnif;
    }

    return answer+ turn;
}