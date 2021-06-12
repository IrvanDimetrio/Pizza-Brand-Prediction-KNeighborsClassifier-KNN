"""
@author : Muhamad Irvan Dimetrio
NIM     : 18360018
Teknik Informatika
Institut Sains dan Teknologi Nasional
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

pizzaDataset = pd.read_csv('Pizza.csv', header = 0)

fitur = pizzaDataset.iloc[:, 1:8].values
label = pizzaDataset['Brand'].values

# Splitting the dataset into the Training set and test set
X_train, X_test, y_train, y_test = train_test_split(fitur, label, test_size = 0.2, random_state=7)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Melatih model dengan X_train, Y_train
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Hitung akurasi dari model
y_pred = classifier.predict(X_test)

print("Akurasi menggunakan Naive Bayes adalah : ", accuracy_score(y_test, y_pred))