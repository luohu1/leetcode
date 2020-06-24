#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arr = dict.fromkeys(set(s), 0)
        for i in range(len(s)):
            arr[s[i]] += 1
            if t[i] not in arr:
                return False
            arr[t[i]] -= 1

        for v in arr.values():
            if v != 0:
                return False

        return True


# @lc code=end
