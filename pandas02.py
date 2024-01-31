# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:46:55 2024

@author: APUGNALIN

css2024 day 2
"""

import pandas as pd

file = pd.read_csv("iris.csv")
df = pd.DataFrame(file)


column_headers = list(df.columns.values)
print("Headers :", column_headers)


# df1 = pd.read_csv("person_split1.csv")
# df2 = pd.read_csv("person_split2.csv")
# df = pd.concat([df1, df2], ignore_index=True)
# print(df)

# join two tables by ID field
# df1 = pd.read_csv('person_education.csv')
# df2 = pd.read_csv('person_work.csv')

## inner join
# df_merge = pd.merge(df1,df2,on='id')

df.rename(columns={"class":"iris_class"}, inplace = True)
column_headers = list(df.columns.values)
print("Headers :", column_headers)
df["iris_class"] = df["iris_class"].str.replace("Iris-", "")
print(df)

df = df[df["sepal_length"] > 5]
df = df[df["iris_class"] == "virginica"]
df.to_csv("pulsar.csv")