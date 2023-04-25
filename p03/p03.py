import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

data=pd.read_csv("../heart_data_subsample.csv")
print(data.head())