#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#

# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        lens = len(nums)
        res = 0
        for a in range(lens):
            for b in range(a+1, lens):
                # left = b+1
                left = b + 1
                right = lens-1
                while left<lens and right> b and left <= right: 
                    mid = int((right - left)/2 + left)
                    if nums[mid] > nums[a] + nums[b]:
                        right = mid-1
                    elif nums[mid] < nums[a] + nums[b]:
                        left = mid +1 
                    else:
                        right = mid -1
                if left >= lens or nums[a]+nums[b]<=nums[left]:
                    t = left-b-1
                # elif nums[a] + nums[b] < nums[left]:
                    # t = 0
                else:
                    t = left-b
                # print(a, b, left, t)
                res += t

        return res

# @lc code=end

