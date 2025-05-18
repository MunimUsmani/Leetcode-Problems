class Solution:
    def firstUniqChar(self, s: str) -> int:
        # dic = dict()
        # for i in s:
        #     if dic.get(i):
        #         dic[i] = dic.get(i) + 1
        #     else:
        #         dic[i] = dic.get(i, 1)
        dic = Counter(s) # this func does the same as in upper code
        # {'l': 2, 'o': 2, 'v': 1, 'e': 4, 't': 1, 'c': 1, 'd': 1}

        for i in range(len(s)):
            if dic.get(s[i]) == 1:
                return i
        return -1
