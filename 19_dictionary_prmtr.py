def birim_islem(**birim):
    print("birimin tipi:",type(birim))
    print("birimin adı:",birim["ad"])
    print("birimin Tipi:",birim["tip"])
    print("birimin yil:",birim["yil"])
 
birim_islem(ad="Balıkesir", tip="Üniversite",yil="1992")