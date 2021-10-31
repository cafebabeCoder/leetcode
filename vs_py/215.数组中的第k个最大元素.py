# @lc app=leetcode.cn id=215 lang=python3
# [215] 数组中的第K个最大元素
# hint:

# @lc code=start

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = self.quickSort(nums, 0, len(nums)-1)
        return res[-k]

    def quickSort(self, nums, left, right):
        # 一定不要忘了外层判断
        if left < right:
            i = left
            j = right
            tmp = nums[left]
            while i < j:
                # 从右边往左找到小于tmp的数，赋值给 左边 移动指针
                while i<j and tmp <= nums[j]:
                    j -= 1
                nums[i] = nums[j]

                # 从左往右找到大于tmp的数，赋值给右边移动指针.
                while i<j and nums[i] <= tmp:
                    i += 1 
                nums[j] = nums[i]
            
            # i=j 退出， 然后这个位置就是哨兵
            nums[i] = tmp
            # 分治， 左闭右闭 
            self.quickSort(nums, left, i - 1)
            self.quickSort(nums, i+1, right)
        return nums
        
# @lc code=end

