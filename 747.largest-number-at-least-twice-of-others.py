#
# @lc app=leetcode.cn id=747 lang=python3
# @lcpr version=30102
#
# [747] 至少是其他数字两倍的最大数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1, max2 = 0, 0
        ans = 0
        for i, num in enumerate(nums):
            if num >= max1:
                max1, max2 = num, max1
                ans = i
            elif num > max2:
                max2 = num
        return ans if max1>=max2*2 else -1


# @lc code=end


#
# @lcpr case=start
# [3,6,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

#
