import random

faceCards = {
    1 : "Ace",
    11 : "Jack",
    12 : "Queen",
    13 : "King"
}
   



suits = [
    "Spades","Clubs","Diamonds","Hearts"
]

def Deal():
    card = random.randint(1,13)
    suit = random.randint(0,3)
    cardValue = card
    suitValue = suit
    if card >= 11:
        card = faceCards[card]
        cardValue = 10
    if card == 1:
        card = faceCards[card]
        cardValue = 11
    suit = suits[suit]
    
    FinalCard = {
        "Card Value" : cardValue,
        "Suit Value" : suitValue,
        "Card Name" : card,
        "Suit Name" : suit

    }
    return(FinalCard)

def printCard(card):
    print(str(card["Card Name"])+" of "+str(card["Suit Name"]))

def AddCards(hand):
    Value1 = 0
    Value2 = 0
    for x in hand:
        if x["Card Value"] == 11:
            Value1 = Value1 + x["Card Value"]
            Value2 = Value2 + 1
        else:
            Value1 = Value1 + x["Card Value"]
            Value2 = Value2 + x["Card Value"]
        
    if Value1 == Value2:
        print(Value1)
    else:
        print(str(Value1)+"/"+str(Value2))

card1 = Deal()
card2 = Deal()
printCard(card1)
printCard(card2)

Hand= []
Hand.append(card1)
Hand.append(card2)

AddCards(Hand)


