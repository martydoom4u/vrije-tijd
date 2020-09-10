# Boter-kaas-en-eieren

import random

def tekenBord(bord):
    # Deze functie tekent het bord dat aan de functie is doorgegeven

    # "bord" is een lijst met 10 strings die het bord weergeeft (we negeren indexnummer 0)
    print(bord[7] + '|' + bord[8] + '|' + bord[9])
    print('-+-+-')
    print(bord[4] + '|' + bord[5] + '|' + bord[6])
    print('-+-+-')
    print(bord[1] + '|' + bord[2] + '|' + bord[3])

    
def kiesLetter():
    # laat de speler de letter typen die ze willen zijn
    letter = ""
    while not(letter == "X" or letter == "O"):
        print("Wil je X of O zijn?")
        letter = input().upper()

    if letter == "X":
        return["X", "O"]
    else:
        return["O", "X"]

def wieMagEerst():
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "speler"

def nogmaalsSpelen():
    print('Wil je nog een keer spelen? (ja of nee)')
    return input().startswith('j')

def doeZet(bord, letter, zet):
    bord[zet] = letter

def isWinnaar(bo, le):
    return((bo[7] == le and bo[8] == le and bo[9] == le) or  #bovenste rij
           (bo[4] == le and bo[5] == le and bo[6] == le) or  #middelste rij
           (bo[1] == le and bo[2] == le and bo[3] == le) or  #onderste rij
           (bo[7] == le and bo[4] == le and bo[1] == le) or  #verticaal links 
           (bo[8] == le and bo[5] == le and bo[2] == le) or  #verticaal midden
           (bo[9] == le and bo[6] == le and bo[3] == le) or  #verticaal rechts
           (bo[7] == le and bo[5] == le and bo[3] == le) or  #diagonaal
           (bo[9] == le and bo[5] == le and bo[1] == le))    #diagonaal

def haalKopierBord(bord):
    kopieerBord = []

    for i in bord :
        kopieerBord.append(i)

    return kopieerBord

def isRuimteVrij(bord, zet):
    return bord[zet] == " "

def haalSpelerZet(bord):
    zet = " "
    while zet not in '1 2 3 4 5 6 7 8 9'.split() or not isRuimteVrij(bord,int(zet)):
        print('Wat is jouw volgende zet? (1-9)')
        zet = input()
    return int(zet)


def kiesWillekeurigZet(bord, zettenLijst):
    mogelijkzets = []
    for i in zettenLijst:
        if isRuimteVrij(bord, i):
            mogelijkzets.append(i)

    if len(mogelijkzets) != 0:
        return random.choice(mogelijkzets)
    else:
        return None


def haalComputerZet(bord, computerLetter):
    if computerLetter == "X":
        spelerLetter = "0"
    else:
        spelerLetter = "X"

# eerst kijken we of bij de volgende zet we kunnen winnen
    for i in range(1, 10):
        kopie = haalKopierBord(bord)
        if isRuimteVrij(kopie, i):
            doeZet(kopie, computerLetter, i)
            if isWinnaar(kopie, computerLetter):
                return i
# blokkeer de speler
    for i in range(1,10):
        kopie = haalKopierBord(bord)
        if isRuimteVrij(kopie, i):
            doeZet(kopie, spelerLetter, i)
            if isWinnaar(kopie, spelerLetter):
                return i

    zet = kiesWillekeurigZet(bord, [1,3,7,9])
    if zet != None:
        return zet

    if isRuimteVrij(bord, 5):
        return 5

    return kiesWillekeurigZet(bord, [2,4,6,8])

def isBordVol(bord):
    for i in range(1,10):
        if isRuimteVrij(bord, i):
            return False
    return True


print("Welkom bij Boter-kaas-en-eieren")

while True:
    hetBord = [' '] * 10
    spelerLetter, computerLetter = kiesLetter()
    beurt = wieMagEerst()
    print("De" + beurt + "  mag eerst")
    spelBezig = True

    while spelBezig:
        if beurt == "speler":
            tekenBord(hetBord)
            zet = haalSpelerZet(hetBord)
            doeZet(hetBord, spelerLetter, zet)

            if isWinnaar(hetBord, spelerLetter):
                tekenBord(hetBord)
                print("Hoera!!!!! Je hebt gewonnen!!!!")
                spelBezig = False
            else:
                if isBordVol(hetBord):
                    tekenBord(hetBord)
                    print("Het is gelijkspel!!!")
                    break
                else:
                    beurt = "computer"
        else:
            zet = haalComputerZet(hetBord, computerLetter)
            doeZet(hetBord, computerLetter, zet)

            if isWinnaar(hetBord, computerLetter):
                tekenBord(hetBord)
                print("Helaas de computer heeft gewonnen. Volgende keer beter! :( ")
                spelBezig = False
            else:
                if isBordVol(hetBord):
                    tekenBord(hetBord)
                    print("Het is gelijkspel!")
                    break
                else:
                    beurt = "speler"

    if not nogmaalsSpelen():
        break