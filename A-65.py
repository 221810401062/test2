#!/usr/bin/env python
# coding: utf-8

# In[2]:


def createfile(filename):
    f = open(filename,'w')
    for i in range(10):
        f.write(" this is %d line\n " %i)
    print("file is created and data has be written")
    return
createfile("file3.txt")
def wordcount(filename,word):
    with open(filename,'r') as f:
        if  f.mode == 'r':
            x = f.read()
            li = x.split() # it's splits the string with 
    cnt = li.count(word)
    return cnt
filename = input('enter the file name:- ')
word = input('enter the word ')
wordcount(filename,word)


# In[ ]:




