#!/usr/bin/env python
# coding: utf-8

# In[1]:


def printLarge(n):
    large = 0
    while n != 0:
        r = n % 10
        if large < r:
            large = r
        n = n // 10
    return large
printLarge(17856)

