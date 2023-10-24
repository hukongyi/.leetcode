#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30102
#
# [209] 长度最小的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = 1e5+1
        subsum = 0
        l = 0
        r = 0
        while(r < len(nums)):
            subsum += nums[r]
            r += 1
            if subsum >= target:
                while(subsum >= target):
                    subsum -= nums[l]
                    l += 1
                minlen = min(minlen, r-l+1)
        return minlen if minlen != 1e5+1 else 0


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
