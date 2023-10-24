#
# @lc app=leetcode.cn id=904 lang=python3
# @lcpr version=30102
#
# [904] 水果成篮
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        maxfruit = 0
        nowfruit = 0
        fruit = dict()
        kind = 0
        while(r < len(fruits)):
            if fruit.get(fruits[r], 0) != 0:
                nowfruit += 1
                fruit[fruits[r]] += 1
                r += 1
                maxfruit = max(maxfruit, nowfruit)
            elif kind < 2:
                nowfruit += 1
                kind += 1
                fruit[fruits[r]] = 1
                r += 1
                maxfruit = max(maxfruit, nowfruit)
            else:
                while(kind >= 2):
                    fruit[fruits[l]] -= 1
                    if fruit[fruits[l]] == 0:
                        kind -= 1
                    l += 1
                    nowfruit -= 1
                nowfruit += 1
                kind += 1
                fruit[fruits[r]] = 1
                r += 1

        return max(maxfruit, nowfruit)

# @lc code=end

#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,1,2,1,1,2,3,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,1,4]\n
# @lcpr case=end

#
