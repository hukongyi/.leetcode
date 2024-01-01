#
# @lc app=leetcode.cn id=860 lang=python3
# @lcpr version=30112
#
# [860] 柠檬水找零
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = {5: 0, 10: 0}
        for i in range(len(bills)):
            if bills[i] == 5:
                count[5] += 1
            elif bills[i] == 10:
                count[10] += 1
                count[5] -= 1
            else:
                if count[10] > 0:
                    count[10] -= 1
                    count[5] -= 1
                else:
                    count[5] -= 3
            if count[10] < 0 or count[5] < 0:
                return False
        return True


# @lc code=end


#
# @lcpr case=start
# [5,5,5,10,20]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,10,10,20]\n
# @lcpr case=end

#
