class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        h = {}

        for i in s:
            h[i] = h.get(i, 0) + 1

        for x in t:
            if x not in h:
                return False

            h[x] -= 1

            if h[x] < 0:
                return False

        return True
    