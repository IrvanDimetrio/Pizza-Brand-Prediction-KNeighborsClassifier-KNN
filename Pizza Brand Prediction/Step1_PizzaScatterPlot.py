"""
@author : Muhamad Irvan Dimetrio
NIM     : 18360018
Teknik Informatika
Institut Sains dan Teknologi Nasional
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Menampilan scatter plot perbandingan Mois VS Carb
pizza = pd.read_csv('Pizza.csv', names=['Brand', 'Mois', 'Prot', 'Fat', 'Ash', 'Sodium', 'Carb',
                                        'Cal'], header=0, sep=",")

sns.scatterplot(x='Mois', y='Carb', hue='Brand', data=pizza).set_title('Perbandingan Mois VS Carb')
plt.figure(1) # n adalah nomor berbeda untuk setiap window gambar
plt.show()

#Menampilan scatter plot perbandingan Fat VS Ash
pizza2 = pd.read_csv('Pizza.csv', names=['Brand', 'Mois', 'Prot', 'Fat', 'Ash', 'Sodium', 'Carb',
                                        'Cal'], header=0, sep=",")

sns.scatterplot(x='Fat', y='Ash', hue='Brand', data=pizza2).set_title('Perbandingan Fat VS Ash')
plt.figure(1) # n adalah nomor berbeda untuk setiap window gambar
plt.show()