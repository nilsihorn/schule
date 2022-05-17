import sys
PIN = "1234"
versuche = 1
fehlversuche = 1
negativefehlversuche = 2


print("Willkommen bei ihrer Bank.")
print(
    "1  Kontostand abfragen",
    "2  Geldabheben",
    "3  Karte auswerfen",
    sep="\n"
)
choice = int(input("Ihre Wahl?\n"))
if choice == 1:
    Eingabe = input("Bitte geben Sie ihre PIN ein.\n")
    if Eingabe == PIN:
        print("Ihr Kontostand beträgt 1000€.")
        versuche = 1
    else:
        while versuche < 3:
            if versuche < 3:
                print("Pin falsch!\nBitte Pin erneut eingeben.")
                print(str(fehlversuche) + ". Fehlversuch.\nNoch " + str(negativefehlversuche) + " Versuche.")
                Eingabe = input()
                if Eingabe == PIN:
                    print("Ihr Kontostand beträgt 1000€.")
                    versuche = 3
                    fehlversuche = 1
                else:
                    versuche += 1
                    negativefehlversuche -= 1

    if negativefehlversuche == 0:
        print("Ihr Konto wurde gesperrt und ihre Karte wird einbehalten.\n")
elif choice == 2:
    Eingabe = input("Bitte geben Sie ihre PIN ein.\n")
    if Eingabe == PIN:
        Eingabe = input("Wieviel Geld wollen Sie abheben?\n")
        print("Hier sind ihre " + str(Eingabe) + "€.")
    else:
        while versuche < 3:
            if versuche < 3:
                print("Pin falsch!\nBitte Pin erneut eingeben.")
                print(str(fehlversuche) + ". Fehlversuch.\nNoch " + str(negativefehlversuche) + " Versuche.")
                Eingabe = input()
                if Eingabe == PIN:
                    Eingabe = input("Wieviel Geld wollen Sie abheben?\n")
                    print("Hier sind ihre " + str(Eingabe) + "€.")
                    versuche = 3
                    fehlversuche = 1
                else:
                    versuche += 1
                    negativefehlversuche -= 1
elif choice == 3:
    sys.exit(0)
else:
    print("Bitte nur Zahlen zwischen 1 und 3 eingeben!")
