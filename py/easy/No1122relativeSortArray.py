class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res=[]
        nums = [0 for _ in range(max(arr1) + 1)]
        for k in arr1:
            nums[k] += 1
        for k in arr2:
            while(nums[k] > 0):
                res.append(k)
                nums[k] -= 1
        for k, v in enumerate(nums):
            while(v > 0):
                res.append(k)
                v -= 1
        return res

Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])