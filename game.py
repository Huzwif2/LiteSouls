import guts
import witch
import random


def welcome():
    if input("Would you like to play? (y/n): ") == "y":
        introduction()
    else:
        print("See you next time traveller...")

def restart():
    if input("Would you like to play again? (y/n): ") == "y":
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
    print("Fighting is about choice.\nTo fight is to make a choice. That was what I was told when the neighbouring kingdom finally invaded out homeland. I was told the slaughtering of our people was done for no other reason than to send a message to any neighbouring kings. I watched all of my friends, family and community slaughtered by soldiers while i hid. What a stupid choice. When the dust had settled I came out of my hiding spot. Rumor was the soliders were going to return as our ruler had already been kidnpped, presumed dead.")
    chooseClass()
    

def berserk():
    guts.printstats()
    print("You hear blood curdling screams from the kingdom's entrance. The soldiers have returned. You turn around to run only to be met by three soldiers shouting at you in a foreign language. One sneaks up behind you and hits you over the head, knocking you to the ground. Your head is throbbing from the agonizing pain while staring at the soldiers boots.")
    
    fight1 = input("Surrender (s) or Fight (f)?: ")
    if fight1 == "s":
         print("You toss your sword to the side and raise your hands. At that moment you remember, you never saw any prisoners since the seige stared. The last thing you hear is the swoosh of a sword down into your skull.\n Game Over....")
         restart()
    elif fight1 == "f":
         f1Roll = random.randint(2,12)
         realRoll = f1Roll + guts.gutsSp
         print("You rolled a", f1Roll, "+ added strength points bonus")
         if realRoll <= 3:
              print("You rolled a", realRoll)
              print("Critical loss!")
              print("As you attempt to slash at the soldiers feet you end up cutting your own leg. The last thing you see is the dirt and the blood from your leg. Your sword manages to clip the ankle of all the soldiers close by and onec you get up youre able to finish them off.")
              guts.gutsSp = guts.gutsSp - 2
              print("You lost two strength points!")
              guts.printstats()
         
         elif 4 <= realRoll <= 7:
              print("You rolled a", realRoll)
              print("Loss!")
              print("As you slash at the soldiers feet you miss and the guards boot comes down onto your skull. As its coming down you quickly stab the soliders foot. Another solider manages to slash your back but youre able to retaliate. You take down all the soldiers and live to fight another day")
              guts.gutsSp = guts.gutsSp -1
              print("You lost one strength point!")
              guts.printstats()
        
         elif 8 <= realRoll <= 10:
              print("You rolled a", realRoll)
              print("Win!")
              print("words")
              guts.gutsSp = guts.gutsSp +1
              print("You gain one strength point!")
              guts.printstats()

         elif 11 <= realRoll <= 12:
              print("You rolled a", realRoll)
              print("Critical Win!")
              print("words")
              guts.gutsSp = guts.gutsSp + 2
              print("You gain two strength points!")
              guts.printstats()
    
    
    print("Yapstory2")
    fight2 = input("Surrender (s) or Fight (f)?: ")
    if fight2 == "s":
         print("loser")
         restart()
    elif fight2 == "f":
         f2Roll = random.randint(2,12)
         realRoll2 = f2Roll + guts.gutsSp
         print("You rolled a", f2Roll, "+ added strength points bonus")
         if realRoll2 <= 3:
              print("You rolled a", realRoll2)
              print("Critical loss!")
              print("words")
              guts.gutsSp = guts.gutsSp - 2
              print("You lost two strength points!")
              guts.printstats()
         
         elif 4 <= realRoll2 <= 7:
              print("You rolled a", realRoll2)
              print("Loss!")
              print("words")
              guts.gutsSp = guts.gutsSp -1
              print("You lost one strength point!")
              guts.printstats()
        
         elif 8 <= realRoll2 <= 10:
              print("You rolled a", realRoll2)
              print("Win!")
              print("words")
              guts.gutsSp = guts.gutsSp +1
              print("You gain one strength point!")
              guts.printstats()

         elif 11 <= realRoll2 <= 12:
              print("You rolled a", realRoll2)
              print("Critical Win!")
              print("words")
              guts.gutsSp = guts.gutsSp + 2
              print("You gain two strength points!")
              guts.printstats()

    print("Yapstory3")
    fight3 = input("Surrender (s) or Fight (f)?: ")
    if fight3 == "s":
         print("loser")
         restart()
    elif fight3 == "f":
         f3Roll = random.randint(2,12)
         realRoll3 = f3Roll + guts.gutsSp
         print("You rolled a", f3Roll, "+ added strength points bonus")
         if realRoll3 <= 3:
              print("You rolled a", realRoll3)
              print("Critical loss!")
              print("words")
              guts.gutsSp = guts.gutsSp - 2
              print("You lost two strength points!")
              guts.printstats()
         
         elif 4 <= realRoll3 <= 7:
              print("You rolled a", realRoll3)
              print("Loss!")
              print("words")
              guts.gutsSp = guts.gutsSp -1
              print("You lost one strength point!")
              guts.printstats()
        
         elif 8 <= realRoll3 <= 10:
              print("You rolled a", realRoll3)
              print("Win!")
              print("words")
              guts.gutsSp = guts.gutsSp +1
              print("You gain one strength point!")
              guts.printstats()

         elif 11 <= realRoll3:
              print("You rolled a", realRoll3)
              print("Critical Win!")
              print("words")
              guts.gutsSp = guts.gutsSp + 2
              print("You gain two strength points!")
              guts.printstats()

def magic():
    witch.printstats()
    print("witch story")