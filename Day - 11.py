#!/usr/bin/env python
# coding: utf-8

# standard libraries
# - File I/O
# - Regular Expression
# - Datetime
# - Math (numerical and Mathematical)

# ### File Handling in Python
# - File:- Document contating infeomation resided on the  permenent storage
# - different types of files:- txt,doc,pdf,csv and etc...
# - Input -- Keyboard
# - Output -- File
# ### Modes of the file I/O
# - 'w' -- This mode is used to file writing
#       -- If the file is not present first it creates the file and write so me data to it

# In[4]:


#fuction to create a file and write to the file
def createfile(filename):
    f = open(filename,'w')
    for i in range(10):
        f.write('this is %d line' % i)
    print("file is created and data has written")
    return
createfile('file1.txt')


# In[5]:


ls


# In[8]:


cat file1.txt


# In[13]:


def createfile(filename):
    f = open(filename,'w')
    f.write('testing...\n')
    print("file is created and data has written")
    return
createfile('file1.txt')


# In[11]:


ls


# In[18]:


def appendData(filename):
    f = open(filename,'a')
    for i in range(10):
        f.write("This is %d Line\n" % i)
    print("File is created and data is succesfully craeted")
    return
appendData('file2.txt')


# In[20]:


def appendData(filename):
    f = open(filename,'a')
    f.write("new line 1 \n")
    f.write("new line 2 \n")
    print("File created and successfully data written")
    return
appendData('file2.txt')
    


# In[21]:


ls


# In[22]:


def fileoperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode == 'r':
            data = f.read()
            print(data)
        elif f.mode == 'a':
            f.write('data to the file')
            print('the data successfully written')
    f.close()
    return
filename = input('enter the file name')
mode = input('enter the mode of the file')
fileoperations(filename,mode)


# In[23]:


def readfiledata(filename):
    f = open(filename,'r')
    if f.mode == 'r':
        x = f.read()
        print(x)
    f.close()
    return
readfiledata('file2.txt')


# In[24]:


# Data Analysis
# Word Count Program
def wordCount(filename,word):
    with open(filename, 'r') as f:
        if f.mode == 'r':
            x= f.read()
            li= x.split()    #It splits the string with whitespace
    cnt= li.count(word)
    return cnt
filename = input('Enter the file name :')
word = input('Enter the word :')  #which word count you need
wordCount(filename,word)


# In[26]:


# character count from the given file
def charcount(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = list(x)
    return len(li)
filename = input('Enter the filename : ')
charcount(filename)
    


# In[29]:


s1 = " Python Programming"
print(s1.split( ))


# In[4]:


#function to find the no of lines in the input files
#Input -- filename(file2.txt)
#Output -- no of lines(12)
def countoflines(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = x.split("\n")
    return len(li)
filename = input('enter  the filename :')
countoflines(filename)


# In[6]:


# function to print the upper and lower character
# Function to print
def caseCount(filename):
    cntUpper = 0
    cntLower = 0
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = list(x)
    for i in li:
        if i.isupper():
            cntUpper += 1 # cntupper = cntupper +1
        elif i.islower():
            cntLower += 1 # cntlower = cntlower +1
    output = 'Upper case = {0} , Lower case = {1}'.format(cntUpper,cntLower)
    return output
filename = input('Enter the filename : ')
caseCount(filename)


# In[8]:


ls


# In[11]:


cd Desktop/PythonProg/Git


# In[12]:


ls


# In[50]:


cd mpilab


# In[51]:


cd Desktop


# In[61]:


cd mpilab\Desktop\prob\git


# In[68]:


ls


# In[70]:


cd prob


# In[72]:


cd git


# In[73]:


ls


# In[74]:


cd ..


# In[76]:


cd ..


# In[77]:


cd ..


# In[78]:


cd probslovingprogramming


# In[79]:


cd git


# In[80]:


ls


# In[81]:


cd ..


# In[82]:


import os
os.listdir('git/')


# In[83]:


li = os.scandir('git/')
for i in li:
    print(i)


# In[84]:


from pathlib import Path
li = Path('git/')
for i in li.iterdir():
    print(i.name)


# In[86]:


import os
dirPath = "Git/"
for i in os.listdir(dirPath):
    if os.path.isfile(os.path.join(dirPath,i)):
        print(i)


# In[87]:


import os
dirPath = "Git/"
for i in os.listdir(dirPath):
    if os.path.isfile(os.path.join(dirPath,i)):
        print(i)


# In[88]:


dirPath = 'Git/'
for i in os.listdir(dirPath):
    if os.path.isdir(os.path.join(dirPath,i)):
        print(i)


# In[89]:


from pathlib import Path
dirPath = Path('Git/')
for i in dirPath.iterdir():
    if i.is_dir():
        print(i.name)


# ###Creating a Single Directory
# 
# 

# In[ ]:


import os
os.mkdir('SingleDirectory')


# In[93]:


import pathlib
p = pathlib.Path('Test')
p.mkdir()


# In[94]:


ls


# ###Creating Multiples Directories
# 
# 

# In[95]:


import os
os.makedirs('2019/July/11')


# In[96]:


ls


# ###Filename Pattern Matching
# 
# 

# In[97]:


import os
dirPath = 'Git/'
for f_name in os.listdir(dirPath):
    if f_name.endswith('.ipynb'):
        print(f_name)


# In[98]:


import os
dirPath = 'Git/'
for f_name in os.listdir(dirPath):
    if f_name.startswith('.ipynb'):
        print(f_name)


# ###Deleting Files and Directories

# In[99]:


ls


# In[100]:


cd git


# In[101]:


ls


# In[103]:


import os
data_file = 'file1.txt' # Give the entire Path
os.remove(data_file)


# In[104]:


pwd


# In[107]:


cd ..


# In[109]:


pwd


# In[111]:


ls


# In[112]:


data_dir = 'Test'
os.rmdir(data_dir)


# In[113]:


pwd


# In[114]:


import shutil
data_dir = '2019'
shutil.rmtree(data_dir)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




