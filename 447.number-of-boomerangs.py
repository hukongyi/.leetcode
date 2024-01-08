#
# @lc app=leetcode.cn id=447 lang=python3
# @lcpr version=30113
#
# [447] 回旋镖的数量
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distence(i, j):
            return (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2

        ans = 0
        distenceSet = [dict() for _ in points]
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                dist = distence(points[i], points[j])
                if dist in distenceSet[i]:
                    ans += distenceSet[i][dist]
                if dist in distenceSet[j]:
                    ans += distenceSet[j][dist]
                distenceSet[i][dist] = distenceSet[i].get(dist, 0) + 1
                distenceSet[j][dist] = distenceSet[j].get(dist, 0) + 1
        return ans*2


# @lc code=end


#
# @lcpr case=start
# [[0,0],[1,0],[2,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,2],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1]]\n
# @lcpr case=end

#
