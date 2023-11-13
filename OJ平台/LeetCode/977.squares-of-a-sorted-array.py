#
# @lc app=leetcode.cn id=977 lang=python3
# @lcpr version=30109
#
# [977] 有序数组的平方
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, k=0, len(nums)-1, len(nums)-1
        res=[None]*len(nums)
        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                res[k]=nums[l] **2
                l+=1
            else:
                res[k]=nums[r] ** 2
                r-=1
            k-=1
        return res
# @lc code=end



#
# @lcpr case=start
# [-4,-1,0,3,10]\n
# @lcpr case=end

# @lcpr case=start
# [-7,-3,2,3,11]\n
# @lcpr case=end

#

