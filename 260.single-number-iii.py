#
# @lc app=leetcode.cn id=260 lang=python3
# @lcpr version=30102
#
# [260] 只出现一次的数字 III
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:

    def getxor(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans

    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = self.getxor(nums)
        for i in range(32):
            if (ans >> i) & 1 == 1:
                break
        list1 = [num for num in nums if (num>>i)&1==1]
        list2 = [num for num in nums if (num>>i)&1==0]
        return [self.getxor(list1),self.getxor(list2)]
        
# @lc code=end



#
# @lcpr case=start
# [1,2,1,3,2,5]\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

#

