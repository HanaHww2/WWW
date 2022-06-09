#include<vector>
#include<iostream>
#include<queue>
using namespace std;
struct Pos{
    int x;
    int y;
};

int solution(vector<vector<int> > maps)
{
    int answer = 0;
    int fin_x = maps.size();
    int fin_y = maps[0].size();

    //�湮�� �� �ִ��� üũ�ϴ� ����
    //�� ĭ���� �ִܰŸ� ����
    vector<vector<int> > distance(fin_x, vector<int> (fin_y));
    //����� ĭ��
    queue<Pos> q;

    int arrayX[] = {-1, 0, 1, 0};
    int arrayY[] = {0, 1, 0, -1};

    Pos a;
    a.x = 0;
    a.y = 0;
    q.push(a);
    flag[0][0]=true;
    distance[0][0]=1;

    while(!q.empty()){
        Pos now = q.front();
        q.pop();

        for(int i =0; i<4; i++){
            int tempX = now.x + arrayX[i];
            int tempY = now.y + arrayY[i];

            if(tempX<0||tempX>=fin_x||tempY<0||tempY>=fin_y){
                continue;
            }
            if(maps[tempX][tempY]==0){
                continue;
            }
            if(flag[tempX][tempY]){
                continue;
            }

            Pos temp;
            temp.x = tempX;
            temp.y = tempY;
            q.push(temp);
            flag[tempX][tempY] = true;
            distance[tempX][tempY] = distance[now.x][now.y]+1;
        }
    }

    if(flag[fin_x-1][fin_y-1]==0){
        return -1;
    }
    else{
        return distance[fin_x-1][fin_y-1];
    }
}