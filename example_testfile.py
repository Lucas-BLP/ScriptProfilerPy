import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ts = pd.Series(np.random.randn(1000),
               index=pd.date_range("1/1/2000", periods=1000))
ts

ts = np.exp(ts.cumsum())
df = pd.DataFrame(np.random.randn(1000, 4),
                  index=ts.index, columns=list("ABCD"))
df
df.head()
df.head()
for i in df.index:
    df.tail()
df.head()
df.head()
df.tail()
for i in df.index:
    
    df.tail()
df.tail()
df.tail()
for i in df.index:
    df.tail()
