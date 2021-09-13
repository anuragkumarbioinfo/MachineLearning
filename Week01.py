
import numpy as np
import pandas as pd

# Q1
print(np.__version__)
# Q2
print(pd.__version__)


data = pd.read_csv("data.csv")

# Q3
BMW_MEAN = data[data.Make == "BMW"].MSRP.mean()
print(BMW_MEAN)

# Q4
HP_DATA = data[data.Year >= 2015][["Engine HP"]]
EMPTY = HP_DATA.isnull().sum()
print(EMPTY)

# Q5
MEAN_Before = HP_DATA.mean()
data2 = HP_DATA.fillna(272.987719)
MEAN_after = data2.mean()
print(MEAN_Before == MEAN_after)

# Q6
RR = Data[Data.Make == "Rolls-Royce"][["Engine HP", "Engine Cylinders", "highway MPG"]]
X = RR.drop_duplicates()


XT = X.T
XTX = XT.dot(X)
inv = np.linalg.inv(XTX) 
sum_inv = sum(sum(inv))

# Q7
y = np.array([1000, 1100, 900, 1200, 1000, 850, 1300])
w = inv.dot(X.T).dot(y)
print(w[0])
