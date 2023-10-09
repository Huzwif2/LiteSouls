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
    quit()

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
   
    # 1st fight
    while True:
          fight1 = input("Surrender (s) or Fight (f)?: ")
          if fight1 == "s":
               print("You toss your sword to the side and raise your hands. At that moment you remember, you never saw any prisoners since the seige stared. The last thing you hear is the swoosh of a sword down into your skull.\nGame Over....")
               restart()
               break

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
                    print("As you slash at the soldiers feet you miss and the guards boot comes down onto your skull. As its coming down you quickly stab the soliders foot. Another solider manages to slash your back but youre able to retaliate. You take down all the soldiers and live to fight another day.")
                    guts.gutsSp = guts.gutsSp -1
                    print("You lost one strength point!")
                    guts.printstats()
               
               elif 8 <= realRoll <= 10:
                    print("You rolled a", realRoll)
                    print("Win!")
                    print("You slash at the soldiers ankles and stab him as he falls. You get up and manage to kill the other guards in your way and escape without being detected.")
                    guts.gutsSp = guts.gutsSp +1
                    print("You gain one strength point!")
                    guts.printstats()

               elif 11 <= realRoll <= 12:
                    print("You rolled a", realRoll)
                    print("Critical Win!")
                    print("You jump to you feet as if it were nothing dueling solider after soldier beating them cleanly every time. The reinforcement see how many bodies you've accumulated and decide its not worth to even try to face you.")
                    guts.gutsSp = guts.gutsSp + 2
                    print("You gain two strength points!")
                    guts.printstats()
                    break
          break
    
    # 2nd Fight
    while True:
          print("You manage to escape the castle scraping by with just your life. As youre walking the vast emptyness of this harsh winter's day you walk over some thin ice and fall for multiple feet. Once you hit the ground and get up you see a dragon ancient even for this time period staring into your soul.")
          fight2 = input("Pet it (p) or Fight (f)?: ")
          
          if fight2 == "p":
               print("The dragon does not enjoy pets on its scales. Youre squashed in an instant.\nGame Over....")
               restart()
               break
          
          elif fight2 == "f":
               f2Roll = random.randint(2,12)
               realRoll2 = f2Roll + guts.gutsWp
               print("You rolled a", f2Roll, "+ added will power points bonus")
          if realRoll2 <= 3:
               print("You rolled a", realRoll2)
               print("Critical loss!")
               print("You run and climb onto a nearby rock but as youre about to jump off the dragon slashes at your legs leaving a massive gash. You trip and fall, accidentally stabbing it in the eye and winning the fight.")
               guts.gutsWp = guts.gutsWp - 2
               print("You lost two will power points!")
               guts.printstats()
          
          elif 4 <= realRoll2 <= 7:
               print("You rolled a", realRoll2)
               print("Loss!")
               print("You run up onto a nearby boulder ready to jump onto the dragon to attack when all of a sudden you trip on a small rock and plummet down to the bottom of this ice cave. On your way down you insert your sword into the dragons belly. While not stopping your fall this move does kill the dragon.")
               guts.gutsWp = guts.gutsWp -1
               print("You lost one will power point!")
               guts.printstats()
          
          elif 8 <= realRoll2 <= 10:
               print("You rolled a", realRoll2)
               print("Win!")
               print("The dragon slashes its claws in an attempt to squash you. You manage to slice off a chunk of its arm. You make quick work of the dragon after that.")
               guts.gutsWp = guts.gutsWp +1
               print("You gain one will power point!")
               guts.printstats()

          elif 11 <= realRoll2 <= 12:
               print("You rolled a", realRoll2)
               print("Critical Win!")
               print("The dragon is about to slash you until it sees your sick moves and, being the smart dragon it is decides to kill itself as it knows dying to you would be almost certain.")
               guts.gutsWp = guts.gutsWp + 2
               print("You gain two will power points!")
               guts.printstats()
               break
          break
    
    # 3rd fight
    while True:
          print("You decide to walk futher into this undiscovered ice cave as you know you cant go back to your home kingdom anyways. In search of civilization you come across an entire nation of people living underground. After speaking to them they agree to let you live in their town as long as you can protect them from any more threats such as that dragon you killed on your way here.\nYour first task as new protector of the town? Kill the old town protector, to prove you're worthy.")

          fight3 = input("Leave (l) or Accept (a)?: ")

          if fight3 == "l":
               print("You awkwardly try to run away but the old warrior smells your fear and hunts you down and that old man never loses his targets. Your last breaths were spent pondering why you decided to run.")
               restart()
               break

          elif fight3 == "a":
               f3Roll = random.randint(2,12)
               realRoll3 = f3Roll + guts.gutsIq
               print("You rolled a", f3Roll, "+ added IQ points bonus")
               if realRoll3 <= 3:
                    print("You rolled a", realRoll3)
                    print("Critical loss!")
                    print("As you begin your duel it only takes a few hits back and fourth to realize he is on another level compared to you. He's unrelenting not giving you a single opening. Youre so preoccupied with trying to stay alive you slip and fall on a patch of ice. This somehow catches the old geezer so off guard he falls ontop of you and stabs himself with his own sword. He looks at you dissaprovingly as he bleeds out on the icey floor. Your head hurts as you took a pretty rough fall. That mightve shaken up your brain.")
                    guts.gutsIq = guts.gutsIq - 2
                    print("You lost two IQ points!")
                    guts.printstats()
               
               elif 4 <= realRoll3 <= 7:
                    print("You rolled a", realRoll3)
                    print("Loss!")
                    print("The old warrior springs into action as soon as the duel is started. His unrelenting will and strength are no match for your skills. He goes for your head and as a knee jerk reaction you swing upwards randomly. You manage to block the hit (with a side of head trauma) but when you open your eyes again you notice the old geezer's head in two parts infront of you. You'd won by accident.")
                    guts.gutsIq = guts.gutsIq -1
                    print("You lost one IQ point!")
                    guts.printstats()
               
               elif 8 <= realRoll3 <= 10:
                    print("You rolled a", realRoll3)
                    print("Win!")
                    print("The duel begins and you can clearly tell you wont beat him in speed nor strength. Instead you devise a plan to use the enviroment to your advantage. He pushes you back as you block his attacks. Over and over he swings and you block until youre pushed back a few meters. Just where you want him. You skillfully step over a patch of ice and without realizing it the old geezer steps right into it. You finish him off and his final moments are spent in agonizingly cold water. Youve won.")
                    guts.gutsIq = guts.gutsIq +1
                    print("You gain one IQ point!")
                    guts.printstats()

               elif 11 <= realRoll3:
                    print("You rolled a", realRoll3)
                    print("Critical Win!")
                    print("Even before the duel had commenced you knew you were no match for his skill, so before the match you manage to convice him to call off the duel and just agree to work together. After successfully convincing him to work together the townspeople cheer as now they have two powerful guardians protecting their little town.")
                    guts.gutsIq = guts.gutsIq + 2
                    print("You gain two IQ points!")
                    guts.printstats()
                    break
               break
          
    print("Status: Alive but not quite living\nThe end (THANK YOU FOR PLAYING :3)")


# The missile knows where it is at all times. It knows this because it knows where it isn't, by subtracting where it is, from where it isn't, or where it isn't, from where it is, whichever is greater, it obtains a difference, or deviation. The guidance sub-system uses deviations to generate corrective commands to drive the missile from a position where it is, to a position where it isn't, and arriving at a position where it wasn't, it now is. Consequently, the position where it is, is now the position that it wasn't, and it follows that the position where it was, is now the position that it isn't. In the event of the position that it is in is not the position that it wasn't, the system has required a variation. The variation being the difference between where the missile is, and where it wasn't. If variation is considered to be a significant factor, it too, may be corrected by the GEA. However, the missile must also know where it was. The missile guidance computance scenario works as follows: Because a variation has modified some of the information the missile has obtained, it is not sure just where it is, however it is sure where it isn't, within reason, and it knows where it was. It now subracts where it should be, from where it wasn't, or vice versa. By differentiating this from the algebraic sum og where it shouldn't be, and where it was. It is able to obtain a deviation, and a variation, which is called "air"



def magic():
    witch.printstats()
    print("You hear blood curdling screams from the kingdom's entrance. The soldiers have returned. You turn around to run only to be met by three soldiers shouting at you in a foreign language. One sneaks up behind you and hits you over the head, knocking you to the ground. Your head is throbbing from the agonizing pain while staring at the soldiers boots.")
   
    # 1st fight
    while True:
          fight1 = input("Surrender (s) or Fight (f)?: ")
          if fight1 == "s":
               print("You raise your hands up signaling your surrender gripping onto your staff tightly. The soldiers all charge you before you can even test out your new toy.\nGame Over....")
               restart()
               break

          elif fight1 == "f":
               f1Roll = random.randint(2,12)
               realRoll = f1Roll + witch.witchFp
               print("You rolled a", f1Roll, "+ added faith points bonus")
               if realRoll <= 3:
                    print("You rolled a", realRoll)
                    print("Critical loss!")
                    print("As you attempt to slash at the soldiers feet you end up cutting your own leg. The last thing you see is the dirt and the blood from your leg. Your sword manages to clip the ankle of all the soldiers close by and onec you get up youre able to finish them off.")
                    witch.witchFp = witch.witchFp - 2
                    print("You lost two faith points!")
                    witch.printstats()
               
               elif 4 <= realRoll <= 7:
                    print("You rolled a", realRoll)
                    print("Loss!")
                    print("As you slash at the soldiers feet you miss and the guards boot comes down onto your skull. As its coming down you quickly stab the soliders foot. Another solider manages to slash your back but youre able to retaliate. You take down all the soldiers and live to fight another day.")
                    witch.witchFp = witch.witchFp -1
                    print("You lost one faith point!")
                    witch.printstats()
               
               elif 8 <= realRoll <= 10:
                    print("You rolled a", realRoll)
                    print("Win!")
                    print("You slash at the soldiers ankles and stab him as he falls. You get up and manage to kill the other guards in your way and escape without being detected.")
                    witch.witchFp = witch.witchFp +1
                    print("You gain one faith point!")
                    witch.printstats()

               elif 11 <= realRoll <= 12:
                    print("You rolled a", realRoll)
                    print("Critical Win!")
                    print("You jump to you feet as if it were nothing dueling solider after soldier beating them cleanly every time. The reinforcement see how many bodies you've accumulated and decide its not worth to even try to face you.")
                    witch.witchFp = witch.witchFp + 2
                    print("You gain two faith points!")
                    witch.printstats()
                    break
          break
    
    # 2nd Fight
    while True:
          print("You manage to escape the castle scraping by with just your life. As youre walking the vast emptyness of this harsh winter's day you walk over some thin ice and fall for multiple feet. Once you hit the ground and get up you see a dragon ancient even for this time period staring into your soul.")
          fight2 = input("Pet it (p) or Fight (f)?: ")
          
          if fight2 == "p":
               print("The dragon does not enjoy pets on its scales. Youre squashed in an instant.\nGame Over....")
               restart()
               break
          
          elif fight2 == "f":
               f2Roll = random.randint(2,12)
               realRoll2 = f2Roll + guts.gutsWp
               print("You rolled a", f2Roll, "+ added will power points bonus")
          if realRoll2 <= 3:
               print("You rolled a", realRoll2)
               print("Critical loss!")
               print("You run and climb onto a nearby rock but as youre about to jump off the dragon slashes at your legs leaving a massive gash. You trip and fall, accidentally stabbing it in the eye and winning the fight.")
               guts.gutsWp = guts.gutsWp - 2
               print("You lost two will power points!")
               witch.printstats()
          
          elif 4 <= realRoll2 <= 7:
               print("You rolled a", realRoll2)
               print("Loss!")
               print("You run up onto a nearby boulder ready to jump onto the dragon to attack when all of a sudden you trip on a small rock and plummet down to the bottom of this ice cave. On your way down you insert your sword into the dragons belly. While not stopping your fall this move does kill the dragon.")
               guts.gutsWp = guts.gutsWp -1
               print("You lost one will power point!")
               witch.printstats()
          
          elif 8 <= realRoll2 <= 10:
               print("You rolled a", realRoll2)
               print("Win!")
               print("The dragon slashes its claws in an attempt to squash you. You manage to slice off a chunk of its arm. You make quick work of the dragon after that.")
               guts.gutsWp = guts.gutsWp +1
               print("You gain one will power point!")
               witch.printstats()

          elif 11 <= realRoll2 <= 12:
               print("You rolled a", realRoll2)
               print("Critical Win!")
               print("The dragon is about to slash you until it sees your sick moves and, being the smart dragon it is decides to kill itself as it knows dying to you would be almost certain.")
               guts.gutsWp = guts.gutsWp + 2
               print("You gain two will power points!")
               witch.printstats()
               break
          break
    
    # 3rd fight
    while True:
          print("You decide to walk futher into this undiscovered ice cave as you know you cant go back to your home kingdom anyways. In search of civilization you come across an entire nation of people living underground. After speaking to them they agree to let you live in their town as long as you can protect them from any more threats such as that dragon you killed on your way here.\nYour first task as new protector of the town? Kill the old town protector, to prove you're worthy.")

          fight3 = input("Leave (l) or Accept (a)?: ")

          if fight3 == "l":
               print("You awkwardly try to run away but the old warrior smells your fear and hunts you down and that old man never loses his targets. Your last breaths were spent pondering why you decided to run.")
               restart()
               break

          elif fight3 == "a":
               f3Roll = random.randint(2,12)
               realRoll3 = f3Roll + guts.gutsIq
               print("You rolled a", f3Roll, "+ added IQ points bonus")
               if realRoll3 <= 3:
                    print("You rolled a", realRoll3)
                    print("Critical loss!")
                    print("As you begin your duel it only takes a few hits back and fourth to realize he is on another level compared to you. He's unrelenting not giving you a single opening. Youre so preoccupied with trying to stay alive you slip and fall on a patch of ice. This somehow catches the old geezer so off guard he falls ontop of you and stabs himself with his own sword. He looks at you dissaprovingly as he bleeds out on the icey floor. Your head hurts as you took a pretty rough fall. That mightve shaken up your brain.")
                    guts.gutsIq = guts.gutsIq - 2
                    print("You lost two IQ points!")
                    witch.printstats()
               
               elif 4 <= realRoll3 <= 7:
                    print("You rolled a", realRoll3)
                    print("Loss!")
                    print("The old warrior springs into action as soon as the duel is started. His unrelenting will and strength are no match for your skills. He goes for your head and as a knee jerk reaction you swing upwards randomly. You manage to block the hit (with a side of head trauma) but when you open your eyes again you notice the old geezer's head in two parts infront of you. You'd won by accident.")
                    guts.gutsIq = guts.gutsIq -1
                    print("You lost one IQ point!")
                    witch.printstats()
               
               elif 8 <= realRoll3 <= 10:
                    print("You rolled a", realRoll3)
                    print("Win!")
                    print("The duel begins and you can clearly tell you wont beat him in speed nor strength. Instead you devise a plan to use the enviroment to your advantage. He pushes you back as you block his attacks. Over and over he swings and you block until youre pushed back a few meters. Just where you want him. You skillfully step over a patch of ice and without realizing it the old geezer steps right into it. You finish him off and his final moments are spent in agonizingly cold water. Youve won.")
                    guts.gutsIq = guts.gutsIq +1
                    print("You gain one IQ point!")
                    witch.printstats()

               elif 11 <= realRoll3:
                    print("You rolled a", realRoll3)
                    print("Critical Win!")
                    print("Even before the duel had commenced you knew you were no match for his skill, so before the match you manage to convice him to call off the duel and just agree to work together. After successfully convincing him to work together the townspeople cheer as now they have two powerful guardians protecting their little town.")
                    guts.gutsIq = guts.gutsIq + 2
                    print("You gain two IQ points!")
                    witch.printstats()
                    break
               break
          
    print("Status: Alive but not quite living\nThe end (THANK YOU FOR PLAYING :3)")