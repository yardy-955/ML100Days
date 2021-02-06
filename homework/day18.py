#!/usr/bin/env python
# coding: utf-8

# # 教學目標 
# 
# 主要說明matplotlib 的基礎操作
# 
# 
# 
# # 範例重點
# 
# 如何使用亂數, 資料集來操作
# 

# In[3]:


# 載入需要的...
import matplotlib.pyplot as plt
import numpy as np

# 準備數據 ... 假設我要畫一個sin波 從0~180度
# 設定要畫的的x,y數據list....
x = np.arange(0,180)
y = np.cos(x * np.pi / 180.0)

# 開始畫圖
plt.plot(x,y)
# 在這個指令之前，都還在做畫圖的動作 
# 這個指令算是 "秀圖"
plt.show() 

#畫出完整的 sin 圖形
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)

plt.plot(x, y_sin)

plt.show()


# In[5]:


#畫出完整的 cos 圖形
'''
作業

'''


#畫出完整的 sin 圖形
x = np.arange(0, 3 * np.pi, 0.1)
y_cos = np.cos(x)

plt.plot(x, y_cos)

plt.show()


# # 散點圖: Scatter Plots
#     
#     顏色由（X，Y）的角度給出。
# 
#     注意標記的大小，顏色和透明度。

# In[5]:


n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

'''
#作業

#方法不只有一種

'''

plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

plt.show()


# In[6]:



import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

plt.scatter(X,Y)
plt.show()

