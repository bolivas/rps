import random
from os import system, name 

names = {1 : "Rock",2 :"Paper",3:"Scissors"}
class Action:
    def __init__(self,action,defeats,defeated):
        self.action = names[action]
        self.defeats = names[defeats]
        self.defeated = names[defeated]

        self.txt = "You have selected "+self.action+". "+self.action+" beats "+self.defeats+", and looses to "+self.defeated+"."

class Score:
    def __init__(self,wins,loses,ties):
        self.wins = wins
        self.loses = loses
        self.ties = ties


score = Score(0,0,0)

# Defines the winnners and loosers
rock = Action(1,2,3)
# print(rock.txt)

paper = Action(2,3,1)
# print(paper.txt)

scissors = Action(3,1,2)
# print(scissors.txt)

objs  = {1 :  rock ,2 : paper ,3: scissors }



first = True
x = True
choice = 0


def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  


def print_score():
    print ("Wins: {} ---- Loses: {} ---- Ties: {}".format(score.wins,score.loses,score.ties))

def print_welcome():
    print("Welcome")
    print("\nThis is a Rock Paper Scisors game use at your own risk.")

def take_selection():
    y = True
    while y:
        choice = input("\nPlease make a selection.\n\n1: Rock\n2: Paper\n3: Scissors\nx: Exit\n")
        if choice in ["1","2","3","x"]:
            return choice
        clear()    
        print_score()
        print("\nBad input try again. Valid selection = 1, 2, 3, x")

def keep_playing():
    
    clear()
    print_score()
    print("\n\n")
    keep = input("Keep Playing? y/n:\n")
    if keep in ["y","n"]:
        if keep == "n":
            clear()
            print_score()
            print("\n\nGoodbye\n")
            exit()  
    return "\n" 


def round(selection):
    outcome = "None"
    choice_obj = objs[selection]
    computer = random.choice((1,2,3))
    

    if choice_obj.action == names[selection]:
        if choice_obj.defeats == names[computer]:
            score.wins += 1
            outcome = "Win"
        elif choice_obj.defeated == names[computer]:
            score.loses += 1
            outcome = "Loss"
        else:
            score.ties += 1
            outcome = "Tie"
    return ("\n"+names[selection] +" VS "+names[computer]+" = "+ outcome)

    
outcome = "\n"
clear()
while x:
    if first:
        print_welcome()
        input("\nPress enter to continue:\n")
        
        first = False

    clear()
    print_score()
    print(outcome)
    choice = take_selection()


    if choice == "x":
       outcome =keep_playing() 
       continue
       
    outcome = round(int(choice))
    



