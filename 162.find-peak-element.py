#
# @lc app=leetcode.cn id=162 lang=python3
# @lcpr version=30110
#
# [162] 寻找峰值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def geti(i):
            if i == -1 or i == len(nums):
                return float('-inf')
            return nums[i]
        l = 0
        r = len(nums)-1
        while(l <= r):
            mid = (l+r)//2
            if geti(mid) > geti(mid-1) and geti(mid) > geti(mid+1):
                return mid
            elif geti(mid) > geti(mid-1):
                l = mid+1
            else:
                r = mid-1
        return l

# @lc code=end


#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,3,5,6,4]\n
# @lcpr case=end

#
