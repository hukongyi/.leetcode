#
# @lc app=leetcode.cn id=674 lang=python3
# @lcpr version=30112
#
# [674] 最长连续递增序列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxlen = 0
        i = 0
        count = 1
        while i < len(nums) - 1:
            if nums[i + 1] > nums[i]:
                count += 1
            else:
                maxlen = max(maxlen, count)
                count = 1
            i += 1
        return max(maxlen, count)


# @lc code=end


#
# @lcpr case=start
# [1,3,5,4,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n
# @lcpr case=end

#
