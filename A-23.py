#!/usr/bin/env python
# coding: utf-8

# In[1]:


def isPalindrome(n):
    rev = 0
    buffer = n
    while n!= 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    if rev == buffer:
        return True
    else:
        return False
    return
def countPalindrome(lb,ub):
    cnt = 0
    while lb != ub:
        # Implement
        if isPalindrome(lb) == True:
            cnt = cnt + 1
        lb = lb + 1
    return cnt
countPalindrome(1,10)

