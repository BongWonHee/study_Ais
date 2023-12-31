#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ## 병합

# In[2]:


# Sample DataFrames
df1 = pd.DataFrame({'A': [1, 'A_2', 3]}, index=[0, 1, 2])
df2 = pd.DataFrame({'B': [4, 'B_5', 6]}, index=[3, 4, 5])


# In[3]:


df1


# In[4]:


df2


# In[5]:


pd.concat([df1,df2],axis=1) # 선 조치 필요


# In[6]:


df1.count(), df2.count()


# In[7]:


df1_reset = df1.reset_index(drop=True)


# In[8]:


df2_reset = df2.reset_index(drop=True)


# In[9]:


pd.concat([df1_reset,df2_reset],axis=1)


# In[16]:


df3 = pd.DataFrame({'B': ['4', 'None', '6']}, index=[3, 4, 5])


# In[17]:


df3.isnull()


# In[18]:


def convertSICK_SYM(sick_sym) :
    if len(sick_sym) < 3:
        return None
    else :
        return sick_sym[:3]


# In[21]:


df3['B'] = df3['B'].apply(convertSICK_SYM)
df3


# In[23]:


df3.isnull().sum()


# In[ ]:




