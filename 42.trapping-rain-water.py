#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30113
#
# [42] 接雨水
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        highlist = [(0, height[0])]
        for i in range(1, len(height)):
            if height[i] >= highlist[-1][1]:
                pre_height = 0
                while len(highlist) > 0 and height[i] >= highlist[-1][1]:
                    tmp_i, tmp_height = highlist.pop()
                    ans += (tmp_height - pre_height) * (i - tmp_i - 1)
                    # print("==", i, ans)
                    # print(tmp_height, pre_height)
                    pre_height = tmp_height
                if len(highlist) != 0:
                    tmp_i, _ = highlist[-1]
                    ans += (height[i] - pre_height) * (i - tmp_i - 1)
            highlist.append((i, height[i]))
        return ans


# @lc code=end


#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#
