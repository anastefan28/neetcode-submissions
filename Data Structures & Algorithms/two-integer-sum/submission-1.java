class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> prevMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int dif = target - nums[i];
            if (prevMap.containsKey(dif))
                return new int[]{prevMap.get(dif), i};
            prevMap.put(nums[i], i);
        }
        return new int[]{};
    }
}
