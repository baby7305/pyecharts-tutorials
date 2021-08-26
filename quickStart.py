#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas
pandas.__version__


# In[5]:


import pandas as pd

mydataset = {
  'sites': ["Google", "Runoob", "Wiki"],
  'number': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)

print(myvar)


# In[ ]:




