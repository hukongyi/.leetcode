#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=21917
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()
        print(nums)
        for i in range(len(nums)):
           if nums[i] in a.keys():
               return [a[nums[i]],i]
           a[target-nums[i]] = i
        return []
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

