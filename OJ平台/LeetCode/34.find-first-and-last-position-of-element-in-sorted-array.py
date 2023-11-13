#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30109
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last=-1, -1
        
        left, right = 0, len(nums)-1
        while left <= right:
            middle=left+(right-left)//2
            if nums[middle]==target:
                if middle==0 or nums[middle-1]!=target:
                    first=middle
                    break
                else:
                    right=middle-1  
            elif nums[middle]>target:
                right = middle-1
            elif nums[middle]<target:
                left = middle+1
        
        left, right = 0, len(nums)-1
        while left <= right:
            middle=left+(right-left)//2
            if nums[middle]==target:
                if(middle==len(nums)-1 or nums[middle+1]!=target):
                    last=middle
                    break
                else:
                    left=middle+1
            elif nums[middle]>target:
                right = middle-1
            elif nums[middle]<target:
                left = middle+1  
                
        return [first,last]
# @lc code=end
#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

