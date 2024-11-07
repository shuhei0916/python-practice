import pandas as pd
import numpy as np

print(pd.__version__)

df_simple = pd.DataFrame(np.arange(12).reshape(3, 4))
print(df_simple)

print(df_simple.values)
print(type(df_simple.values))

