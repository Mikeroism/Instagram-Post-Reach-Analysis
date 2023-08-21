import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

import seaborn as sns
import plotly.express as px 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveClassifier
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator




data = pd.read_csv("Instagram data.csv", encoding ="latin1")
""" 
print(data.head())
"""



plt.figure(figsize=(10,8))
plt.title('Impressions Distribution from Home')
sns.distplot(data['From Home'])
plt.style.use('fivethirtyeight')
""" 
plt.show()
""" 






plt.figure(figsize=(10,8))
plt.title('Impressions Distribution from Hashtags')
sns.distplot(data['From Hashtags'])
plt.style.use('fivethirtyeight')
""" 
plt.show()
""" 

  





plt.figure(figsize=(10,8))
plt.title('Impressions Distribution from Explore')
sns.distplot(data['From Explore'])
plt.style.use('fivethirtyeight')
""" 
plt.show()
""" 






home = data["From Home"].sum()
hashtags = data["From Hashtags"].sum()
explore = data["From Explore"].sum()
other = data["From Other"].sum()

labels = ["From Home", "From Hashtags", "From Explore", "Other"]

values = [home, hashtags, explore, other]

fig = px.pie(data, values= values, names = labels, title = "Impression of Posts By Source", hole = 0.5)

""" 
fig.show()
"""




txt = " ".join(i for i in data.Caption)

stopwords = set(STOPWORDS) 
worldcloud = WordCloud(stopwords = stopwords, background_color="white").generate(txt)

plt.style.use('classic')
plt.figure( figsize = (12, 10))
plt.imshow(worldcloud, interpolation='bilinear')
plt.axis('off')
""" 
plt.show()
"""




txt = " ".join(i for i in data.Hashtags)

stopwords = set(STOPWORDS) 
worldcloud = WordCloud(stopwords = stopwords, background_color="white").generate(txt)

plt.style.use('classic')
plt.figure( figsize = (12, 10))
plt.imshow(worldcloud, interpolation='bilinear')
plt.axis('off')
""" 
plt.show()
"""






figure = px.scatter(data_frame= data, x = "Impressions", y ="Likes", size="Likes", trendline= "ols",
                      title =" Relationship between Impressions and Likes")


"""
fig.show()
"""





figure = px.scatter(data_frame= data, x = "Impressions", y ="Comments", size="Comments", trendline= "ols",
                      title =" Relationship between Impressions and Comments")

"""
fig.show()
"""



figure = px.scatter(data_frame= data, x = "Impressions", y ="Shares", size="Shares", trendline= "ols",
                      title =" Relationship between Impressions and Shares")

"""
fig.show()
"""





figure = px.scatter(data_frame= data, x = "Impressions", y ="Saves", size="Saves", trendline= "ols",
                      title =" Relationship between Impressions and Saves")


"""
fig.show()
"""



conversion_rate = (data["Follows"].sum() / data["Profile Visits"].sum()) * 100
"""
print(conversion_rate)
"""



figure = px.scatter(data_frame= data, x = "Profile Visits", y ="Follows", size="Follows", trendline= "ols",
                      title =" Relationship between Profile Visits and New Followers")

                      

""" 
figure.show()
""" 