import csv 

baslik = ["sicaklik","nem","basinc"]
veri = [[30,75.5,10],[32,45.5,12],[35,78.5,50],[34,5.5,102]]
with open('sensor_veri.csv','w',encoding='UTF-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(baslik)
    writer.writerows(veri)
    