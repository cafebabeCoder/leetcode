#
# @lc app=leetcode.cn id=659 lang=python3
#
# [659] 分割数组为连续子序列
#

# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = {}
        need = {}
        for num in nums:
            freq[num]=freq.get(num, 0)+1

        for i in range(len(nums)):
            num = nums[i]
            # 
            if freq[num] == 0:
                continue

            if need.get(num, 0) > 0:
                freq[num] -= 1
                need[num] = need.get(num, 0)-1  # 下一个不能接同一个数字了
                need[num+1] = need.get(num + 1, 0) + 1
            elif freq.get(num, 0)>0 and freq.get(num+1, 0)>0 and freq.get(num+2, 0)>0:
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                need[num+3] = need.get(num+3, 0) + 1
            else:
                return False
        
        return True

# @lc code=end

