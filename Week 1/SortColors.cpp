class Solution {
public:
    void sortColors(vector<int>& nums) {
        int len = nums.size();
       for(int i = 0; i < len; i++) {
           for(int j = 0; j < len ; j++) {
               if(nums[i] < nums[j])
                   swap(nums[i], nums[j]);
           } 
       } 
    }
};