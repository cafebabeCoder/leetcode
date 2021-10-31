#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
#

# @lc code=start
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        self.res = []
        self.sort(arr, len(arr))
        return self.res
    
    def sort(self, arr, n):
        if n == 1:
            return
        # 找到最大的那个
        max_v = 0 
        max_idx = 0 
        for i in range(0, n, 1): 
            if max_v  < arr[i]:
                max_v = arr[i] 
                max_idx = i

        # 翻转前面 
        self.reverse(arr, 0, max_idx)
        self.res.append(max_idx+1)  #注意append + 1

        #翻转后面
        self.reverse(arr, 0, n-1)
        self.res.append(n)

        self.sort(arr, n-1)

    def reverse(self, arr, i, j):
        while i<j:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
            i += 1
            j -= 1


# @lc code=end

