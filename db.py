import sqlite3

bag  =sqlite3.connect("a.vt")#tabloyu oluşturdum

cursor = bag.cursor()#işlem yapabilmek için cursor oluşturdum . 


cursor.execute("CREATE TABLE IF NOT EXISTS kitap"
                "(id INTEGER NOT NULL PRIMARY KEY,"
                "isim TEXT , yazar TEXT "
              )

bag.commit()




bag.close()#bağlantıyı kkoparıyoruz