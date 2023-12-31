#
# @lc app=leetcode.cn id=376 lang=python3
# @lcpr version=30112
#
# [376] 摆动序列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        method 1
        flag = 1
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] > nums[i - 1] and (flag or not up):
                flag=0
                up = True
                ans += 1
            if nums[i] < nums[i - 1] and (flag or up):
                flag=0
                up = False
                ans += 1
        return ans



# @lc code=end


#
# @lcpr case=start
# [1,7,4,9,2,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,17,5,10,13,15,10,5,16,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7,8,9]\n
# @lcpr case=end

#
