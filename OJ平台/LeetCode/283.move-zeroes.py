#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30109
#
# [283] 移动零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        front=0
        last=len(nums)-1
        count0=0
        for i in range(len(nums)):
                if nums[i]==0:
                    count0+=1
                else:
                    nums[front]=nums[i]
                    front+=1
        while count0:
            nums[last]=0
            count0-=1
            last-=1  
# @lc code=end



#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

