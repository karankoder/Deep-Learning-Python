import pandas as pd
import numpy as np

a=np.array([10,20,30,40,50])
b=pd.Series(a)

b=b.astype(np.int64)
print(b)
