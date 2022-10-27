import pandas as pn

veri= pn.read_csv("iris.data")
"""
print(veri.head())#büyük dosyalarda hepsini görmektense en üsttekileri görmeye yarar.
print(veri.columns)#sütunları yazar
print(veri[3:7])#ikisi arasındaki verileri gösterir.
"""
print(veri.sort_values(by="sepal_length"))


