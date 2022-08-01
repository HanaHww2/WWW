#include <vector>
using namespace std;

int maxSubArray(vector<int>& nums) {

    int great = nums[0];

    for (int i = 1; i < nums.size(); i++)
    {
        nums[i] = max(nums[i], nums[i - 1] + nums[i]);
        great = max(great, nums[i]);
    }

    return great;
}