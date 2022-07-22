#!/usr/bin/env python
# coding: utf-8

# In[2]:


#get_ipython().system('pip install -q streamlit')


# In[3]:


import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle


# In[4]:


st.write("""
# Even/Odd Identification App
This app identifies the app as even or odd
""")


# In[5]:


#Get Input

st.header('User Input Parameters')


# In[6]:


def user_input_features():
    input_number = st.number_input("Input_number",min_value=0,max_value=100,step=1)
    
    return input_number

num = user_input_features()


# In[7]:


st.subheader('User Input number')
st.write(num)


# In[8]:


st.subheader('The given Number is:')
if num%2 == 0:
    st.write('EVEN')
else:
    st.write('ODD')

