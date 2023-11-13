/*
 * @lc app=leetcode.cn id=34 lang=java
 * @lcpr version=30109
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int first=-1,last=-1;

        int left=0;
        int right=nums.length-1;
        while (left<=right) {
            int mid=left+(right-left)/2;
            if (nums[mid]==target) {
                if (mid==0||nums[mid-1]!=target) {
                    first=mid;
                    break;   
                }else right=mid-1;
            }else if(nums[mid]>=target){
                right=mid-1;
            }else if(nums[mid]<=target){
                left=mid+1;
            }
        }
        left=0;
        right=nums.length-1;
        while (left<=right) {
            int mid=left+(right-left)/2;
            if (nums[mid]==target) {
                if (mid==nums.length-1||nums[mid+1]!=target) {
                    last=mid;
                    break;   
                }else left=mid+1;
            }else if(nums[mid]>=target){
                right=mid-1;
            }else if(nums[mid]<=target){
                left=mid+1;
            }
        }

        return new int[]{first,last};
    }
}
// @lc code=end



/*
// @lcpr case=start
// [5,7,7,8,8,10]\n8\n
// @lcpr case=end

// @lcpr case=start
// [5,7,7,8,8,10]\n6\n
// @lcpr case=end

// @lcpr case=start
// []\n0\n
// @lcpr case=end

 */

