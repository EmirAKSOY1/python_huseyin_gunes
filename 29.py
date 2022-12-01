import os
import zipfile
import pandas as pd
import sqlite3

if not os.path.exists("veri"):
    os.mkdir("veri")
    arsiv = zipfile.ZipFile("pariteler_cikti_1hour_2022_2022.zip")
    arsiv.extractall("veri/")

else:
    pandas_csv_list = []
    tum_dosyalar = os.listdir('veri')
    for i in tum_dosyalar:
        veri=pd.read_csv("veri/"+i)
        del veri["volume"]
        
        pandas_csv_list.append(veri)
    """
    
    """   

    birlesmis=pd.concat(pandas_csv_list)
    birlesmis.to_csv('deneme.csv',index=False)

    bag  =sqlite3.connect("parite.vt")#tabloyu oluşturdum

    cursor = bag.cursor()#işlem yapabilmek için cursor oluşturdum .
    cursor.execute("""CREATE TABLE IF NOT EXISTS  parite ("
                
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	otime DATETIME,
	open FLOAT,
	high FLOAT,
	low FLOAT,
	close FLOAT
	
");"""
              )

    bag.commit()
    bag.close()


