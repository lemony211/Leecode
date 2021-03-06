# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

# 例如，给出 n = 3，生成结果为：

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def process(self,s,lis,left,right):
        if left>right:
            return 
        if left>0:
            self.process(s+'(',lis,left-1,right)
        if right>0:
            self.process(s+')',lis,left,right-1)
        if left==0 and right==0:
            lis.append(s)
            return 
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left = n
        right = n
        lis = []
        self.process('',lis,left,right)
        return lis
    
