import random

def drive():
    choice = random.random()
    if(choice < .002):
        return "1"
    elif(.002 <= choice and choice < .00504):
        return "2"
    elif(.00504 <= choice and choice < .0054):
        return "3"
    elif(.0054 <= choice and choice < .00756):
        return "4"
    elif(.00756 <= choice and choice < .00896):
        return "5"
    elif(.00896 <= choice and choice < .0096):
        second_choice = random.random()
        if(choice <= .5):
            return "6"
        else:
            return "7"
    elif(.0096 <= choice and choice < .01344):
        return "8"
    elif(.01344 <= choice and choice < .0144):
        return "9"
    elif(.0144 <= choice and choice < .024):
        return "10"
    elif(.024 <= choice and choice < .0252):
        return "11"
    elif(.0252 <= choice and choice < .03024):
        return "12"
    elif(.03024 <= choice and choice < .0324):
        second_choice = random.random()
        if(choice <= .5):
            return "13"
        else:
            return "14"
    elif(.0324 <= choice and choice < .0378):
        return "15"
    elif(.0378 <= choice and choice < .04536):
        return "16"
    elif(.04536 <= choice and choice < .0486):
        return "17"
    elif(.0486 <= choice and choice < .063):
        return "18"
    elif(.063 <= choice and choice < .504):
        return "19"
    elif(.504 <= choice and choice < 1):
        return "20"

routes = {
    "1": 26,
    "2": 33,
    "3": 28,
    "4": 34,
    "5": 36,
    "6": 31,
    "7": 32,
    "8": 37,
    "9": 33,
    "10": 32,
    "11": 31,
    "12": 34,
    "13": 29,
    "14": 30,
    "15": 32,
    "16": 35,
    "17": 31,
    "18": 29,
    "19": 28,
    "20": 34
}

for i in range(1,10000):
    print(drive())