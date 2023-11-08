#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30105
#
# [15] 三数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while(l < r):
                if nums[i]+nums[l]+nums[r] > 0:
                    r -= 1
                elif nums[i]+nums[l]+nums[r] < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while(r > l and nums[r] == nums[r+1]):
                        r -= 1
                    while(l < r and nums[l] == nums[l-1]):
                        l += 1
        return ans


# @lc code=end


#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [-2,0,0,2,2]\n
# @lcpr case=end

#
