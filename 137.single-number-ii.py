#
# @lc app=leetcode.cn id=137 lang=python3
# @lcpr version=21917
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans

# @lc code=end



#
# @lcpr case=start
# [2,2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,1,0,1,99]\n
# @lcpr case=end

#

