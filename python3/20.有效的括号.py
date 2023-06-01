#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            if char in brackets.values():
                if len(stack) == 0 or brackets[stack.pop()] != char:
                    return False

        return len(stack) == 0
# @lc code=end
