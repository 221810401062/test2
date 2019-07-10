#!/usr/bin/env python
# coding: utf-8

# In[1]:


d1 = {"Gitam":"Mail","gitam@gamil.com":"Attendence"}
print(d1)


# In[10]:


d2 = {"mail":"bunnurockzz@gmail.com","name":"syama","Roll number":"221810401062"} 
print(d2)


# In[27]:


d2["mail"] = "python@gmail.com"


# In[26]:


d2["mail"]


# In[28]:


del d1['mail']


# In[29]:


d1


# In[31]:


d1.keys()


# In[32]:


d1.values()


# In[34]:


d1.items()


# In[37]:


t1 = (7,6,8,9)
t1
type(t1)


# In[39]:


contacts = {}
def addcontacts(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("contacts added")
    else:
        print("contact already exist")
    return
addcontacts('gitam','0987654321')
addcontacts('gitam','1234567890')
addcontacts('python','9078563412')


# In[40]:


def searchcontacts(name):
    if name in contacts:
        print(name, ":" , contacts[name])
    else:
        print("%s does not exits" % name)
    return
searchcontacts('gitam')
searchcontacts('anil')


# In[44]:


def importcontact(newcontacts):
    contacts.update(newcontacts)
    print(len(newcontacts.keys()),"contacts added successfully")
    return
newcontacts = {'dinesh':7890654321,'sdfg':8970453612}
importcontact(newcontacts)


# In[46]:


contacts


# In[47]:


def deletecontact(name):
    if name in contacts:
        del contacts[name]
        print(name,"deleted successfully")
    else:
        print(name,"not exist")
    return
deletecontact('gitam')


# In[48]:


contacts


# In[49]:


def deletecontact(name,phone):
    if name in contacts:
        contacts[name] = phone
        print(name,"updated successfully")
    else:
        print(name,"not exist")
    return
deletecontact('gitam',9087654321)
deletecontact('ajay',6789054321)


# In[52]:


s1 = "gitam"
print(s1.upper())
print(s1.lower())


# In[53]:


s2 = 'gitam'
print(s2.islower())
print(s2.isupper())


# In[54]:


li = ["python","Programming"]
print("%s %s "% (li[0],li[1]))

print("{0} {1}".format(li[0] , li[1]))


# In[55]:


li1 = [1,2,3,4]
print("%d %d %d %d " % (li1[0],li1[1],li1[2],li1[3]))

print("{0} {1} {2} {3}".format(li1[0],li1[1],li1[2],li1[3]))


# In[56]:


s3 = "Gitam"
s4 = "gitam"
print(s3.istitle())
print(s4.istitle())


# In[58]:


s2 = "error 404"
s3 = "done"
print(s2.isalpha())
print(s3.isalpha())


# In[59]:


s1 = "@123"
s2 = "80084"
print(s1.isnumeric())
print(s2.isnumeric())


# In[60]:


s1 = "---"
s2 = "   "
print(s1.isspace())
print(s2.isspace())


# In[61]:


s1 = 'gitam'
print(' '.join(s1))


# In[62]:


s2 = "python programming easy to learn"
print(" ".join(s2))


# In[1]:


s2 = "Python Programming easy to lean"
print(s2.split())


# In[2]:


s2 = "Python Programming easy to lean"
li = s2.split()
print(li)
print(len(li))


# In[3]:


s2 = "Python Programming easy to lean"
li = list(s2)
print(li)


# In[1]:


s2 = "Python Programming Easy to learn"
print(s2.split())


# In[2]:


s2 = "Python Programming Easy to learn"
print(s2.split('a'))


# In[3]:


s2 = "Python Programming Easy to learn"
li=s2.split()   #split the string -- List object
print(li)
print(len(li))


# In[4]:


s2 = "Python Programming Easy to learn"
li=list(s2)
print(li)


# In[5]:


import math
math.floor(123.45)


# In[6]:


items=[1,5]
print("s",items)


# In[7]:


def randomNNumbers(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub),end=" ")
    return
randomNNumbers(10,0,100)


# In[ ]:




