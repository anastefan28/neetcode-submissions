class Solution {
public:
    bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
        int n = matrix.size();
        int m = matrix[0].size();
        int left = 0, right = n * m - 1;
        while (left <= right)
        {
            int mid = (left + right) / 2;
            int element = matrix[mid / m][mid % m];
            if (element == target) return true;
            if (element < target) left = mid + 1;
            else right = mid - 1;
        }
        return false;
    }
};
