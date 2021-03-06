# 954. 二倍数对数组 我的提交返回竞赛
# 用户通过次数 92
# 用户尝试次数 158
# 通过次数 97
# 提交次数 651
# 题目难度 Medium
# 给定一个长度为偶数的整数数组 A，只有对 A 进行重组后可以满足 “对于每个 0 <= i < len(A) / 2，都有 A[2 * i + 1] = 2 * A[2 * i]” 时，返回 true；否则，返回 false。

 

# 示例 1：

# 输入：[3,1,3,6]
# 输出：false
# 示例 2：

# 输入：[2,1,2,6]
# 输出：false
# 示例 3：

# 输入：[4,-2,2,-4]
# 输出：true
# 解释：我们可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
# 示例 4：

# 输入：[1,2,4,16,8,4]
# 输出：false
 

# 提示：

# 0 <= A.length <= 30000
# A.length 为偶数
# -100000 <= A[i] <= 100000

class Solution:
    def canReorderDoubled(self,A):
        """
        :type A: List[int]
        :rtype: bool
        """
        dic = {}
        for i in A:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        while len(dic.keys()) != 0:
            i = list(dic.keys())[0]
            try:
                if dic[i] == dic[2 * i if 2 * i in dic else i / 2]:
                    if dic[i] > 1:
                        dic[i] -= 1
                        dic[2 * i if 2 * i in dic else i / 2] -= 1
                        if dic[i] == 0:
                            dic.pop(i)
                    else:
                        dic.pop(i)
                        dic.pop(2 * i if 2 * i in dic else i / 2)
                else:
                    return False
            except:
                break
        if len(dic) == 0:
            return True
        else:
            return False
