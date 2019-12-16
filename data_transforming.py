#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import os
import time


# In[5]:


main_path="C:/Users/User/Desktop/PD"
files=os.listdir(main_path)
print(os.listdir(main_path))
path_1=main_path+"/"+files[0]
path_2=main_path+"/"+files[1]
path_3=main_path+"/"+files[2]
path_4=main_path+"/"+files[3]

print(len(os.listdir(path_1)),len(os.listdir(path_2)),len(os.listdir(path_3)),len(os.listdir(path_4)))


# In[6]:


get_ipython().system('pip install nibabel')
import nibabel as nib


# In[7]:


list_of_RSH=[]
list_of_RSL=[]
list_of_RDH=[]
list_of_RDL=[]


for i in range(4):
    for a in os.listdir(main_path+"/"+files[i]):
        new_path=main_path+"/"+files[i]+"/"+a
        img=nib.load(new_path) 
        img=img.get_fdata()
        if i==0:
            list_of_RSH.append(img)
        elif i==1:
            list_of_RSL.append(img)
        elif i==2:
            list_of_RDH.append(img)
        elif i==3:
            list_of_RDL.append(img)
            
print(len(list_of_RSH),len(list_of_RSL),len(list_of_RDH),len(list_of_RDL))

        


# In[19]:


#CONTROL BLOCK
plt.imshow(list_of_RSH[1][176,:,:])
plt.show()
trial_path="C:/Users/User/Desktop/PD/Reapraisal-Suppression (high) PREPROCESSED/sub-010023_ses-01_acq-mp2rage_brain.nii"
img2=nib.load(trial_path)
img2=img2.get_fdata()
plt.figure()
plt.imshow(img2[176,:,:])
plt.show()
array=img2[176,:,:]-list_of_RSH[1][176,:,:]
print(np.sum(array))


# In[26]:


#CONTROL BLOCK-2
list_of_all=list_of_RSH+list_of_RSL+list_of_RDH+list_of_RDL
a=0
for i in list_of_all:
    if i.shape!=(256,256,256):
        print("error")
    else:
        a+=1
print(a)
        


# In[27]:


RSH_array=np.asarray(list_of_RSH)
RSL_array=np.asarray(list_of_RSL)
RDH_array=np.asarray(list_of_RDH)
RDL_array=np.asarray(list_of_RDL)


# In[31]:


print(RSH_array.shape,RSL_array.shape,RDH_array.shape,RDL_array.shape)
np.save("C:/Users/User/Desktop/RSH_array.npy",RSH_array)
np.save("C:/Users/User/Desktop/RSL_array.npy",RSL_array)
np.save("C:/Users/User/Desktop/RDH_array.npy",RDH_array)
np.save("C:/Users/User/Desktop/RDL_array.npy",RDL_array)


# In[ ]:


##arrayler birleştirilip shuffle edilecek. daha sonra train-val olarak separate edilecek. 

