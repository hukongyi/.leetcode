#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30112
#
# [131] 分割回文串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                f[i][j] = (s[i] == s[j]) and f[i+1][j-1]

        ret = list()
        ans = list()
        def dfs(i):
            if i==n:
                ret.append(ans.copy())
                return
            for j in range(i,n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j+1)
                    ans.pop()

        dfs(0)
        return ret
            
# @lc code=end

#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#
