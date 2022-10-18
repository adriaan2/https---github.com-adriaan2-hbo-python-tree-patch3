

global x
x=True
def dead():
 print("you are dead")
 
def weapons():

    mountainlist=["SHOTGUN","PICKAXE","BOW","SHOVEL","GRENADE"]
    
def mountains():
    print("in front of you is a giant mountain  you start climbing the mountain ")
    print("the moon is full ") 
    print("you see a wolflike creature approaching ")     
    print("choose fight or standstill and hope to not be noticed")
    Fightorhide=input("")
    if Fightorhide=="fight":
        dead()


def caves():
        print("")



def forest():

   print("")


def town():

   print("test")

def valley():
   print
def castle():
    print()


def mines():
    print


def snowstorm():
    print()


    def desert():
        print()


def checkpoint():
 print()

def weapons():
    global ammo
    ammo=10


def answer_input():
      answer_yes_or_no=input("DO YOU WANT TO ENTER THE GAME\n YES OR NO\n").upper()
      if answer_yes_or_no=="YES":
        name_input=input("WHAT IS YOUR NAME?").upper()
        print("WELCOME",name_input)
        while True:
            user_location = input(
                "WICH LOCATION DO YOU WANT ___FOREST__CAVE__MOUNTAINS__VALLEY__TOWN__CASTLE__DRAGONCITY__MINES__SNOW STORM__DESSER__").upper()
            if user_location == "FOREST":
                while True:
                    input("WEAPONS CHOISE/ SHOTGUN___HANDGUN__BOW__SHOVEL__PICKAXE__")
            elif user_location=="Cave":
                           caves()

            elif user_location=="MOUNTAINS":
                    mountains()

                
answer_input()