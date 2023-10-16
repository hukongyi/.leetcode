#
# @lc app=leetcode.cn id=137 lang=python3
# @lcpr version=21917
#
# [137] 只出现一次的数字 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums_max = math.ceil(math.log2(max([abs(num) for num in nums])))
        for i in range(nums_max+1):
            total = sum([(abs(num) >> i) & 1 for num in nums])
            if total % 3 != 0:
                ans |= (1 << i)
            # print(ans)
            # print(bin(ans))
        if min(nums) < 0:
            i = 31
            total = sum([(num >> i) & 1 for num in nums])
            if total % 3 != 0:
                ans = -ans
        return ans

# @lc code=end


#
# @lcpr case=start
# [2,2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,1,0,1,99]\n
# @lcpr case=end

# @lcpr case=start
# [-2,-2,1,1,4,1,4,4,-4,-2]\n
# @lcpr case=end

# @lcpr case=start
# [-19,-46,-19,-46,-9,-9,-19,17,17,17,-13,-13,-9,-13,-46,-28]\n
# @lcpr case=end
#
