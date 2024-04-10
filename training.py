import numpy as np
import pandas as pd

 
def loadDataAndTargets():
    df = pd.read_csv("final_data.csv")
    # print(df)
    # X = df.loc[:, df.columns != 'win']
    df.columns.values[0] = "index"
    X = df.drop(['index','win'], axis=1)
    y = df["win"]
    return X, y.to_numpy()

df, y = loadDataAndTargets()
print(df)