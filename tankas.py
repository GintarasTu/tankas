
class Tankas:
    tuscio_lauko_reiksme = " - "

    kryptys = {0: "į šiaurę,", 1: "į rytus,", 2: "į pietus,", 3: "į vakarus,"}
    suviu_kiekis_pagal_krypti = [0] * len(kryptys)
    zaidimo_pabaiga = False

    def __init__(self, x, y, kryptis, lauko_ilgis, lauko_aukstis):
        self.x = x
        self.y = y
        self.kryptis = kryptis
        self.ilgis = lauko_ilgis
        self.aukstis = lauko_aukstis
        self.zaidimo_plotas = [[self.tuscio_lauko_reiksme for i in range(lauko_ilgis)] for b in range(lauko_aukstis)]

    def pirmyn(self):
        self.kryptis = 0
        if (self.y != 0):
            self.y -= 1
            self.__istrinti_sena_pozicija(self.x, self.y + 1)

    def desinen(self):
        self.kryptis = 1
        if (self.x != self.ilgis - 1):
            self.x += 1
            self.__istrinti_sena_pozicija(self.x - 1, self.y)

    def atgal(self):
        self.kryptis = 2
        if (self.y != self.aukstis - 1):
            self.y += 1
            self.__istrinti_sena_pozicija(self.x, self.y - 1)

    def kairen(self):
        self.kryptis = 3
        if (self.x != 0):
            self.x -= 1
            self.__istrinti_sena_pozicija(self.x + 1, self.y)

    def suvis(self):
        self.suviu_kiekis_pagal_krypti[self.kryptis] += 1

    def baigti_zaidima(self):
        self.zaidimo_pabaiga = True
        print("Žaidimas baigtas. Viso gero!")

    def ar_zaidimo_pabaiga(self):
        return self.zaidimo_pabaiga

    def info(self):
        print("Tanko informacija:")
        print(f"     pozicija x: {self.x} y: {self.y}")
        print(f"     kryptis: {self.kryptys[self.kryptis]}")
        print("Šūviai pagal pozicijas:")
        for key in self.kryptys:
            print(f"     kryptis: {self.kryptys[key]} šūvių skaičius: {self.suviu_kiekis_pagal_krypti[key]}")

    def __piesti_tanka(self):
        self.zaidimo_plotas[self.y][self.x] = " X "

    def __istrinti_sena_pozicija(self, x, y):
        self.zaidimo_plotas[y][x] = self.tuscio_lauko_reiksme

    def musio_laukas(self):
        self.__piesti_tanka()

        for y in range(self.aukstis):

            eilute = ""
            for x in range(self.ilgis):
                eilute += (self.zaidimo_plotas[y][x])
            print(eilute)
