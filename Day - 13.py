#!/usr/bin/env python
# coding: utf-8

# ## Transforming Code into Idiomatic Python

# In[1]:


# Looping over a range of numbers - Traditional Approch
for i in [0,1,2,3,4,5]:
    print(i**2,end=" ")


# In[2]:


# Idiomatic Programming
for i in range(6):
    print(i**2,end=" ")


# ## Looping over a collection

# In[4]:


colors = ['red','green','yellow','purple']
for i in range(len(colors)):
    print(colors[i],end=" ")


# In[5]:


for colors in colors:
    print(colors,end=" ")


# ## Looping backwards

# In[6]:


colors = ['red','green','yellow','purple']
for i in range(len(colors)-1,-1,-1):
    print(colors[i],end=" ")


# In[7]:


for color in reversed(colors):
    print(color,end=" ")


# In[8]:


for color in sorted(colors,reverse=True):
    print(color,end=" ")


# ### 
#  - if x <=y and y <=z:
#  - if x<=y<=z:
#  - if x == True:
#  - if x:

# ## Pandas

# In[1]:


import pandas as pd


# In[2]:


dt = {'Id' :[11,12,13,14,15],
     'first_name':['A','B','C','D','E'],
     'company':['aa','bb','cc','dd','ee'],
     'address':['Hyd','Hyd','Hyd','Hyd','Hyd']}
mydt = pd.DataFrame(dt)


# In[3]:


print(mydt)


# In[4]:


import os


# In[ ]:


os.chdir("D:\\MyData\\")


# In[ ]:


mydt.to_csv('WorkingFile.csv',index = False)


# In[ ]:









# In[ ]:





# In[ ]:




