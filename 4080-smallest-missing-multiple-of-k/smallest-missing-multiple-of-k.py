class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        multiple =[]
        for i in nums:
            if i % k == 0:
                multiple.append(i)
        candidate = k
        while candidate in multiple:
            candidate += k
        return candidate
                 




