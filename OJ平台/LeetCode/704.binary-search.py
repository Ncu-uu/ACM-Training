#
# @lc app=leetcode.cn id=704 lang=python3
# @lcpr version=30108
#
# [704] 二分查找
#


# @lcpr-template-start

# @lcpr-template-end

# @lc code=start

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            middle=(left+right)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                right = middle-1
            elif nums[middle]<target:
                left = middle+1            
        return -1
# @lc code=end



#
# @lcpr case=start
# [-1,0,3,5,9,12]\n9\n
# @lcpr case=end

# @lcpr case=start
# [-1,0,3,5,9,12]\n2\n
# @lcpr case=end

#

