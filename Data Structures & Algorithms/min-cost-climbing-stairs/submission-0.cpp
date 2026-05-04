class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
    int size = cost.size();
    vector<int> res(size);
    res[0] = cost[0];
    res[1] = cost[1];
    for (int i = 2;i < size;i++)
        res[i] = min(res[i - 1], res[i - 2]) + cost[i];
    return min(res[size - 1], res[size - 2]);


}
};
