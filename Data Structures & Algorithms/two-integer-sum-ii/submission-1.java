class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 1;
        int right = numbers.length;
        while (left < right) {
            if (numbers[left-1] + numbers[right-1] == target)
                return new int[]{left, right};
            if (numbers[left-1] + numbers[right-1] < target)
                left++;
            else right--;
        }
        return new int[0];
    }
}