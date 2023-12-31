#
# @lc app=leetcode.cn id=77 lang=python3
# @lcpr version=30112
#
# [77] 组合
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        self.backtracking(n,k,1,[],result)
        return result
    
    def backtracking(self,n,k,index,path,result):
        if len(path)==k:
            result.append(path[:])
            return
        for i in range(index,n-(k-len(path))+2):
            path.append(i)
            self.backtracking(n,k,i+1,path,result)
            path.pop()

# @lc code=end



#
# @lcpr case=start
# 4\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

