versuche = 1
fehlversuche = 1
negativefehlversuche = 2
Kontostand = 1000

def pinrichtig(pin):
    if pin == "1234":
        return True 
    else:
        return False
    
def abbruch(stop):
    if stop == 1:
        return True
    else:
        return False

while abbruch != True:
    
    print("\nWillkommen bei ihrer Bank.")
    print(
        "1  Kontostand abfragen",
        "2  Geldabheben",
        "3  Karte auswerfen",
        sep="\n"
    )
 
    choice = int(input("Ihre Wahl?\n"))
    if choice == 1:
        pin = input("Bitte geben Sie ihre PIN ein.\n")
        if pinrichtig(pin):
            print("Ihr Kontostand beträgt "+str(Kontostand)+"€.")
            versuche = 1
        else:
            while versuche < 3:
                if versuche < 3:
                    print("Pin falsch!\nBitte Pin erneut eingeben.")
                    print(str(fehlversuche) + ". Fehlversuch.\nNoch " + str(negativefehlversuche) + " Versuche.")
                    pin = input()
                    if pinrichtig(pin):
                        print("Ihr Kontostand beträgt "+str(Kontostand)+"€.\n")
                        versuche = 3
                        fehlversuche = 1
                    else:
                        versuche += 1
                        negativefehlversuche -= 1

        if negativefehlversuche == 0:
            print("Ihr Konto wurde gesperrt und ihre Karte wird einbehalten.\n")
    elif choice == 2:
        pin = input("Bitte geben Sie ihre PIN ein.\n")
        if pinrichtig(pin):
            Eingabe = input("Wieviel Geld wollen Sie abheben?\n")
            print("Hier sind ihre " + str(Eingabe) + "€.\nIhr Kontostand beträgt "+str(float(Kontostand)-float(Eingabe))+"€.")
            Kontostand = int(Kontostand) - int(Eingabe)
        else:
            while versuche < 3:
                if versuche < 3:
                    print("Pin falsch!\nBitte Pin erneut eingeben.")
                    print(str(fehlversuche) + ". Fehlversuch.\nNoch " + str(negativefehlversuche) + " Versuche.")
                    pin = input()
                    if pinrichtig(pin):
                        Eingabe = input("Wieviel Geld wollen Sie abheben?\n")
                        print("Hier sind ihre " + str(Eingabe) + "€.\nIhr Kontostand beträgt "+str(float(Kontostand)-float(Eingabe))+"€.")
                        Kontostand = int(Kontostand) - int(Eingabe)
                        versuche = 3
                        fehlversuche = 1
                    else:
                        versuche += 1
                        negativefehlversuche -= 1
    elif choice == 3:
        print("Auf Wiedersehen!")
        abbruch = True
    else:
        print("Bitte nur Zahlen zwischen 1 und 3 eingeben!")