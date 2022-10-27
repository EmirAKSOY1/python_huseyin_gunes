dosya = open("cop.txt",'w')

print("print('wfw')", file=dosya)

dosya.close()

dosya=open("cop.txt",'r')

satir=dosya.readline()
eval(satir)
dosya.close()