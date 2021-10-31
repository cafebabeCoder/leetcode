#
# @lc code=start
# Definition for singly-linked list.
# Definition for a binary tree node.
#[5,3,6,2,4,null,null,1]
#3
def gcd(a, b):
    a, b = (a, b) if a > b else (b, a)
    while b:
        a, b = b, a%b
    return a 


def lcm(a, b):
    return a * b // gcd(a, b)

res = gcd(15, 50)
print(res)

print(lcm(15, 50))