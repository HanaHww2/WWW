#include <vector>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

int maxSubarraySumCircular(vector<int>& nums) {
    if (nums.size() == 1) return nums[0];

    int great = -3 * pow(10, 4);
    int minS = 3 * pow(10, 4);

    int sum, minNum, maxNum;
    sum = minNum = maxNum = nums[0];

    for (int i = 1; i < nums.size(); i++)
    {
        sum += nums[i];

        minNum = min(nums[i], nums[i] + minNum);
        minS = min(minS, minNum);

        maxNum = max(nums[i], nums[i] + maxNum);
        great = max(great, maxNum);
    }

    if (minS == sum) return great;
    else sum -= minS;

    return max(sum, great);
}

void main()
{
	vector<int> nums = { -3, -2, -3 };
	int answer = maxSubarraySumCircular(nums);

	cout << answer << endl;
}