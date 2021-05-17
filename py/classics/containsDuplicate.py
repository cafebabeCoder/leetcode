class Solution(object):
    def containsDuplicate_set(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) - len(nums) < 0:
            return True
        else:
            return False

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.quicklySort(nums, 0, len(nums) - 1)
        for k in range(1, len(nums), 1):
            if nums[k-1] == nums[k]:
                return True
        return False


    def quicklySort(self, nums, low, high):
        if low < high:
            tmp = nums[low]
            i = low
            j = high
            while i < j:
                while i < j and tmp <= nums[j]:
                    j -= 1
                nums[i] = nums[j]
                while i < j and tmp >= nums[i]:
                    i += 1
                nums[j] = nums[i]
            nums[i] = tmp
            print(nums)
            self.quicklySort(nums, low, i - 1)
            self.quicklySort(nums, i + 1, high)

nums = [2,4,3,1,6,9,4]
# Solution().quicklySort(nums, 0, 6)
print(nums)
print(Solution().containsDuplicate(nums))
print(Solution().containsDuplicate_set(nums))