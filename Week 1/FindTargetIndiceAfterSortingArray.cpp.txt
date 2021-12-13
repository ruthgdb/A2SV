class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<int> ind;
        int len = nums.size();
        for(int i = 0; i < len; i++) {
            if(nums[i] == target)
                ind.push_back(i);
        }
        return ind;
    }
};