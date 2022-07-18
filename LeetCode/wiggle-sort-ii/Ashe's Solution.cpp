#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

void wiggleSort(vector<int>& nums) {
    sort(nums.begin(), nums.end());

    vector<int>::iterator p;
    p = nums.size() % 2 == 0 ? nums.begin() + nums.size() / 2 : nums.begin() + nums.size() / 2 + 1;
    sort(nums.begin(), p, greater<int>());

    int i = 1;
    while (i <= nums.size())
    {
        nums.insert(nums.begin() + i, nums[nums.size() - 1]);
        nums.pop_back();
        i += 2;
    }
}

void main()
{
    vector<int> nums = {1,4,3,4,1,2,1,3,1,3,2,3,3 };
    wiggleSort(nums);

    for (int i : nums) cout << i << " ";
}