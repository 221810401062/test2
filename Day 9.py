#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Day objectives

1.python data structures
   . lists
   . Tuples
   . Dictionaries
 . basic program sets on data strutcures
 . advanced problem set 
 . contact application(Dicionary object)

 Data structures:
        
        . to store,search and sort the data


# In[7]:


lst = [1,2,3,4,5,6]
print(lst)
print(lst[1])
print(lst[0])
print(lst[-1])
print(lst[-2])
print(lst[1:])
print(lst[1:4])
print(lst[0:])
print(lst[-1:])


# In[8]:


li = ["Gitam","Python",1989,2009]
print(li)
li[2] = [1999]
print(li)


# In[9]:


li = ["Gitam","Python",1989,2009]
print(li)
del li[2]
print(li)


# In[16]:


lst = [1,2,3,4,5,6,7,8,9]
print(len(lst))
print(lst * 2)
print(3 in lst)
for x in range(len(lst)):
    print(lst[x],end=" ")    


# In[17]:


print(lst)


# In[34]:


lst
print(min(lst))
print(max(lst))
print(sum(lst))
print(int(sum(lst)/len(lst)))
print(sum(lst[::4]))
print(int(sum(lst[1::2])/len(lst[1::2])))


# In[43]:


lst
lst.append(24)
lst
lst.insert(3,55)
lst
lst.count(3)
lst.index(8)
lst.sort()
lst
lst.pop()
lst
lst.pop(1)


# In[49]:


def secondlarge(ls):
    ls.sort()
    return ls[-2]
def genericlarge(ls,n):
    ls.sort()
    return ls[-n]
ls = [2,10,7,3,8,67]
genericlarge(ls,4)


# In[52]:


def linearsearch(li,taritem):
    for x in range(len(li)):
        if li[x] == taritem:
            print(x,end=" ")
    return
li = [2,7,4,0,5,9,7,6,7,1]
linearsearch(li,5)


# In[53]:


def LinearSearch3(li,tarItem):
    # Implemen tthe logic
    for x in range(len(li)):
        if li[x] == tarItem:
            j = 0
            while j != x+1:
                print("!",end="")
                j = j + 1
            print(end=" ")
    return
li = [1,5,9,6,5,15,1,2,5]
LinearSearch3(li,5) 


# In[55]:


def linearsearch2(li):
    sum = 0
    for x in range(len(li)):
        if li[x] % 3 == 0 and li[x] % 5 == 0:
            sum += li[x]
    return sum
li = [12,60,15,8,10,9]
linearsearch2(li)


# In[56]:


lst=["gitam","school"]
print(lst)


# In[58]:


def linearsearch1(li):
    for x in range(len(li)):
        if x == 0 and x == len(li) - 1:
            print(li[x],end=" ")
        elif li[x-1] % 2 == 0 and li[x+1] % 2 == 0:
            print(li[x],end=" ")
    return
li = [1,2,3,4,5,6,7]
linearsearch1(li)


# In[61]:


def numberlistconversion(n):
    li = []
    while n != 0:
        r = n % 10
        li.append(r)
        n = n // 10
    li.reverse()
    return li
numberlistconversion(56785)


# In[62]:


def countCharOccurances(s,c):
    cnt=0
    for ch in s:
        if ch == c:
            cnt+=1
    return cnt
countCharOccurances("Python Programming",'m')


# In[63]:


def strintToListConversion(s):
    li=s.split()
    numberslist =[]
    for i in li:
        numberslist.append(int(i))
    return numberslist
s="1 2 3 4 5 6"
strintToListConversion(s) #[1,2,3,4,5,6]


# In[64]:


def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li
li= [19,1,25,6,18,3]
bubbleSort(li)


# In[ ]:




