#
# @lc app=leetcode.cn id=718 lang=python3
# @lcpr version=30112
#
# [718] 最长重复子数组
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * len(nums1) for _ in nums2]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if i > 0 and j > 0:
                        dp[j][i] = dp[j - 1][i - 1] + 1
                    else:
                        dp[j][i] = 1
        return max(map(max, dp))


# @lc code=end


#
# @lcpr case=start
# [1,2,3,2,1]\n[3,2,1,4,7]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,0,0]\n[0,0,0,0,0]\n
# @lcpr case=end

#
