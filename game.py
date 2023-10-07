import guts
import witch
import random

def rollDice():
     diceNum = random.randint(2,12)
     print("You roll two dice and get:", diceNum)

def welcome():
    rollDice()
    if input("Would you like to play? (y/n): ") == "y":
        introduction()
    else:
        print("See you next time traveller...")

def chooseClass():
        userClass = input("I knew I needed to have sometthing to defend myself with if they were to return.\nI find an abandoned house, hoping I can find something to defend myself with. Inside there is a sword on display up on the wall but in the dusty corner I notice a staff with a strange glow around it.\n(Type sword or staff to make your choice)\n")
        if userClass == "sword":
                print("You have chosen Berserker class!")
                berserk()
        elif userClass == "staff":
            print("You have chosen Wizard class!\n")
            magic()
        else:
            print("Type sword OR staff\n")
            chooseClass()

def introduction():
    rollDice()
    print("Fighting is about choice.\nTo fight is to make a choice. That was what I was told when the neighbouring kingdom finally invaded out homeland. I was told the slaughtering of our people was done for no other reason than to send a message to any neighbouring kings. I watched all of my friends, family and community slaughtered by soldiers while i hid. What a stupid choice. When the dust had settled I came out of my hiding spot. Rumor was the soliders were going to return as our ruler had already been kidnpped, presumed dead.")
    chooseClass()
    

def berserk():
    guts.printstats()


def magic():
    witch.printstats()
    print("gatsu story")