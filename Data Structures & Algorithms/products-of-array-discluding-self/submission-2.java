
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int size = nums.length;
        int[] prefixes = new int[size];
        int[] suffixes = new int[size];
        int[] result = new int[size];
        prefixes[0] = 1;
        suffixes[size - 1] = 1;
        for (int i = 1; i < size; i++) {
            prefixes[i] = prefixes[i - 1] * nums[i - 1];
        }
        for (int i = size - 2; i >= 0; i--) {
            suffixes[i] = suffixes[i + 1] * nums[i + 1];
        }
        for (int i = 0; i < size; i++)
            result[i] = prefixes[i] * suffixes[i];
        return result;
    }
}
