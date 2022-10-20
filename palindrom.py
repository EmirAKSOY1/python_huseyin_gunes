
def bul(*params):
    polindrom_top=0
    olmayan=0
    for x in params:
        x=str(x)
        ters=x[::-1]
        if(x==ters):
            polindrom_top+=int(x)
        else:
            olmayan+=int(x)
    return polindrom_top-olmayan
    
print(bul(10,101,55,40,9009))