class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> stack;
        vector<int> result(temperatures.size());
        for (int i = 0;i < temperatures.size();i++) {
            while (!stack.empty() && temperatures[i] > stack.top().first)
            {
                result[stack.top().second] = i - stack.top().second;
                stack.pop();
            }
            stack.push(make_pair(temperatures[i], i));
        }
        return result;
    }
};
