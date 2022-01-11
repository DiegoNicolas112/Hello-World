#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


comments=pd.read_csv('/Users/diegoaviles/Desktop/Data Analytics - Python/1-Youtube Text Data Analysis/GBcomments.csv',error_bad_lines=False)


# In[3]:


comments.head()


# In[4]:


pip install textblob


# In[5]:


from textblob import TextBlob


# In[6]:


TextBlob('Its more accurate to call it the M+ (1000) be..').sentiment.polarity


# In[7]:


comments.isna().sum()


# In[ ]:


comments.dropna(inplace=True)


# In[ ]:


polarity=[]
for i in comments['comment_text']:
    polarity.append(TextBlob(i).sentiment.polarity)


# In[ ]:


comments['polarity']=polarity


# In[ ]:


comments.head(20)


# In[ ]:


comments_positive = comments[comments['polarity']==1]


# In[ ]:


comments_positive.shape


# In[ ]:


comments_positive.head()


# In[ ]:


pip install wordcloud


# In[ ]:


from wordcloud import WordCloud,STOPWORDS


# In[ ]:


stopwords = set(STOPWORDS)


# In[ ]:


comments_positive['comment_text']


# In[ ]:


total_comments =''.join(comments_positive['comment_text'])


# In[ ]:


wordcloud = WordCloud(width=1000,height=500,stopwords=stopwords).generate(total_comments)


# In[ ]:


plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis('off')


# In[ ]:


videos=pd.read_csv('/Users/diegoaviles/Desktop/Data Analytics - Python/1-Youtube Text Data Analysis/USvideos.csv',error_bad_lines=False)


# In[ ]:


videos.head()


# In[ ]:


# Con este comando puedo traer seleccionar y traer datos de la columna

videos['tags']


# In[ ]:


# Al ingresar join estas uniendo todas las etiquetas

' '.join(videos['tags'])


# In[ ]:


# Almacenaremos todas estas etiquetas en una variable

tags_complete = ' '.join(videos['tags'])


# In[ ]:


tags_complete


# In[ ]:


import re


# In[ ]:


re.sub('[^a-zA-Z]',' ',tags_complete)


# In[ ]:


tags=re.sub(' +',' ',tags)


# In[ ]:


wordcloud=WordCloud(width=1000,height=500,stopwords=set(STOPWORDS)).generate(tags)


# In[ ]:


plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis('off')


# In[ ]:


# Q2 


# In[ ]:


sns.regplot(data=videos,x='views',y='likes')
plt.title('Regression plot for views & likes')


# In[ ]:


df_corr=videos[['views','likes','dislikes']]


# In[ ]:


df_corr.corr()


# In[ ]:


sns.heatmap(df_corr.corr(),annot=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




