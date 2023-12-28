#
# @lc app=leetcode.cn id=2660 lang=python3
# @lcpr version=30112
#
# [2660] 保龄球游戏的获胜者
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def getscore(player):
            flag = 1
            count = 0
            score = 0
            for s in player:
                score += s*flag
                if flag == 2:
                    count -= 1
                    if count == 0:
                        flag = 1
                if s == 10:
                    flag = 2
                    count = 2
            return score
        score1 = getscore(player1)
        score2 = getscore(player2)
        if score1 > score2:
            return 1
        elif score1 < score2:
            return 2
        return 0
# @lc code=end


#
# @lcpr case=start
# [4,10,7,9]\n[6,5,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,5,7,6]\n[8,10,10,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3]\n[4,1]\n
# @lcpr case=end

#
