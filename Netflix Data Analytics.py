#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pandas library
import pandas as pd


# In[2]:


#importing dataset
data=pd.read_csv(r"C:\Users\HP 2021\Desktop\8. Netflix Dataset.csv")
#r--to remove unicode error


# In[3]:


data


# # 1.head()

# In[4]:


data.head()       #to show top-5 records of the dataset 


# # 2.tail()

# In[5]:


data.tail()    # to show bottom-5 records of dataset 


# # 3.shape

# In[6]:


data.shape    #to show th NO.of Rows and Columns


# # 4.size

# In[7]:


data.size    #To show No. of total values(elements) in the dataset


# # 5.columns

# In[8]:


data.columns  #To show each column name


# # 6.dtypes

# In[9]:


data.dtypes     #To show the data-type of each column


# # 7.info()

# In[10]:


data.info()    #To show indexes, columns, data-types of each column, memory at once


# # Task1.Is there any Duplicate Record in this dataset?if yes,then remove the duplicate records
# 
# 
# duplicate()
# 

# In[11]:


data.head()


# In[12]:


data.shape


# In[13]:


data[data.duplicated()]     #To check row wise and detect the Duplicate rows


# In[14]:


data.drop_duplicates(inplace=True) #To Remove the Duplicate rows permanently


# In[15]:


data[data.duplicated()]


# In[16]:


data.shape


# # Task.2.Is there any Null Value present in any column?Show with Heat-map.

# # isnull()

# In[17]:


data.head()


# In[18]:


data.isnull()      #To show where Null value is present


# In[19]:


data.isnull().sum()    #To show the count of Null values in each column


# # seaborn library(heat-map)

# In[20]:


import seaborn as sns   #To import seaborn library


# In[21]:


sns.heatmap(data.isnull())     #Using heat-map to show null values count


# In the figure above  the white colors are the null values

# # Q.1.For 'House of Cards',what is the Show id and who is the director of this show?

# # isin()

# In[22]:


data.head(2)


# In[23]:


data[data['Title'].isin(['House of Cards'])]   #To show all records of a particular item in any column


# # str.contains()

# In[24]:


data[data['Title'].str.contains('House of Cards')]   #To show all records of a particular string in any column


# # Q.2.In which year highest number of the TV Shows &Movies were released?Show with Bar Graph.

# # dtypes

# In[25]:


data.dtypes


# # to_datetime

# In[26]:


data['Data_N']=pd.to_datetime(data['Release_Date'])


# In[27]:


data.head()


# # dt.year.value_counts()

# In[28]:


data['Data_N'].dt.year.value_counts()   #It counts the occurrence of all individual years in Time column


# # Bar Graph

# In[29]:


data['Data_N'].dt.year.value_counts().plot(kind='bar')


# # Q.3.How many Movies&TV Shows are in the dataset?Show with Bar Graph.

# In[30]:


data.head(2)


# In[31]:


data.groupby('Category').Category.count()  #To group all unique items of a column and show their count


# # countplot()

# In[32]:


sns.countplot(data['Category'])    #To show the count of all unique values of any column in the form of bar graph


# # Q.4.Show all the Movies that were released in year 2020.

# In[33]:


data.head(2)


# In[34]:


data['Year']=data['Data_N'].dt.year  #To create new Year column;it will consider only year


# In[35]:


data.head(2)


# # Filtering

# In[36]:


data[(data['Category']=='Movie')&(data['Year']==2020)]


# # Q.5.Show only the Titles of all TV Shows that were released in India only.

# # Filtering

# In[37]:


data.head(2)


# In[38]:


data[(data['Category']=='TV Show')&(data['Country']=='India')]['Title']


# # Q.6.Show Top 10 Directors,who gave the highest number of TV Shows &Movies to Netflix?

# # value_counts()

# In[39]:


data.head(2)


# In[40]:


data['Director'].value_counts().head(10)


# # Q.7.Show all the Records ,where "Category is Movie and Type is Comedies"or "Country is United Kingdom".

# # Filtering (And ,Or Operators)

# In[41]:


data.head(2)


# In[42]:


data[(data["Category"]=='Movie')&(data['Type']=='Comedies')|(data['Country']=="United Kingdom")].head(2)


# # Q.8.In how many movies/shows,Tom Cruise was cast?

# In[43]:


data.head(2)


# # filtering

# In[45]:


data[data['Cast']=="Tom Cruise"]


# # str.contains()

# In[47]:


data[data['Cast'].str.contains("Tom Cruise")]


# # Creating new data-frame

# In[49]:


data_new=data.dropna()    #it drops the rows that contains all or any missing values


# In[50]:


data_new.head(2)


# In[51]:


data_new[data_new["Cast"].str.contains("Tom Cruise")]


# # Q.9.What are the different Ratings defined by Netflix?

# # nunique()

# In[52]:


data.head(2)


# In[53]:


data.Rating.nunique()         #It shows the total no. of unique values in the series


# # unique()

# In[54]:


data.Rating.unique()    #It shows the all unique values of the series


# # Q.9.1.How many Movies got the "TV-14" rating in Canada?

# In[55]:


data.head(2)


# In[59]:


data[(data["Category"]=="Movie") &(data["Rating"]=="TV-14")].shape


# In[60]:


data[(data["Category"]=="Movie") &(data["Rating"]=="TV-14")&(data["Country"]=="Canada")].shape


# # Q.9.2.How many TV Show got the "R" rating.after year 2018?

# In[61]:


data.head(2)


# In[63]:


data[(data["Category"]=="TV Show") &(data["Rating"]=="R")].shape


# In[68]:


data[(data["Category"]=="TV Show") &(data["Rating"]=="R")&(data["Year"]>2018)].shape


# # Q.10.What is the Maximum duration of a Movie/Show on Netflix?

# In[69]:


data.head(2)


# In[70]:


data["Duration"].unique()


# In[72]:


data.Duration.dtypes


# # str.split()

# In[79]:


data[["Minutes","Unit"]]=data["Duration"].str.split(" ",expand=True)    # It splits a column's string into different columns


# In[80]:


data.head(2)


# # max()

# In[81]:


data.Minutes.max()


# In[85]:


data.dtypes


# In[86]:


data["Minutes"].min()


# In[87]:


data["Minutes"].mean()


# # Q.11.Which individual country has the Highest No. of TV Shows?

# In[88]:


data.head(2)


# In[89]:


data_tvshow=data[data["Category"]=="TV Show"]


# In[90]:


data_tvshow.head(2)


# In[91]:


data_tvshow.Country.value_counts()


# In[96]:


data_tvshow.Country.value_counts().head(2)


# # Q.12.How can we sort the dataset by Year?

# In[97]:


data.head(2)


# In[98]:


data.sort_values(by="Year").head(2)


# In[99]:


data.sort_values(by="Year",ascending=False).head(2)


# # Q.13.Find all the instances where:

# # Category is "Movie" and Type is "Drams"

# # or 

# # Category is "TV Show"&Type is "Kids TV"

# In[100]:


data.head(2)


# In[108]:


data[(data["Category"]=="Movie")&(data["Type"]=="Dramas")].head(2)


# In[113]:


data[(data["Category"]=="TV Show")&(data["Type"]=="Kids' TV")].head(2)


# In[118]:


data[(data["Category"]=="Movie")&(data["Type"]=="Dramas")|(data["Category"]=="TV Show")&(data["Type"]=="Kids'TV")].head()


# In[ ]:




