#
# @lc app=leetcode.cn id=349 lang=python3
# @lcpr version=30105
#
# [349] 两个数组的交集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n[2,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,5]\n[9,4,9,8,4]\n
# @lcpr case=end

#

