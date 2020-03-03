from os import system, name 
ties = 0 
wins = 0
loses = 0 


def determine(selection):
    selection_obj = objs[selection]
    if selection_obj.action == names[choice]:
        if rock.defeats == names[computer]:
            print("you win")
            wins+=1
        elif rock.defeated == names[computer]:
            print("you lose")
            loses+=1
        else:
            print('tie')
            ties+=1
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  


def print_score():
    print ("Wins: {} ---- Loses: {} ---- Ties: {}".format(wins,loses,ties))

def print_welcome():
    if first:
        print("\nWelcome")
        print("\nThis is a Rock Paper Scisors game use at your own risk.")
        first = False

def take_selection():
    y = True
    while y:
        choice = input("\nPlease make a selection.(type x to exit)\n\n1: Rock\n2: Paper\n3: Scissors\n")
        if choice in ["1","2","3","x"]:
            break
        clear()    
        print ("Wins: {} ---- Loses: {} ---- Ties: {}\n".format(wins,loses,ties))
        print("\nBad input try again. Valid selection = 1, 2, 3, x\n")