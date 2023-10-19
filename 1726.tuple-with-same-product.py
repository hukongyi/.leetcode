#
# @lc app=leetcode.cn id=1726 lang=python3
# @lcpr version=30102
#
# [1726] 同积元组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = dict()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                times = nums[i]*nums[j]
                count[times] = count.get(times, 0)+1
        ans = 0
        for i in count.keys():
            ans += (count[i]*count[i]-count[i])*4
        return ans
# @lc code=end


#
# @lcpr case=start
# [2,3,4,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,5,10]\n
# @lcpr case=end

#
