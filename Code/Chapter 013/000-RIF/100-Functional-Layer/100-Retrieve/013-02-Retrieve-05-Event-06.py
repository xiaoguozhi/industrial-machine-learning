#!/usr/bin/env python
# coding: utf-8

# ## Apress - Industrialized Machine Learning Examples
# 
# Andreas Francois Vermeulen
# 2019
# 
# ### This is an example add-on to a book and needs to be accepted as part of that copyright.

# # Chapter-013-02-Retrieve-Event-06

# In[1]:


import datetime
import os
nowStart = datetime.datetime.now()


# In[2]:


dirbasename=os.path.abspath(os.path.join(*[os.path.dirname(os.path.dirname(os.getcwd()))], os.pardir))
print(dirbasename)
dirname = os.path.abspath(os.path.join(dirbasename,'900-DL/100-Raw-Zone/200-Load-Data/05-Event'))
print(dirname)


# ![RIF Functional Layer - Retrieve Step](../../../../../images/DV-Event.JPG)

# ![RIF Functional Layer - Retrieve Step](../../../../../images/RIF-FL-RET.JPG)

# In[3]:


setnr=6
filename='13-02-Retrieve-Event-%06d.csv' % setnr
fileZipname=filename + '.gz'
print(fileZipname)


# In[4]:


import pandas as pd


# # Load Events

# In[5]:


dirDataName = os.path.abspath('../../../../../Data/Chapter 13/000-ExternalData/05-Event/')
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# In[6]:


fileDataName='Event-%06d.csv.gz' % setnr
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[7]:


objectFullDF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(objectFullDF.shape)


# # Create 100-Raw-Zone

# ![Raw Zone](../../../../../images/DL-RZ.JPG)

# In[8]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[9]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Save Events

# In[10]:


objectFullDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[11]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




