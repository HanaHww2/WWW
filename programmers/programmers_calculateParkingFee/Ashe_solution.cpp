// 2022 카카오_ 주차 요금 계산: https://programmers.co.kr/learn/courses/30/lessons/92341
#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
using namespace std;

int calcTime(string t1, string t2)
{
    int result = 0;
    int h1, m1, h2, m2;
    
    h1 = stoi(t1.substr(0, 2));
    m1 = stoi(t1.substr(3, 2));
    h2 = stoi(t2.substr(0, 2));
    m2 = stoi(t2.substr(3, 2));

    m1 += h1 * 60;
    m2 += h2 * 60;
    result = m2 - m1;
    
    return result;
}

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    map<string, vector<string>> records_by_cars;
    map<string, vector<string>>::iterator p;
    
    int i, j; 
    for (i = 0; i < records.size(); i++)
    {
        string time, car;
        stringstream ss(records[i]);
        ss >> time; ss >> car;
        
        if (records_by_cars.find(car) != records_by_cars.end())
            records_by_cars[car].push_back(time);
        else
            records_by_cars[car] = { time };
    }


    for (p = records_by_cars.begin(); p != records_by_cars.end(); p++)
    {
        int time = 0;
        vector<string> times = p->second;
        if (times.size() % 2 == 0)
        {
            for (i = 0; i < times.size(); i+=2)
            {
                time += calcTime(times[i], times[i + 1]);
            }
        }
        else
        {
            for (i = 0; i < times.size()-1; i+=2)
            {
                time += calcTime(times[i], times[i + 1]);
            }
            time += calcTime(times[times.size() - 1], "23:59");
        }
        if (time <= fees[0]) answer.push_back(fees[1]);
        else answer.push_back(fees[1] + ceil((time - fees[0]) / fees[2]) * fees[3]);
    }

    return answer;
}