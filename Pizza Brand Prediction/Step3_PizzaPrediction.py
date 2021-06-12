"""
@author : Muhamad Irvan Dimetrio
NIM     : 18360018
Teknik Informatika
Institut Sains dan Teknologi Nasional
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

dataset = pd.read_csv('Pizza.csv', header=0)
x = dataset.iloc[:, 1:8].values
y = dataset['Brand'].values

model = KNeighborsClassifier(n_neighbors =7)
model.fit(x, y)

mois = float(input("Masukkan Moisture : "))
prot = float(input("Masukkan Protein : "))
fat = float(input("Masukkan Lemak : "))
ash = float(input("Masukkan Ash : "))
sodium = float(input("Masukkan Sodium : "))
carb = float(input("Masukkan Karbohidrat : "))
cal = float(input("Masukkan Kalsium : "))

prediction = model.predict([[mois, prot, fat, ash, sodium, carb, cal]])
print('Prediksi Brand Adalah : ' + prediction)