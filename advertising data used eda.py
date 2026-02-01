import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# this is advertising data
df=pd.read_csv("E:\\VISHAKHA PYTHON ALL IMPORTANT DATA VERY IMPORTANT DATA\EDA RELATED DATA THIS IS USE FOR EDA\\advertising data used eda\\advertising data.csv")
#print(df)
print(df.describe())
df.info()
#print(df['Timestamp'].dtype)
print(df.isnull().sum()) # there is no na and null value
print(df.duplicated().sum()) # no duplicate value in this data
print(df['Male'].value_counts())
print(df['Age'].value_counts())
print(df['City'].value_counts())
# column rename ("ya madhe column cha rename dila ahey")
df.rename(columns={'Male':'Gender'},inplace=True)
print(df.columns)

# outlier availble on lower limit outlier
import matplotlib.pyplot as plt
plt.figure(figsize=(6,4))# here is lower_limit outlier
plt.boxplot(df['Area Income'].dropna())
plt.title('Box plot in area income')
plt.show()

# find the value of outlier
area=df['Area Income']
Q1=area.quantile(0.25)
Q3=area.quantile(0.75)
IQR=Q3-Q1
# we find upper limit and lower limit
lower_limit=Q3-1.5*IQR
upper_limit=Q1+1.5*IQR
print(lower_limit)
print(upper_limit)

# find how many percent of outlier in this data (100 per-cent of outlier)
outlier_p=len(area)/len(area)*100
print(outlier_p)

# replacement of outlier
import numpy as np 
mode_val=df['Area Income'].mode()
median_val=df['Area Income'].median()
print(mode_val,median_val)
df['Area Income']=df['Area Income'].clip(lower_limit,upper_limit)

# check value replace or not
print(df.describe())

# box-plot after using outlier treatment
import matplotlib.pyplot as plt
df.boxplot(column='Area Income')
plt.show()

# histogram after outlier treatment
plt.hist(df['Area Income'],bins=30)
plt.title("data after outlier treatment")
plt.show()

# skwess is availble or not
print(df['Area Income'].skew())

# scatter plot
plt.scatter(df['Area Income'],df['Daily Time Spent on Site'])
plt.xlabel("Age Income")
plt.ylabel("Daily Internet Usage")
plt.title("Scatter plot")
plt.show()

# count ploting 
sns.countplot(x='Gender',data=df)
plt.title("Count plot of Gender")
plt.show()

# pairplot
sns.pairplot(df[['Area Income','Daily Time Spent on Site','Age']])
plt.show()

#violin plot
'''sns.violinplot(x='Daily Time Spent on Site',y='Area Income',data=df)
plt.title("violine-plot")
plt.show()

# bar plot 
sns.barplot(x='Daily Time Spent on Site',y='Gender',data=df)
plt.title("Bar-plot")
plt.show()'''

# line plot
sns.lineplot(x='Area Income',y='Daily Time Spent on Site',data=df)
plt.title("Line-plot")
plt.show()
