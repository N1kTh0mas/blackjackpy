import random
import os

#Blackjackpy by Nik Thomas
#Created 08/2023
#V1 Console Version

#Name Lookup Dict for Console Output
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

#Creates a newShoe (Inilization)
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

#Replaces current shoe (Shoe.txt) with a new shoe that is shuffled
def replaceShoe():
    shoeFile = open("Shoe.txt","w")
    shoeFile.write("")
    blankShoeFile = open("blankShoe.txt","r")
    blankShoeData = blankShoeFile.read()
    for x in blankShoeData:
        shoeFile.write(x)
    shoeFile.close()
    blankShoeFile.close()
    shuffleShoe()
    



#Shuffles Shoe.txt
def shuffleShoe():
    
    #Makes a seed
    s = 0
    strSeed = ""
    while s != 10:
        temp = random.randint(0,9)
        strSeed += str(temp)
        s += 1
    seed = int(strSeed)
    random.seed(seed)
    

    #Shuffle Shoe
    file = open("Shoe.txt", "r")
    rawData = file.read()
    cleanData = rawData.split()
    file.close()
    random.shuffle(cleanData)
    random.shuffle(cleanData)
    random.shuffle(cleanData)
    
    shuffledData = ""
    file = open("Shoe.txt", "w")
    for x in cleanData:
        shuffledData += (x + " ")
        
    file.write(shuffledData)
    file.close()



#Prints a Shoe in console using Name Lookup (args: [str]filename)
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
    file.close()

        


#Checks if Blank Template Shoe Exists
Filetest = os.path.isfile('./blankShoe.txt')
if Filetest == False:
    print("Shoe Created")
    newShoe(4)


#testing
replaceShoe()
printShoe("Shoe.txt")


