#!/usr/bin/env python
# coding: utf-8

# ### Regular Expression
#  - Pattern Matching
#  - Patterns(re) package
#  - Cap symbol is used to represnt the start of re
#  - Dollar symbol is used to represent the end of re
#  - [0-9]  --> Any digit Matching
#             -- Two digit number (^[0-9]{2}$)
#             -- Five digit number (^[0-9]{5}$)

# In[5]:


#fuction to test two digit number matching
import re
def twodigitnumber(n):
    pattern = '^[0-9]{2}$'
    n = str(n)
    if re.match(pattern,n):
        return True
    return False
print(twodigitnumber(76))
print(twodigitnumber(876))


# In[7]:


#function to define to test username having 8 characters
#upper case nd lower case
def testusername(n):
    pattern = '^[a-zA-Z]{8}$'
    if re.match(pattern,n):
        return True
    return False
print(testusername('Gitamhyd'))
print(testusername('Gitam876'))


# ### Regualar expressio to match the Indian Mobile Number
# - 10 Digits
# - (Firtst digit will be [6-9]) and remaining 9 digits will be [0-9]
# - Example (9876543201)
# - Re-^[6-9][0-9]{9}
# 

# In[17]:


# Function to validate the indian mobile number
def phonenumbervalidation(phone):
    patter = '^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    phone = str(phone)
    if re.match(patter,phone):
        return True
    return False
print(phonenumbervalidation(8008470879))
print(phonenumbervalidation(+918999765431))
    


# - Regular Expression to Validate the RollNumber
#    - Example : 1521A0501
#    - Example : 1521A0109
#    - Example : 1521A0499
# - Regular Expression to validate the password
#     - parameters : Len min of 6 characters and Max of 15 characters
#     - Accept Lower case, upper case, Digits spl char (@,#,!)

# In[23]:


def rollnumber(number):
    pattern = '^[1][5][2][1][A][0][0-9]{3}$'
    number = str(number)
    if re.match(pattern,number):
        return True
    return False
print(rollnumber('1521A0897'))


# In[32]:


def password(passw):
    pattern = '[A-za-z0-9@#!]{6,15}'
    passw = str(passw)
    if re.match(pattern,passw):
        return True
    return False
print(password('bunnuAX098@'))


# # Email Id validation using Regular Expression
# - Example :- Username@DomainName.extension
# - Username :- 
#    - Length will be [6-15]
#    - No specials characters apart from Underscore(_)
#    - Should no begin and end with Underscore(_)
#    - Characters set : All digits and lower case
# - DominName :-
#    - Length will be [3-18]
#    - No special characters
#    - Character set  : All digits are lower case 
#  - Extensions :-
#    - Length will be [2-4]
#    - No special characters
#    - Characters set : lower case characters

# In[1]:


import re
def mail(n):
    pattern = '^[A-za-z0-9.@]{8,30}$'
    if re.match(pattern,n):
        return True
    return False
print(mail('Anuraaglalaji14@gmail.com'))


# In[ ]:


# Step 1 : Make all the turtle package to be imported
import turtle
# Turtle method creates and returns a new object
a1= turtle.Turtle()
# forward() method moves 100 pixels
turtle.forward(250)
#we are done
turtle.done()


# In[ ]:


#Line draw in reverse direction
import turtle as tt
a1 = tt.Turtle()
tt.backward(100)
tt.done()


# In[ ]:


#Draw square
import turtle as tt
a1 = tt.Turtle()
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
tt.done()


# In[16]:


import re
def sites(n):
    pattern1 = '^[h][t][t][p][s][:][/][/][a-z]{1,30}[.][a-z]{1,30}[.][c][o][m][/][a-z]{1,30}[/][0-9]{1,30}$'
    pattern2 = '^[h][t][t][p][s][:][/][/][a-z]{1,30}[.][a-z]{1,30}[.][c][o][m][/][a-z/]{5,20}[0-9/]{1,10}[a-z#/]{1,50}'
    pattern3 = '^[h][t][t][p][s][:][/][/][w][w][w][.][a-z]{5,30}[.][c][o][m][/]'
    if re.match(pattern1,n):
        return True
    elif re.match(pattern2,n):
        return True 
    elif re.match(pattern3,n):
        return True
    return False
print(sites('https://mail.google.com/mail/u/0/#inbox/FMfcgxwChcrgrrzfVFwwTbKvSTFzdqSD'))
print(sites('https://www.regexpal.com/'))
print(sites('https://drive.google.com/drive/my-drive'))


# In[ ]:


# Star
import turtle as t
a1 = t.Turtle()
for i in range(40):
    a1.forward(50)
    a1.right(144)
t.done()


# In[ ]:


# Spiraling Star
import turtle as t
a1 = t.Turtle()
a1.pencolor('blue')
for i in range(40):
    a1.forward(i*10)
    a1.right(144)
t.done()


# In[ ]:


# Square Spiral help of Turtle
import turtle as t
a1= t.Turtle()
for i in range(250):
    a1.forward(i)
    a1.left(91)
t.done()


# In[ ]:


import turtule as t2
i1 = t2.turtle()
for i in range(30):
    i1.forward(30)
    i1.


# In[ ]:





# In[ ]:





# In[ ]:




