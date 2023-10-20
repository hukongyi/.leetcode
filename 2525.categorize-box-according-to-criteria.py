#
# @lc app=leetcode.cn id=2525 lang=python3
# @lcpr version=30102
#
# [2525] 根据规则将箱子分类
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
def ifBulky(length, width, height):
    return max(length, width, height) >= 1e4 or length*width*height >= 1e9


def ifHeavy(mass):
    return mass >= 100


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        Bulky = ifBulky(length, width, height)
        Heavy = ifHeavy(mass)
        ans = ["Neither", "Bulky", "Heavy", "Both"]
        return ans[Bulky+(Heavy << 1)]

# @lc code=end

#
# @lcpr case=start
# 1000\n35\n700\n300\n
# @lcpr case=end

# @lcpr case=start
# 200\n50\n800\n50\n
# @lcpr case=end


# @lcpr case=start
# 2909\n3968\n3272\n727\n
# @lcpr case=end

#
