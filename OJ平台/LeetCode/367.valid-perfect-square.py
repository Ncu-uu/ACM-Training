#
# @lc app=leetcode.cn id=367 lang=python3
# @lcpr version=30109
#
# [367] 有效的完全平方数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        left, right=1, num/2
        mid=left+(right-left)//2
        while left<=right:
            if mid**2 == num:
                return True
            elif mid**2 > num:
                right=mid-1
            elif mid**2 < num:
                left=mid+1
        return False
        
# @lc code=end



#
# @lcpr case=start
# 16\n
# @lcpr case=end

# @lcpr case=start
# 14\n
# @lcpr case=end

#

