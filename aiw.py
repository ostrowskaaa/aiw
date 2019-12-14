import numpy as np
from pandas import DataFrame, read_csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import seaborn as sns

df = pd.read_csv('stardataset.csv')
types = ['0 Brown Dwarf', '1 Red Dwarf', '2 White Dwarf', '3 Main Sequence', '4 Supergiant', '5 Hypergiant']
a = df['Star type']
#ogólne dane statystyczne dot zmiennych (średnie, centyle itd)
print(df.describe())

#temperatura vs. wielkość
x = df["Temperature (K)"]
y = df["Absolute magnitude(Mv)"]
plt.ylabel("Star type")
plt.xlabel("Magnitude")
plt.title("H-R Diagram of Total Stars ")
plt.legend((a,b,c,d,e,f),('Brown Dwarf','Red Dwarf','White Dwarf','Main Sequence','Supergiant','Hypergiant'))
plt.scatter(x, y, color = 'grey')
plt.show()


'''
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
fig = plt.figure()
ax = plt.subplot(111)
y = df["Luminosity(L/Lo)"]
x = df["Star type"]
plt.xlabel("Star type")
plt.ylabel("Luminosity")
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
ax.scatter(x, y, color = 'purple', label=types)
ax.legend(loc = "upper center", bbox_to_anchor = (0.5, -0.05), fancybox = True, shadow = True)
ax.grid(True)
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
'''
