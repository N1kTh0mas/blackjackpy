import random
import os

nameLookup = {
    1 : "Ace",
    11 : "Jack",
    12 : "Queen",
    13 : "King",
    20 : "Clubs",
    21 : "Spades",
    22 : "Hearts",
    23 : "Diamonds"
}

def newShoe(deckAmt):
    file = open("blankShoe.txt","w")
    while deckAmt != 0:
        cardValue = 1
        while cardValue != 14:
            suitValue = 20
            while suitValue != 24:    
                file.write(str(cardValue)+"-"+str(suitValue)+" ")
                suitValue += 1
            cardValue += 1
        deckAmt -= 1
    file.close()

def replaceShoe():
    pass

def shuffleShoe():
    pass

def printShoe(filename):
    file = open(filename, "r")
    rawData = file.read()
    cleanData = rawData.split()
    print(cleanData)
    for x in cleanData:
        printout = ""
        cardData = x.split('-')
        if int(cardData[0]) == 1 or int(cardData[0]) >= 11:
            
            printout += str(nameLookup[int(cardData[0])])
        else:
            printout += str(cardData[0])
        
        printout += " of "
        printout += str(nameLookup[int(cardData[1])])
        print(printout)

        


#Checks if Blank Template Shoe Exists
Filetest = os.path.isfile('./blankShoe.txt')
if Filetest == False:
    print("Shoe Created")
    newShoe(4)

printShoe("blankShoe.txt")



