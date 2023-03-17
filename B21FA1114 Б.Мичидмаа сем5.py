#!/usr/bin/env python
# coding: utf-8

# In[11]:


#1-р даалгавар
def a(n):
    for i in range (0, n):
        for j in range (0, i+1):
            print("*", end = " ")
        print("\r")
a(6)


# In[29]:


#2-р даалгавар
def x(n):
    for i in range (0, n):
        for j in range (0, i+1):
            print("*", end = " ")
        print("\r")
x(6)


# In[17]:


#3-р даалгавар
dict_students = {
 'Bat': 18,
 'Oyun': 22,
 'Dulam': 21,
 'Suren': 20
}
max_value = max(dict_students.values())
print(max_value)


# In[12]:


#4-р даалгавар
import numpy as np
a = np.arange(1, 1000)
b = a[(a % 3 == 0) | (a % 7 == 0)]
print(b[:1000])
print(b.sum())


# 
