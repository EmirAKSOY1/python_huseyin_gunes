def topla(*toplanacak,fazladan=0):
    toplam=0
    for deger in toplanacak:
        toplam+=fazladan+deger
    return toplam


print(topla(3,5,9,15.2,36,fazladan=2))
