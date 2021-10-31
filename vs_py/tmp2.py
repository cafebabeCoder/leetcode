class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        sor = nums[0]
        while left < right:
            while left <right and nums[right]%2==0:
                right -=1
            nums[left] = nums[right]
            while left<right and nums[left]%2!=0:
                left +=1
            nums[right] = nums[left]
            print(nums)
        nums[left] = sor
        return nums

s = Solution()
res = s.exchange([1,2,3,4])	 
print(res)