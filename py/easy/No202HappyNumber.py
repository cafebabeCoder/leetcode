#!/usr/bin/env python3
import math

class Solution:
	def isHappy(self, n: int) -> bool:
		va = {}
		while n!=1:
			st = str(n)
			m = int(math.fsum([math.pow(int(i), 2) for i in st]))
			print(m)
			if m == 1 or va.get(m) is True:
				n = m
				break
			n = m
			va[m] = True

		if n == 1:
			return True
		else:
			return False


st="sde"
print(Solution().isHappy(23))