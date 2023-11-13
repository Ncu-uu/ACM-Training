#
# @lc app=leetcode.cn id=35 lang=python3
# @lcpr version=30109
#
# [35] 搜索插入位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            middle=(left+right)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                right = middle-1
            elif nums[middle]<target:
                left = middle+1            
        return left
        
# @lc code=end



#
# @lcpr case=start
# [1,3,5,6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n7\n
# @lcpr case=end

#

