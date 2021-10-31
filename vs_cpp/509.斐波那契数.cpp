/*
 * @lc app=leetcode.cn id=509 lang=cpp
 *
 */

#include <iostream>
using namespace std;
//@lc code=star

class Solution
{
public:
    int fib(int n)
    {
        if (n < 1)
            return 0;
        else if(n==1 || n==2)
            return 1;
        else{
            int pre=1, cur = 1;
            for(int i=3; i<=n; i++){
                int res = pre + cur;
                pre = cur;
                cur = res;
            }
            return cur;
        }
    }
};


// @lc code=end
int main()
{
    Solution s;
    cout << s.fib(30);
    return 0;
}