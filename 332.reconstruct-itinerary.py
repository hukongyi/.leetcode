#
# @lc app=leetcode.cn id=332 lang=python3
# @lcpr version=30112
#
# [332] 重新安排行程
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         tickets.sort()
#         def getticket(tickets, begin, used):
#             index = list()
#             ticketslist = list()
#             for i, ticket in enumerate(tickets):
#                 if i not in used and ticket[0] == begin:
#                     index.append(i)
#                     ticketslist.append(ticket)
#             # if len(index) > 0:
#                 # ticketslist, index = zip(*sorted(zip(ticketslist, index)))
#             return ticketslist, index

#         ans = list(["JFK"])
#         used = set()

#         def dfs():
#             if len(ans) == len(tickets)+1:
#                 return ans
#             begin = ans[-1]
#             ticketslist, index = getticket(tickets, begin, used)
#             if len(index) == 0:
#                 return
#             for ticket, i in zip(ticketslist, index):
#                 used.add(i)
#                 ans.append(ticket[1])
#                 rst = dfs()
#                 if rst is not None:
#                     return rst
#                 ans.pop()
#                 used.remove(i)
#         return dfs()
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = defaultdict(list)
        # 构建航班信息
        for start, end in tickets:
            flights[start].append(end)
        # 使用堆对目的地进行排序
        for start in flights:
            heapq.heapify(flights[start])
        
        def dfs(start):
            # 当存在从start出发的航班时，选择字典序最小的目的地
            while flights[start]:
                dfs(heapq.heappop(flights[start]))
            # 当不存在从start出发的航班时，把start加入到路径中
            path.append(start)
        
        path = []
        dfs('JFK')
        # 由于dfs是在没有航班可选时才把机场加入到路径中，所以最后要反转路径
        return path[::-1]

# @lc code=end

#
# @lcpr case=start
# [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]\n
# @lcpr case=end

# @lcpr case=start
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]\n
# @lcpr case=end

#
