

def main():
    varsta = input_varsta()

    while True:
        try:
            inaltime = int(input("Introduceți înălțimea (cm): "))
        except ValueError:
            print("Introduceți o valoare validă pentru înălțime.")
            continue
        if 150 <= inaltime <= 220:
            break
        else:
            print("Înălțimea trebuie să fie între 150 și 220 cm.")

    while True:
        sex = input("Introduceți sexul (M sau F): ").upper()
        if sex in ["M", "F"]:
            break
        else:
            print("Sexul trebuie să fie 'M' sau 'F'.")

    while True:
        try:
            greutate = float(input("Introduceți greutatea actuală (kg): "))
            if 45 <= greutate <= 300:
                break
            else:
                print("Greutatea trebuie să fie între 45 kg și 300 kg.")
        except ValueError:
            print("Introduceți o valoare validă pentru greutate.")


    if sex == "M":
        greutate_ideala = inaltime - 100 - ((inaltime - 150) / 4 + (varsta - 20) / 4)
    else:
        greutate_ideala = inaltime - 100 - ((inaltime - 150) / 2.5 + (varsta - 20) / 6)

    print(f"\nGreutatea ideală este: {greutate_ideala:.2f} kg")

    diferenta = greutate - greutate_ideala
    if diferenta > 0:
        print("Recomandare: Ar fi bine să slăbiți puțin.")
    elif diferenta < 0:
        print("Recomandare: Ar fi bine să adăugați puțină greutate.")
    else:
        print("Felicitări! Aveți greutatea ideală.")


def input_varsta():
    while True:
        i = input("Introduceți vârsta (ani): ")
        
        try:
            varsta = int(i)
        except ValueError:
            print("Introduceți o valoare validă pentru vârstă.")
            continue

        if varsta < 20:
            print("Vârsta trebuie să fie între 21 și 119 ani.")
            continue
        
        if varsta > 120:
            print("Vârsta trebuie să fie între 21 și 119 ani.")
            continue

        return varsta
    

main()