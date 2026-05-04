class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int maxi = 0;
        while (left < right) {
            int width = right - left;
            int area = Math.min(heights[left], heights[right]) * width;
            maxi = Math.max(maxi, area);
            if (heights[left] <= heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxi;
    }

}