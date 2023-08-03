import random


def clearFile():
    f = open("shoe.txt", "w")
    f.write("")
    f.close()

clearFile()


x = 0
f = open("shoe.txt","a")
while x < 20:
    n = random.randint(1,13)
    n2 = random.randint(1,13)
    card = {
        "num1" : n,
        "num2" : n2
    }
    f.write(str(card)+"\n")
    x = x + 1

print(x)

f.close()