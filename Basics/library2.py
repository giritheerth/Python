import pandas as pd
import numpy as np
# read the file and print info
df = pd.read_csv('C:\\Users\\theer\\Downloads\\saraniyaa.csv')
print(df.info)


mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
  'rating': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# read json
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)

''' cleaning data:
1. Empty cells
new_df = df.dropna()
new_df = df.dropna(inplace = True)
new_df = df.filena(value=130, inplace= True)
df["Calories"].fillna(130, inplace = True)
2. Data in wrong format
3. Wrong data
4. Duplicates
'''

