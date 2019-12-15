import numpy as np
from pandas import DataFrame, read_csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import seaborn as sns

df = pd.read_csv('stardataset.csv')
df1 = df.drop('Star type', axis=1)
#ogólne dane statystyczne dot zmiennych (średnie, centyle itd)
print(round(df.describe(), 2))
#df.describe().to_csv("ogólne statystyki.csv")

# średnie wartości dla danego typu gwiazd
print(round(df.groupby('Star type').mean(),3))

#porządkowanie kolorków
df.replace(['yellow-white', 'Yellowish White', 'White-Yellow'], 'White Yellow', inplace=True)
df.replace(['yellowish'], 'Yellowish', inplace=True)
df.replace(['white', 'Whitish'], 'White', inplace=True)
df.replace(['Blue-White', 'Blue-white', 'Blue White'], 'Blue White', inplace=True)
df.replace(['yellowish'], 'Yellowish', inplace=True)
print(pd.crosstab(df['Star type'], df['Star color']).stack())


def wykres_wyodrebnione_typy_gwiazd(zmienna1, zmienna2):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    brawn_dwarfs = df.loc[df['Star type'] == 0]
    x0 = brawn_dwarfs[zmienna1]
    y0 = brawn_dwarfs[zmienna2]
    red_dwarfs = df.loc[df['Star type'] == 1]
    x1 = red_dwarfs[zmienna1]
    y1 = red_dwarfs[zmienna2]
    white_dwarfs = df.loc[df['Star type'] == 2]
    x2 = white_dwarfs[zmienna1]
    y2 = white_dwarfs[zmienna2]
    main_sequences = df.loc[df['Star type'] == 3]
    x3 = main_sequences[zmienna1]
    y3 = main_sequences[zmienna2]
    supergiants = df.loc[df['Star type'] == 4]
    x4 = supergiants[zmienna1]
    y4 = supergiants[zmienna2]
    hypergiants = df.loc[df['Star type'] == 5]
    x5 = hypergiants[zmienna1]
    y5 = hypergiants[zmienna2]

    ax.scatter(x0, y0, c = 'orange', label = 'Brawn Dwarfs')
    ax.scatter(x1, y1, c = 'green', label = 'Red Dwarfs')
    ax.scatter(x2, y2, c = 'pink', label = 'White Dwarfs')
    ax.scatter(x3, y3, c = 'purple', label = 'Main Sequences')
    ax.scatter(x4, y4, c = 'grey', label = 'Supergiants')
    ax.scatter(x5, y5, c = 'yellow', label = 'Hypergiants')

#temperatura vs. jasność
wykres_wyodrebnione_typy_gwiazd("Temperature (K)", "Luminosity(L/Lo)")
plt.legend()
plt.xlabel("Temperature")
plt.ylabel("Luminosity")
plt.show()

#jasność vs. jasność względna
wykres_wyodrebnione_typy_gwiazd("Luminosity(L/Lo)", "Absolute magnitude(Mv)")
plt.legend()
plt.xlabel("Luminosity")
plt.ylabel("Magnitude")
plt.show()

#temperatura vs. jasność względna
wykres_wyodrebnione_typy_gwiazd("Temperature (K)", "Absolute magnitude(Mv)")
plt.legend()
plt.xlabel("Temperature")
plt.ylabel("Magnitude")
plt.show()

#radius vs. kuminosity
x = df["Radius(R/Ro)"]
y = df["Luminosity(L/Lo)"]
plt.xlabel("Radius")
plt.ylabel("Luminosity")
plt.scatter(x, y, color = 'green')
plt.show()
####
wykres_wyodrebnione_typy_gwiazd("Radius(R/Ro)", "Luminosity(L/Lo)")
plt.legend()
plt.xlabel("Temperature")
plt.ylabel("Radius")
plt.show()

#temperatura vs. typ gwiazd
x = df["Star type"]
y = df["Temperature (K)"]
plt.xlabel("Star type")
plt.ylabel("Temperature")
plt.scatter(x, y, color = 'grey')
plt.show()

#jaką jasność względną przyjmuje dany typ gwiazd
x = df["Star type"]
y = df["Absolute magnitude(Mv)"]
plt.xlabel("Star type")
plt.ylabel("Magnitude")
plt.scatter(x, y, color = 'orange')
plt.show()

#jaką jasność przyjmuje dany typ gwiazd
x = df["Star type"]
y = df["Luminosity(L/Lo)"]
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
