from tankas import Tankas

while True:
    asies_X_plotis = int(input("Formuojame mūšio lauką. Įveskite nelyginį skaičių X ašies pločiui nustatyti: "))
    asies_Y_aukstis = int(input("Įveskite nelyginį skaičių y ašies pločiui nustatyti: "))

    if asies_X_plotis % 2 == 0 or asies_Y_aukstis % 2 == 0:
        print("Bent vienas įvestas skaičius buvo lyginis. Įveskite abu nelyginius.")
    else:
        break
print(f"Mūšio lauko plotas {asies_X_plotis}x{asies_Y_aukstis}.")

tanko_pozicija_x = asies_X_plotis // 2
tanko_pozicija_y = asies_Y_aukstis // 2

tankas = Tankas(tanko_pozicija_x, tanko_pozicija_y, 0, asies_X_plotis, asies_Y_aukstis)  # tankas - objektas, Tankas - šablonas

while True:
    tankas.musio_laukas()
    tankas.info()
    if tankas.ar_zaidimo_pabaiga():
        break
    pasirinkimas = input("w - pirmyn \ns - atgal \na - kairėn \nd - dešinėn \nq - šauti \nesc - išeiti \n")
    match pasirinkimas:
        case "w":
            tankas.pirmyn()
        case "s":
            tankas.atgal()
        case "a":
            tankas.kairen()
        case "d":
            tankas.desinen()
        case "q":
            tankas.suvis()
        case "esc":
            tankas.baigti_zaidima()
