class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Create complement array
        vector<int> complements(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            complements[i] = target - nums[i];
        }
        
        // Now we need to find if any nums[i] equals any complements[j]
        unordered_map<int, int> numMap;
        for (int i = 0; i < nums.size(); i++) {
            numMap[nums[i]] = i;
        }
        
        for (int j = 0; j < complements.size(); j++) {
            if (numMap.find(complements[j]) != numMap.end() && numMap[complements[j]] != j) {
                return {j, numMap[complements[j]]};
            }
        }
        return {};
    }
};