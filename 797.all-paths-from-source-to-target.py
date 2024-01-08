#
# @lc app=leetcode.cn id=797 lang=python3
# @lcpr version=30113
#
# [797] 所有可能的路径
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = list()
        path = [0]

        def dfs():
            if path[-1] == len(graph) - 1:
                result.append(path[:])
                return
            for i in graph[path[-1]]:
                path.append(i)
                dfs()
                path.pop()

        dfs()
        return result


# @lc code=end


#
# @lcpr case=start
# [[1,2],[3],[3],[]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,3,1],[3,2,4],[3],[4],[]]\n
# @lcpr case=end

#
