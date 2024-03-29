import random

ronde = 0
scoresDict = {"1" : 0,
              "2" : 0,
              "3" : 0,
              "4" : 0,
              "5" : 0,
              "6" : 0,
              "three of a kind" : 0,
              "four of a kind" : 0,
              "full house" : 0,
              "small straight" : 0,
              "large straight" : 0,
              "yahtzee" : 0,
              "chance" : 0}
getallen = [1,2,3,4,5,6]
totaal = 0
opnieuwaantal = 1
dobbelList = []
apartList = []

def start():
    spelers = int(input("Met hoeveel spelers wilt u het spel spelen?"))
    if spelers == 1:
        print("Ok, het spel start met 1 speler")
        roll()
    elif spelers > 1:
        print()
    else:
        print("U moet het spel met minimaal 1 speler starten")
        start()

def roll():
    global ronde, dobbelList, apartList
    ronde+=1
    if ronde <= 5 and apartList:
        for x in range(5):
            if x+1 in apartList:
                print(f'dobbelsteen {x+1} is: {dobbelList[x]}')
            else:
                dobbelList[x] = getallen[random.randrange(0,6)]
                print(f'dobbelsteen {x+1} is: {dobbelList[x]}')
        apartList = []
        opnieuwFunc()
    elif ronde <= 5 and not apartList:
        for x in range(5):
            dobbelList.append(getallen[random.randrange(0,6)])
            print(f'dobbelsteen {x+1} is: {dobbelList[x]}')
        apartList = []
        opnieuwFunc()
    else:
        totaalFunc()

def opnieuwFunc():
    global opnieuwaantal,dobbelList
    if opnieuwaantal >= 3:
        keuzeFunc()
    else:
        opnieuw = input("Wilt u nog een keer rollen? (Y/N)").lower()
        if opnieuw == "y":
            opnieuwaantal+=1
            apartFunc()
        elif opnieuw == "n":
            keuzeFunc()
        else:
            print("Only answer with Y or N")
            opnieuwFunc()

def apartFunc():
    global dobbelList,apartList
    apartList = []
    apart = input('Wilt u dobbelstenen apart leggen? (Y/N)').lower()
    if apart == "y":
        while True:
            try:
                apart = input("Welke dobbelstenen wilt u apart leggen? (Geef de dobbelstenen die u apart wilt houden met een komma ertussen; 1,3,4)")
                split = apart.split(",")
                map_object = map(int, split)
                apartList = list(map_object)
                break
            except:
                continue
        print(apartList)
        roll()
    elif apart == "n":
        apartList = []
        roll()
    else:
        print("Only answer with Y or N")
        apartFunc()

def keuzeFunc(dobbelList):
    print("Bovenste vakken: 1,2,3,4,5,6")
    print("Onderste vakken: Three of a kind")
    print("                 Four of a kind")
    print("                 Full house")
    print("                 Small straight")
    print("                 Large straight")
    print("                 Yahtzee")
    print("                 Chance")
    keuze = input("Aan welke combinatie wilt u de score van uw dobbelstenen toevoegen?").lower()
    dobbelList.sort()
    dobbeltotal = dobbelList[0] + dobbelList[1] + dobbelList[2] + dobbelList[3] + dobbelList[4]
    if keuze == "1":
        y = 0
        for x in range(5):
            if dobbelList[x] == 1:
                y+=1
        score1new = scoresDict["1"] + y
        scoresDict.update({"1" : score1new})
        scorebericht(keuze)
    elif keuze == "2":
        y = 0
        for x in range(5):
            if dobbelList[x] == 1:
                y+=2
        score2new = scoresDict["2"] + y
        scoresDict.update({"2" : score2new})
        scorebericht(keuze)
    elif keuze == "3":
        y = 0
        for x in range(5):
            if dobbelList[x] == 1:
                y+=3
        score3new = scoresDict["3"] + y
        scoresDict.update({"3" : score3new})
        scorebericht(keuze)
    elif keuze == "4":
        y = 0
        for x in range(5):
            if dobbelList[x] == 1:
                y+=4
        score4new = scoresDict["4"] + y
        scoresDict.update({"4" : score4new})
        scorebericht(keuze)
    elif keuze == "5":
        y = 0
        for x in range(5):
            if dobbelList[x] == 1:
                y+=5
        score5new = scoresDict["5"] + y
        scoresDict.update({"5" : score5new})
        scorebericht(keuze)
    elif keuze == "6":
        y = 0
        for x in range(5):
            if dobbelList[x] == 1:
                y+=6
        score6new = scoresDict["6"] + y
        scoresDict.update({"6" : score6new})
        scorebericht(keuze)
    elif keuze == "three of a kind":
        if dobbelList[0] == dobbelList[2] or dobbelList[1] == dobbelList[3] or dobbelList[2] == dobbelList[4]:
            toaknew = scoresDict["three of a kind"] + dobbeltotal
        scoresDict.update({"three of a kind" : toaknew})
    elif keuze == "four of a kind":
        if dobbelList[0] == dobbelList[3] or dobbelList[1] == dobbelList[4]:
            foaknew = scoresDict["four of a kind"] + dobbeltotal
        scoresDict.update({"four of a kind" : foaknew})
    elif keuze == "full house":
        if dobbelList[0] == dobbelList[1] and dobbelList[2] == dobbelList[4] or dobbelList[0] == dobbelList[2] and dobbelList[3] == dobbelList[4]:
            fhnew = scoresDict["full house"] + 25
        scoresDict.update({"full house" : fhnew})
    elif keuze == "small straight":
        if dobbelList[0] == dobbelList[3] or dobbelList[1] == dobbelList[4]:
            smallnew = scoresDict["small straight"] + 30
        scoresDict.update({"small straight" : smallnew})
    elif keuze == "large straight":
        if dobbelList[4] == dobbelList[0]+4:
            largenew = scoresDict["large straight"] + 40
        scoresDict.update({"large straight" : largenew})
    elif keuze == "yahtzee":
        if dobbelList[0] == dobbelList[4]:
            yahtzeescore = scoresDict["yahtzee"] + 50
            scoresDict.update({"yahtzee" : yahtzeescore})
        scorebericht(keuze)
    elif keuze == "chance":
        chancescore = scoresDict["chance"] + dobbeltotal
        scoresDict.update({"chance" : chancescore})
        scorebericht(keuze)
    else:
        print("U heeft geen geldige keuze gemaakt, check of u spelfouten heeft gemaakt.")
        keuzeFunc()
    
def scorebericht(keuze):
    print(f"uw score voor {keuze} is: {scoresDict[keuze]}")
    roll()

start()