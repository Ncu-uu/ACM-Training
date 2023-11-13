#
# @lc app=leetcode.cn id=69 lang=python3
# @lcpr version=30109
#
# [69] x 的平方根 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, ans=0, x, -1
        while left<=right:
            mid=left+(right-left)//2
            if mid**2 <=x:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 8\n
# @lcpr case=end

#

