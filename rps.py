import random
class RPSObject():
    def __init__(self, name, winsAgainst: tuple, losesTo: tuple):
        self.name = name
        self.winsAgainst = winsAgainst
        self.losesTo = losesTo


rock = RPSObject(name = "rock", winsAgainst = ("scissors"), losesTo = ("paper"))
paper = RPSObject(name = "paper", winsAgainst = ("rock"), losesTo = ("scissors"))
scissors = RPSObject(name = "scissors", winsAgainst = ("paper"), losesTo = ("rock"))

rpschoices = {"rock": rock, "paper": paper, "scissors": scissors}

def findWinner(object1, object2):
    winner = ""
    if object1[0].name in object2[0].losesTo: winner = f"{object1[1]} wins. Opponent's choice was {object2[0].name}."
    elif object1[0].name in object2[0].winsAgainst: winner = f"{object2[1]} wins. Opponent's choice was {object1[0].name}."
    elif object1[0].name == object2[0].name: winner = "Could not declare winner."
    return winner

player_rps = rpschoices[input("Rock, paper, or scissors?\n>\t").lower()]

pc_choice = rpschoices[random.choice(("rock", "paper", "scissors"))]

print(findWinner(object1 = (player_rps, "Player"), object2 = (pc_choice, "PC")))