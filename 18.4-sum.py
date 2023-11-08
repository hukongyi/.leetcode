#
# @lc app=leetcode.cn id=18 lang=python3
# @lcpr version=30105
#
# [18] 四数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] > target and nums[i] > 0 and target > 0:  # 剪枝（可省）
                break
            if i > 0 and nums[i] == nums[i-1]:  # 去重
                continue
            for j in range(i+1, n):
                if nums[i] + nums[j] > target and target > 0:  # 剪枝（可省）
                    break
                if j > i+1 and nums[j] == nums[j-1]:  # 去重
                    continue
                left, right = j+1, n-1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        result.append(
                            [nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
return result
# @lc code=end


#
# @lcpr case=start
# [1,0,-1,0,-2,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n8\n
# @lcpr case=end

#
