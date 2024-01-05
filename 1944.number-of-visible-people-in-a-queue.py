#
# @lc app=leetcode.cn id=1944 lang=python3
# @lcpr version=30112
#
# [1944] 队列中可以看到的人数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        tmp = [heights[-1]]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] < tmp[-1]:
                ans[i] = 1
                tmp.append(heights[i])
            else:
                count = 1
                while len(tmp) > 0 and tmp[-1] < heights[i]:
                    tmp.pop()
                    count += 1
                if len(tmp) == 0:
                    count -= 1
                tmp.append(heights[i])
                ans[i] = count
        return ans


# @lc code=end


#
# @lcpr case=start
# [10,6,8,5,11,9]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,2,3,10]\n
# @lcpr case=end

#
