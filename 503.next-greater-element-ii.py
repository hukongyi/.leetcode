#
# @lc app=leetcode.cn id=503 lang=python3
# @lcpr version=30113
#
# [503] 下一个更大元素 II
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        maxi = 0
        maxnums = float("-inf")
        for i in range(len(nums)):
            if nums[i] > maxnums:
                maxnums = nums[i]
                maxi = i
        largelist = [maxnums]
        ans = [0] * len(nums)
        ans[maxi] = -1
        i = (maxi - 1) % len(nums)
        while i != maxi:
            if nums[i] < largelist[-1]:
                ans[i] = largelist[-1]
                largelist.append(nums[i])
            else:
                while len(largelist) != 0 and nums[i] >= largelist[-1]:
                    largelist.pop()
                if len(largelist) == 0:
                    ans[i] = -1
                else:
                    ans[i] = largelist[-1]
                largelist.append(nums[i])
            i = (i - 1) % len(nums)
        return ans


# @lc code=end


#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1,1]\n
# @lcpr case=end

#
