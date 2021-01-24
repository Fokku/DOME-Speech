from sense_hat import SenseHat
from time import sleep
from random import randint

S = SenseHat()
S.low_light = True


#Configuring Colors,
def col_random():
    random_red = randint(0,255)
    random_green = randint(0,255)
    random_blue = randint(0,255)
    return(random_red, random_green, random_blue)

X = col_random()
O = (0,0,0)
userInput = "";


#Configuring Numbers,
Num1 = [
    O,O,O,X,X,O,O,O,
    O,O,X,X,X,O,O,O,
    O,O,O,X,X,O,O,O,
    O,O,O,X,X,O,O,O,
    O,O,O,X,X,O,O,O,
    O,O,O,X,X,O,O,O,
    O,O,X,X,X,X,O,O,
    O,X,X,X,X,X,X,O,
    ]

Num2 = [
    O,O,O,X,X,O,O,O,
    O,O,X,X,X,X,O,O,
    O,X,X,O,X,X,O,O,
    O,O,O,O,X,X,O,O,
    O,O,O,X,X,O,O,O,
    O,O,X,X,O,O,O,O,
    O,X,X,X,X,X,X,O,
    O,X,X,X,X,X,X,O,
    ]

Num3 = [
    O,O,X,X,X,X,O,O,
    O,X,X,X,X,X,X,O,
    O,X,O,O,O,X,X,O,
    O,O,O,X,X,X,O,O,
    O,O,O,X,X,X,O,O,
    O,X,O,O,O,X,X,O,
    O,X,X,X,X,X,X,O,
    O,O,X,X,X,X,O,O,
    ]

Num4 = [
    O,O,O,O,X,X,O,O,
    O,O,O,X,X,X,O,O,
    O,O,X,X,X,X,O,O,
    O,X,X,O,X,X,O,O,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    O,O,O,O,X,X,O,O,
    O,O,O,O,X,X,O,O,
    ]

Num5 = [
    O,X,X,X,X,X,X,O,
    O,X,X,X,X,X,X,O,
    O,X,X,O,O,O,O,O,
    O,X,X,X,X,X,O,O,
    O,O,X,X,X,X,X,O,
    O,O,O,O,O,X,X,O,
    O,X,X,X,X,X,X,O,
    O,X,X,X,X,X,O,O,
    ]

Num6 = [
    O,O,X,X,X,X,O,O,
    O,X,X,X,X,X,X,O,
    O,X,X,O,O,O,O,O,
    O,X,X,X,X,X,O,O,
    O,X,X,X,X,X,X,O,
    O,X,X,O,O,X,X,O,
    O,X,X,X,X,X,X,O,
    O,O,X,X,X,X,O,O,
    ]

Num7 = [
    O,X,X,X,X,X,X,O,
    O,X,X,X,X,X,X,O,
    O,O,O,O,O,X,X,O,
    O,O,O,O,X,X,O,O,
    O,O,O,X,X,O,O,O,
    O,O,O,X,X,O,O,O,
    O,O,O,X,X,O,O,O,
    O,O,O,X,X,O,O,O,
    ]

Num8 = [
    O,O,X,X,X,X,O,O,
    O,X,X,X,X,X,X,O,
    O,X,X,O,O,X,X,O,
    O,O,X,X,X,X,O,O,
    O,O,X,X,X,X,O,O,
    O,X,X,O,O,X,X,O,
    O,X,X,X,X,X,X,O,
    O,O,X,X,X,X,O,O,
    ]

Num9 = [
    O,O,X,X,X,X,O,O,
    O,X,X,X,X,X,X,O,
    O,X,X,O,O,X,X,O,
    O,X,X,X,X,X,X,O,
    O,O,X,X,X,X,X,O,
    O,O,O,O,O,X,X,O,
    O,X,X,X,X,X,X,O,
    O,O,X,X,X,X,O,O,
    ]