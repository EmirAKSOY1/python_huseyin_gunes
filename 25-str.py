class sinif():
    metin=""
    def __init__(self,a):
        self.metin=a

    def __str__(self):
        return "yazdırılan : " + self.metin
    #direkt nesne yazdırıldığında str içersindeki metin yazdırılır 
nesne=sinif("metin")

print(nesne)

