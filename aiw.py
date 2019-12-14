import numpy as np
from pandas import DataFrame, read_csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import seaborn as sns

df = pd.read_csv('stardataset.csv')
#ogólne dane statystyczne dot zmiennych (średnie, centyle itd)
print(df.describe())

#temperatura vs. wielkość
fig = plt.figure()
ax = fig.add_subplot(111)
brawn_dwarfs = df.loc[df['Star type'] == 0]
x0 = brawn_dwarfs["Temperature (K)"]
y0 = brawn_dwarfs["Absolute magnitude(Mv)"]
red_dwarfs = df.loc[df['Star type'] == 1]
x1 = red_dwarfs["Temperature (K)"]
y1 = red_dwarfs["Absolute magnitude(Mv)"]
white_dwarfs = df.loc[df['Star type'] == 2]
x2 = white_dwarfs["Temperature (K)"]
y2 = white_dwarfs["Absolute magnitude(Mv)"]
main_sequences = df.loc[df['Star type'] == 3]
x3 = main_sequences["Temperature (K)"]
y3 = main_sequences["Absolute magnitude(Mv)"]
supergiants = df.loc[df['Star type'] == 4]
x4 = supergiants["Temperature (K)"]
y4 = supergiants["Absolute magnitude(Mv)"]
hypergiants = df.loc[df['Star type'] == 5]
x5 = hypergiants["Temperature (K)"]
y5 = hypergiants["Absolute magnitude(Mv)"]

ax.scatter(x0, y0, c = 'orange', label = 'Brawn Dwarfs')
ax.scatter(x1, y1, c = 'green', label = 'Red Dwarfs')
ax.scatter(x2, y2, c = 'pink', label = 'White Dwarfs')
ax.scatter(x3, y3, c = 'purple', label = 'Main Sequences')
ax.scatter(x4, y4, c = 'grey', label = 'Supergiants')
ax.scatter(x5, y5, c = 'yellow', label = 'Hypergiants')

plt.legend()
plt.ylabel("Temperature")
plt.xlabel("Magnitude")
plt.title("H-R Diagram of Total Stars ")
plt.show()

#temperatura vs. typ gwiazd
y = df["Temperature (K)"]
x = df["Star type"]
plt.xlabel("Star type")
plt.ylabel("Temperature")
plt.scatter(x, y, color = 'grey')
plt.show()

#jaką wielkość przyjmuje dany typ gwiazd
y = df["Absolute magnitude(Mv)"]
x = df["Star type"]
plt.xlabel("Star type")
plt.ylabel("Magnitude")
plt.scatter(x, y, color = 'orange')
plt.show()

#jaką jasność przyjmuje dany typ gwiazd
y = df["Luminosity(L/Lo)"]
x = df["Star type"]
plt.xlabel("Star type")
plt.ylabel("Luminosity")
plt.scatter(x, y, color = 'orange')
plt.show()

#sprawdzam, czy są jakieś braki w danych
print(df.isnull().values.any())
#korelacja
print(df.corr())
#wizualizacja korelacji
f, ax = plt.subplots(figsize=(10, 8))
corr = df.corr()
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)
plt.show()
#każdy z każdym
sns.set(style = "ticks", color_codes=True)
sns.pairplot(data=df, diag_kind="kde", markers="+",
                  plot_kws=dict(s=50, edgecolor="g", linewidth=1),
                  diag_kws=dict(shade=True))
plt.show()
