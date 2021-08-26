#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas
pandas.__version__


# In[6]:


import pandas as pd

df = pd.read_csv('nba.csv')

print(df)


# In[7]:


import pandas as pd
   
# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
   
# 字典
dict = {'name': nme, 'site': st, 'age': ag}
     
df = pd.DataFrame(dict)
 
# 保存 dataframe
df.to_csv('site.csv')


# In[ ]:




