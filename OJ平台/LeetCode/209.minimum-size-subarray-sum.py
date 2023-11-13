#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30109
#
# [209] 长度最小的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #滑动窗口
        
        
        
        
        
        # 暴力，超时
        # sum, res =0, len(nums)+1 
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         sum += nums[j]
        #         if sum >= target:
        #             res = j-i+1 if j-i+1<res else res
        #     sum=0
        # return 0 if res==len(nums)+1 else res
                    
                
# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

