#
# @lc app=leetcode.cn id=406 lang=python3
# @lcpr version=30112
#
# [406] 根据身高重建队列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        que = list()
        for i in people:
            que.insert(i[1], i)
        return que


# @lc code=end


#
# @lcpr case=start
# [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]\n
# @lcpr case=end

#
