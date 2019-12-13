#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install nibabel')


# In[1]:


import numpy as np
from nibabel.testing import data_path


# In[2]:


import os
example_file_name=os.path.join(data_path, 'example.nii')


# In[3]:


print(type(example_file_name))
print(example_file_name)
import nibabel as nib


# In[30]:


# img=nib.load("C:/Users/User/Desktop/example2.nii")
# print(type(img))
# print(img.shape)
# data=img.get_fdata()
# print(type(data),data.shape)
import cv2
import matplotlib.pyplot as plt

#176.256.256 olduğu için normal split ile parçalayamayız. 3 tane değil 176 tane derinlik var çünkü. 

#plt.imshow(data[155,:,:])
img2=nib.load("C:/Users/User/Desktop/example20.nii")   #Preprocessed
data1=img2.get_fdata()
plt.figure()
plt.imshow(data1[100,::])

img3=nib.load("C:/Users/User/Desktop/example21.nii")   #T1 ağırlıklı 
data2=img3.get_fdata()
plt.figure()
plt.imshow(data2[100,::])

img4=nib.load("C:/Users/User/Desktop/example22.nii")    #T2 ağırlıklı 
data3=img4.get_fdata()
plt.figure()
plt.imshow(data3[100,::])

print(data2[100,::])

def show_all_slices(data):
    x=0 
    while x<176:
        if x==155:
            data1=data[x,:,:]
            plt.figure()
            plt.imshow(data1)
            plt.show()
        x+=1


# In[31]:


import json
data=json.load()


# In[ ]:





# In[ ]:




