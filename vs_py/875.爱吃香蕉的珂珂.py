#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = -1
        for i  in piles:
            if m < i:
                m = i
    
        left = 1 
        right = m + 1
        while(left <= right):
            mid = int(left + (right - left) / 2)
            if self.hour_consum(piles, mid) < h:
                right = mid-1
            elif self.hour_consum(piles, mid) > h:
                left = mid + 1
            elif self.hour_consum(piles, mid) == h:
                right = mid-1


        return left
    
    def hour_consum(self, piles, speed):
        t = 0
        for p in piles:
            m = 0 if p % speed == 0 else 1 
            t += int(p / speed) + m 
        return t
        

# @lc code=end