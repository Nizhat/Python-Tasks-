import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'a': np.random.randint(0, 50, 1000)})

# positively correlated with 'a'
df['b'] = df['a'] + np.random.normal(0, 5, 1000)

# negatively correlated with 'a'
df['c'] = 100 - df['a'] + np.random.normal(0, 5, 1000)

# not correlated with 'a'
df['d'] = np.random.randint(0, 50, 1000)

df.corr()

pd.plotting.scatter_matrix(df, figsize = (6, 6))
plt.show()
