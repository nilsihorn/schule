SIM = "1234"
versuche = 1
fehlversuche = 1
negativefehlversuche = 2
PUK = "12345678"
versuchepuk = 1
fehlversuchepuk = 1
negativefehlversuchepuk = 9


print("Bitte Pin eingeben.")
Eingabe = input()


if Eingabe == SIM:
        print("Willkommen bei O2!")
        versuche = 1
else:
    while versuche < 3:
        if versuche < 3:
            print("Pin falsch!\nBitte Pin erneut eingeben.")
            print(str(fehlversuche) + ". Fehlversuch.\nNoch " + str(negativefehlversuche) + " Versuche.")
            Eingabe = input()
            if Eingabe == SIM:
                print("Willkommen bei O2!")
                versuche = 3
                fehlversuche = 1
            else:
                versuche += 1
                fehlversuche += 1
                negativefehlversuche -= 1

if negativefehlversuche == 0:
    print("Ihr Handy wurde gesperrt.\nBitte geben Sie ihre PUK ein um ihr Handy zu entsperren.")
    EingabePUK = input()
    if EingabePUK == PUK:
        print("Willkommen bei O2!")
    else:
        while versuchepuk < 10:
            if versuchepuk < 10:
                print("PUK falsch!\nBitte erneut eingeben.")
                print(str(fehlversuchepuk) + ". Fehlversuch.\nNoch " + str(negativefehlversuchepuk) + " Versuche.")
                EingabePUK = input()
                if EingabePUK == PUK:
                    print("Willkommen bei O2!\nBitte ändern Sie ihren Pin!")
                    SIM = input()
                    print("Pin geändert!")
                    versuchepuk = 10
                    fehlversuchepuk = 1
                else:
                    versuchepuk += 1
                    fehlversuchepuk += 1
                    negativefehlversuchepuk -= 1

if negativefehlversuchepuk == 0:
    print("Ihre SIM-Karte wurde gesperrt.\nBitte melden Sie sich bei ihrem O2 Kontakt.")