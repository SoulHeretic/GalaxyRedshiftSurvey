#!/usr/bin/env python
# coding: utf-8

# In[244]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#name the columns. Otherwise it will be freed as per text.
col_names = ["id", "ra", "dec", "bj","zz","zraw","bjlim","qual","bjg","bjp","bjgp","plate","field date", "eta", "ccd","ecce","orie","jon","area"]
#put file location below.
df = pd.read_table('/Users/-usernamehere-/Documents/parent.ngp.txt', delim_whitespace=True, header=0, names = col_names,skiprows=1)

df2 = df.loc[(df['bjlim'] >= 3) & (df['bj'] <= .1)]

boolean_mask = (df2['bj'] > -9)
grown_df = df2[boolean_mask]

#Ho in meters
Ho = (70000/(3.086*10**22))
#speed of light in meters
c = (3*10**8)
#bj is the z because of it being moved
#id is the right ascension angle
#ra is the declination angle
grown_df['radius'] =(((grown_df['bj'])*c)/Ho)*3.240779289E-23 #turn meters to megaparsecs


    
grown_df['xdeg'] = grown_df['radius'] * np.sin(grown_df['ra'].apply(np.degrees)) * np.cos(grown_df['id'].apply(np.degrees))

grown_df['ydeg'] = grown_df['radius'] * np.sin(grown_df['ra'].apply(np.degrees)) * np.sin(grown_df['id'].apply(np.degrees))

grown_df['zdeg'] = grown_df['radius'] * np.cos(grown_df['ra'].apply(np.degrees))


fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
X = grown_df['xdeg']
Y = grown_df['ydeg']
Z = grown_df['zdeg']

x = [0]
y = [0]
z = [0]

ax.scatter(X,Y,Z,c='r', marker = 'o',s=.001)#reduce marker size by a lot

ax.scatter(x,y,z,c='b', marker = 'o',s=100)
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')



plt.show()
print(grown_df)
