#
# @lc app=leetcode.cn id=496 lang=python3
# @lcpr version=30112
#
# [496] 下一个更大元素 I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)
        return [res[num] for num in nums1]

# @lc code=end



#
# @lcpr case=start
# [4,1,2]\n[1,3,4,2].\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n[1,2,3,4].\n
# @lcpr case=end

#

