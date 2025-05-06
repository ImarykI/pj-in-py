
def get_varsta(ani_umani):
    t = ani_umani - 15
    if (t > 0):
        return get_varsta(t) + t * 3
    if 3 <= ani_umani:
        return get_varsta(2) + (ani_umani - 2) * 4
    if 2 <= ani_umani:
        return get_varsta(1) + 7 
    return 18

def get_varsta_acumulator(v):
    pass

while True:
    raspuns = input("Pisica este mai mică de un an? (Da/Nu): ").lower()
    if raspuns == "da":
        conversie = {
            1: "6 luni",
            2: "10 luni",
            3: "2 ani",
            4: "5 ani",
            5: "8 ani",
            6: "14 ani",
            7: "15 ani",
            8: "16 ani",
            9: "16 ani",
            10: "17 ani",
            11: "17 ani"
        }

        while True:
            try:
                luni = int(input("Introduceți câte luni are pisicul (1-11): "))
                if 1 <= luni <= 11:
                    print(f"În ani omenești, pisicul are: {conversie[luni]}")
                    break
                else:
                    print("Introduceți o valoare între 1 și 11.")
            except ValueError:
                print("Introduceți o valoare numerică validă.")
        break
    elif raspuns == "nu":
        while True:
            varsta_input = input("Introduceți câți ani are pisicul (1-35): ")
            try:
                varsta = int(varsta_input)
            except ValueError:
                print("Introduceți o valoare numerică validă.")
                continue
            if not (1 <= varsta < 35):
                print("Introduceți un număr între 1 și 34.")
                continue

            # recursie
            # conditii + acumulator
            # if varsta == 1:
            #     rezultat = 18
            # elif varsta == 2:
            #     rezultat = 18 + 7
            # elif 3 <= varsta <= 15:
            #     rezultat = 18 + 7 + (varsta - 2) * 4
            # else:
            #     rezultat = 18 + 7 + 13 * 4 + (varsta - 15) * 3

            rezultat = get_varsta(varsta)
            print(f"În ani omenești, pisica are aproximativ {rezultat} ani.")
            break
        break
    else:
        print("Răspuns invalid. Trebuie să răspundeți cu Da/Nu sau Yes/No.")
