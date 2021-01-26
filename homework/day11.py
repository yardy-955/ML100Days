#!/usr/bin/env python
# coding: utf-8

# In[ ]:


運用編碼處理類別資料
補缺失值
作業重點:
類別編碼有多種方法，需分辨使用方法與時機
補缺失值須因應情境決定如何補值
get_ipython().set_next_input("題目 : 將以下問卷資料的職業(Profession)欄位缺失值填入字串'others'，更進一步將字串做編碼。 此時用什麼方式做編碼比較適合?為什麼");get_ipython().run_line_magic('pinfo', '為什麼')

import pandas as pd
q_df = pd.DataFrame([['male', 'teacher'], ['male', 'engineer'], ['female', None], ['female', 'engineer']],columns=['Sex','Profession'])


# In[15]:


import pandas as pd
q_df = pd.DataFrame([['male', 'teacher'], 
              ['male', 'engineer'],
              ['female', None],
              ['female', 'engineer']],columns=['Sex','Profession'])
q_df


# In[ ]:


#更進一步將字串做編碼。 此時用什麼方式做編碼比較適合?為什麼?


# In[16]:


gf=q_df.fillna('others')
gf


# In[21]:


pf = pd.get_dummies(gf[['Profession']])  #Profession為一般性資料，所以get dummy
af = pd.concat([gf, pf], axis=1)
af 

