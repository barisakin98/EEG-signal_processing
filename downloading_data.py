#!/usr/bin/env python
# coding: utf-8

# In[6]:


import webbrowser
import pandas as pd
webbrowser.open("https://ftp.gwdg.de/pub/misc/MPI-Leipzig_Mind-Brain-Body-LEMON/MRI_MPILMBB_LEMON/MRI_Raw/sub-010024/ses-01/anat/sub-010024_ses-01_T2w.nii.gz")


# In[20]:


num_list_1="12,23,33,37,45,48,59,81,92,203,225,226,230,238,247,257,260,276,280"
num_list_2="5,19,38,39,45,48,50,50,64,80,91,126,166,222,241,242,243,247,279,302,294"
num_list_3="319,312,306,303,292,291,286,285,274,272,267,262,258,257,234,228,202,201,163,152,148,146,136,94,88,86,84,23,7"
num_list_4="5,10,29,34,43,63,67,77,83,86,89,141,202,264,266,267,273,278,291,299,304"

new_list=num_list_4.split(",")
print(new_list,len(new_list))
for i in new_list:
    print(len(i))

for i in new_list:
    x=i
    if len(i)==1:
        webbrowser.open("https://ftp.gwdg.de/pub/misc/MPI-Leipzig_Mind-Brain-Body-LEMON/MRI_MPILMBB_LEMON/MRI_Preprocessed_Derivetives/sub-01000"+x+"/anat/sub-01000"+x+"_ses-01_acq-mp2rage_brain.nii.gz")
    elif len(i)==2: 
        webbrowser.open("https://ftp.gwdg.de/pub/misc/MPI-Leipzig_Mind-Brain-Body-LEMON/MRI_MPILMBB_LEMON/MRI_Preprocessed_Derivetives/sub-0100"+x+"/anat/sub-0100"+x+"_ses-01_acq-mp2rage_brain.nii.gz")
    elif len(i)==3:
        webbrowser.open("https://ftp.gwdg.de/pub/misc/MPI-Leipzig_Mind-Brain-Body-LEMON/MRI_MPILMBB_LEMON/MRI_Preprocessed_Derivetives/sub-010"+x+"/anat/sub-010"+x+"_ses-01_acq-mp2rage_brain.nii.gz")
        


# In[ ]:




