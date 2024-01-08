#
# @lc app=leetcode.cn id=739 lang=python3
# @lcpr version=30112
#
# [739] 每日温度
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        hightemperatures = [(len(temperatures) - 1, temperatures[-1])]
        for i in range(len(temperatures) - 2, -1, -1):
            if temperatures[i] < hightemperatures[-1][1]:
                ans[i] = 1
            else:
                while (
                    len(hightemperatures) > 0
                    and temperatures[i] >= hightemperatures[-1][1]
                ):
                    hightemperatures.pop()
                if len(hightemperatures) == 0:
                    ans[i] = 0
                else:
                    ans[i] = hightemperatures[-1][0] - i
            hightemperatures.append((i, temperatures[i]))
        return ans


# @lc code=end


#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#
