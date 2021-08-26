#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas
pandas.__version__


# In[17]:


import pandas as pd

data = [['Google',10],['Runoob',12],['Wiki',13]]

df = pd.DataFrame(data,columns=['Site','Age'])

print(df)


# In[ ]:




