class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int,int> map;
    for (int i=0;i<nums.size();i++){
        auto res=map.find(target-nums[i]);
        if(res!=map.end()){
            return vector<int>{res->second,i};
        }
        map[nums[i]] = i;
    }
}
};
