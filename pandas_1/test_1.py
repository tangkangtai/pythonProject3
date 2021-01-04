import pandas as pd
import numpy as np

# df = np.random.randn(5)
df = pd.DataFrame([1,2,3,5,5],columns=['number'],index=list('abcde'))
print(df)
print('-------------')


print(df.idxmax())