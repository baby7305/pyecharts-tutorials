#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas
pandas.__version__


# In[8]:


import pandas as pd

a = [1, 2, 3]

myvar = pd.Series(a)

print(myvar[1])


# In[10]:


import pandas as pd

a = ["Google", "Runoob", "Wiki"]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)


# In[ ]:




