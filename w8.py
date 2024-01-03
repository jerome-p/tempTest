import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

electrons_df = pd.read_csv("electrons.csv", delimiter=' ')


x = np.array(electrons_df['Distance'])
y = np.array(electrons_df['Energy'])

plt.scatter(x,y)

result = np.polyfit(x,y,1)

a = result[1]
b = result[0]

yfit = a + b*x

plt.plot(x,yfit,c='red')

elfield = b/1.6e-19