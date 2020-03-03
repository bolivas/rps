import random
from os import system, name 

  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  

clear()



names = {1 : "Rock",2 :"Scissors",3:"Paper"}

ties = 0 
wins = 0
loses = 0 


class Action:
    def __init__(self,action,defeats,defeated):
        self.action = names[action]
        self.defeats = names[defeats]
        self.defeated = names[defeated]

        self.txt = "You have selected "+self.action+". "+self.action+" beats "+self.defeats+", and looses to "+self.defeated+"."



# Defines the winnners and loosers
rock = Action(1,2,3)
# print(rock.txt)

paper = Action(2,3,1)
# print(paper.txt)

scissors = Action(3,1,2)
# print(scissors.txt)

objs = {1 : rock,2 :scissors,3:paper}



first = True
x = True
choice = 0
while x:
    print ("Wins: {} ---- Loses: {} ---- Ties: {}".format(wins,loses,ties))

    if first:
        print("\nWelcome")
        print("\nThis is a Rock Paper Scisors game use at your own risk.")
        first = False

    
    
    y = True
    while y:
        choice = input("\nPlease make a selection.(type x to exit)\n\n1: Rock\n2: Paper\n3: Scissors\n")
        if choice in ["1","2","3","x"]:
            break
        clear()    
        print ("Wins: {} ---- Loses: {} ---- Ties: {}\n".format(wins,loses,ties))
        print("\nBad input try again. Valid selection = 1, 2, 3, x\n")
        

    if choice == "x":
        clear()
        print("\n\n\n\n\n\nFinal Score\nWins: {} ---- Loses: {} ---- Ties: {}".format(wins,loses,ties))
        if wins > loses:
            print("You are the ultimate winner.")
        elif wins == loses:
            print("You are tied.")
        else:
            print("you are a loser.")
        keep = input("Keep Playing? y/n:\n")
        if keep in ["y","n"]:
            if keep == "y":
                clear()
                print("\n\n")
                continue
            else:
                break    
        break
    else:
        choice = int(choice)
    clear()

    computer = random.choice((1,2,3))
    print(names[choice] +" VS "+names[computer]+"\n")


   

    if rock.action == names[choice]:
        if rock.defeats == names[computer]:
            print("you win")
            wins+=1
        elif rock.defeated == names[computer]:
            print("you lose")
            loses+=1
        else:
            print('tie')
            ties+=1

    if paper.action == names[choice]:
        if paper.defeats == names[computer]:
            print("you win")
            wins+=1
        elif paper.defeated == names[computer]:
            print("you lose")
            loses+=1
        else:
            print('tie')
            ties+=1

    if scissors.action == names[choice]:
        if paper.defeats == names[computer]:
            print("you win")
            wins+=1
        elif paper.defeated == names[computer]:
            print("you lose")
            loses+=1
        else:
            print('tie')
            ties+=1
print("Goodbye")