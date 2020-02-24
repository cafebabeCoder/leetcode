#!/usr/bin/env python3
from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		profit = 0
		for i in range(1, len(prices)):
			if prices[i]-prices[i-1] > 0:
					profit = profit+prices[i]-prices[i-1]
		return profit

print(Solution().maxProfit([7,1,1,3,6,4]))
