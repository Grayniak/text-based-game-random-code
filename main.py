#if (ans == ""):
import os
import time
import random
where = dict = {1: '1', 2: '0'}
ans = "0" #answer for all imputs
dresrv = "0" #Dresser story switch
deskv = "0" #Desk story switch
radiov = "0" #Radio story switch
doorv = "0" #Door story switch
BRpocket = "empty" #Back Right pocket occupancy
FRpocket = "empty" #Front Right pocket occupancy
FLpocket = "empty" #Front Left pocket occupancy
BLpocket = "empty" #Back Left pocket occupancy
invans = "0" #Var to close inv
GetNewsp = "0" #Has newspaper been taken
splinterIn = "0" #Has splinter been given
dresrlock = "0" #Has dresser button been pressed
def inv():
  global FRpocket
  global BLpocket
  global FLpocket
  global ans
  while (ans == "inv"):
    if not (ans == "close"):
      print("\nBack Right Pocket = " + BRpocket + "\nBack Left Pocket = " + BLpocket + "\nFront Left Pocket = " + FLpocket + "\nFront Right Pocket = " + FRpocket)
      ans = input('When you want to close the inventory type "close" to go back to the game.\n\n')

def dresser():
  global dresrv
  global where
  global splinterIn
  global ans
  where[1] = "2"
  where[2] = "0"
  if (dresrv == "0"):
    print("\nYou walk over to the dresser. It looks like it was made in the 1950's and it has an aged cream color. It has 7 drawers in it, the top being the smallest. You touch the drawer, admiring its antiquity, and as you were running your hand along the side you get a splinter. Now it hurts to touch anything.")
    splinterIn = "yes"
    dresrv = "1"
    ans = input("\nWhat do you do?\n1. Try to get the splinter out\n2. Walk elsewhere\n3. Sit back down in the chair you awakened in\n4. Stay and keep admiring the dresser\n\n")
  else:
    ans = input("What do you do?\n1. Walk elsewhere\n2. Stay and keep admiring the dresser\n3. Try to open the drawers\n")
  if (splinterIn == "yes"):
    if ("set" and "splinter" or "take" and "splinter" in ans):
      chance = (random.randint(1,100))
      if (chance <= 20):
        print("You tried to get the splinter out with your teeth, but you only got half of it out, the other half is still in your finger. It still hurts.")
      else:
        print("Using your teeth and fingers, you got the splinter out. It no longer hurts.")
        splinterIn = "no"
    ans = input("What do you do?\n1. Walk elsewhere\n2. Stay and keep admiring the dresser\n3. Try to open the drawers\n")
    if (ans == "1"): #walk elsewhere
      ans == input("Where do you go?\n1. Desk\n2. Chair\n3. Radio\n4. Door\n")
      if (ans == "1"): #desk
        desk()
      if (ans == "2"): #chair
        chair()
      if (ans == "3"): #radio
        radio()
      if (ans == "4"): #door
        door()
    if (ans == "2"):
    
      
      print("You continue to admire the dresser and note the distressed wood appears old. It's dull, rough surface appears ready and able to dole out splinters galore. You run your hand along the top, being careful to avoid another splinter. As you examine this side you notice a small circle carved into the wood. As you finger the circle, tracing it, trying to determine how deep the cut is, you press on the cork and realize it allows you to depress it slightly, as if it is an intenionally placed button. You press on it some more, although it wont budge.")
      if (dresrlock == "0"):
        ans = input("\nWhat do you do?\n1. try the drawers\n2. Keep inspecting the dresser\n3. Investigate the circle in the wood")
      else:
        ans = input("\nWhat do you do?\n1. try the drawers\n2. Keep inspecting the dresser\n")
      if (ans == "1"):
        ans = input("\nWhich Drawer?\n1. Drawer 1\n2. Drawer 2\n3.Drawer 3\n4. Drawer 4\n5. Drawer 5\n6.Drawer 6\n7.Drawer 7\n8. Nevermind")
        if (ans == "1"):
          print("You open the top drawer and find nothing but socks and underwear in it.")
          ans == input("\nWhat do you do?\n1. Rifle through the clothes\n2. Take a pair of socks\n3. Take some underwear\n4. check other drawers.")
          if (ans == ""):
            print("Hooray")
        if (ans == "2"):
          print("Hooray")
        if (ans == "3"):
          print("Hooray")
        if (ans == "4"):
          print("Hooray")
        if (ans == "5"):
          print("Hooray")
        if (ans == "6"):
          print("Hooray")
        if (ans == "7"):
          print("Hooray")
        if (ans == "8"):
          print("Hooray")
      if (ans == "2"):
        print("\nYou wonder if there are anymore secrets to this dresser. In this state of curiosity, you reach around all other sides of it, alas, you find nothing.")
      if (dresrlock == "1"):
        if (ans == "4"):
          print("You further investigate the mysterious circle in the wood, feeling around it. You squat down to ge a better look at it, and notice that you can see behind the circle by looking into the incision.")
          input("\nWhat do you do?\n1. Leave it alone\n2. Try to push the circle through")
          if (ans == "1"):
            print("You decide that this isnt important enough to waste your time. You need to get out of this place, not mess with tiny shapes.")
            
  else:
    print("bob")
    print(ans)

def desk():
  global GetNewsp
  global where
  where = "desk"
  print(where)
  if  (deskv == "0"):
    print("You walk over to the desk and notice it has 3 drawers on the right. It has nothing on it but some papers and a lamp. Overall it seems rather boring.\nWhat do you do?")
    ans = input("\nWhat do you do?\n1. Inspect the papers\n2. Inspect the lamp\n3. Inspect the drawers\n4. Go elsewhere\n\n")
  if (ans == "1"): #inspect papers
    print('\nYou pick up the papers, all three of them being newspapers. You realize that you dont know what year it is, or even who you are for that matter. The newspapers all have different years on them. 1957 and 1974, the third magazines date has been blacked out. They are all on a page specifying a missing person, "Richard Evans missing, last seen April 12, 1957" You check the next paper: "Henry Mitchells missing, last seen April 15, 1974". As you go to the last paper, you notice that any information regarding this missing person has a black box over it. The picture of the person has also been ripped out of the page.')
    if (GetNewsp == "0"):
      ans = input("\nWhat do you do?\n1. Rip out the pieces of information about the missing people\n2. Inspect other part of the desk\n3. Go elsewhere\n\n")
    else:
      ans = input("\nWhat do you do?\n1. Inspect other part of the desk\n2. Go elsewhere\n")
      if (ans == "1"):
        print("\nYou decide you want to explore the rest of the desk.")
        input("\nWhat do you want to do?\n1. Check the drawers\n2. Check the lamp\n3. Go elsewhere")
        if (ans == "1"): #check the drawers
          print("\nYou bend down to reach the drawers, and you notice that the middle drawer has a lock on it. The other two seem to be unlocked.")
          input("\nWhat do you do?\n1. Try the top drawer\n2. Try the middle drawer\n3. Try the bottom drawer.\n4. Further inspect the drawers\n5. Nevermind")
          if (ans == "1"):
            print('You open the top drawer. Inside are a few magazines. "Cosmopolitan", "Life", and "American Rifleman" You seem to vaguely recognize the last magazine, but dont remember where or when you saw it.')
          if (ans == "2"):
            print("hooray")
          if (ans == "3"):
            print("hooray")
          if (ans == "4"):
            print("hooray")
          if (ans == "5"):
            print("hooray")
        if (ans == "2"): #check the lamp
          print("hooray")
        if (ans == "3"): #go elsewhere
          ans = input("\nWhere to?\n1. The chair\n2. The dresser\n3. The radio\n4. The door\n5. Nevermind")
          if (ans == "1"):
            chair()
          if (ans == "2"):
            dresser()
          if (ans == "3"):
            radio()
          if (ans == "4"):
            door()
          if (ans == "5"):
            print("hooray")
    if (ans == "1"):
      if (GetNewsp == "0"):
        print("You carefully tear out the intact missing person sections out of the two newspapers.")
        input("\nWhat pocket do you want to put this in?\n1. Front right\n2. Front left\n3. Back right\n4. Back left\n5. Nevermind")
        if (ans == "1"):
          FRpocket = "Missing persons paper"
          GetNewsp = "1"
        if (ans == "2"):
          FLpocket = "Missing persons paper"
          GetNewsp = "1"
        if (ans == "3"):
          BRpocket = "Missing persons paper"
          GetNewsp = "1"
        if (ans == "4"):
          BLpocket = "Missing persons paper"
          GetNewsp = "1"
        if (ans == "5"):
          ans = input("\nWhere to?\n1. The chair\n2. The dresser\n3. The radio\n4. The door")
        print("\nNow what?\n1. Inspect lamp\n2. ")

def chair():
  print("hooray")
def radio():
  global radiov
  if (radiov == "0"):
    print("radio")

def door():
  global doorv
  if (doorv == "0"):
    print("yippee")

def elsewhere():
  global ans
  if (where == "dresser"):
    ans = input("\nWhere to\n1. The chair\n2. The desk\n3. The radio\n4. The door\n5. Nevermind?")
    if (ans == "1"):
      chair()
    if (ans == "2"):
      desk()
    if (ans == "3"):
      radio()
    if (ans == "4"):
      door()
    if (ans == "5"):
      print("hooray")
  if (where == "desk"):
    ans = input("\nWhere to\n1. The chair\n2. The dresser\n3. The radio\n4. The door\n5. Nevermind?")
    if (ans == "1"):
      chair()
    if (ans == "2"):
      dresser()
    if (ans == "3"):
      radio()
    if (ans == "4"):
      door()
    if (ans == "5"):
      print("hooray")
  if (where == "radio"):
    ans = input("\nWhere to\n1. The chair\n2. The desk\n3. The dresser\n4. The door\n5. Nevermind?")
    if (ans == "1"):
      chair()
    if (ans == "2"):
      desk()
    if (ans == "3"):
      dresser()
    if (ans == "4"):
      door()
    if (ans == "5"):
      print("hooray")
  if (where == "chair"):
    ans = input("\nWhere to\n1. The dresser\n2. The desk\n3. The dresser\n4. The door\n5. Nevermind?")
    if (ans == "1"):
      dresser()
    if (ans == "2"):
      desk()
    if (ans == "3"):
      dresser()
    if (ans == "4"):
      door()
    if (ans == "5"):
      print ("hooray")
  if (where == "door"):
    ans = input("\nWhere to\n1. The chair\n2. The desk\n3. The dresser\n4. The dresser\n5. Nevermind?")
    if (ans == "1"):
      chair()
    if (ans == "2"):
      desk()
    if (ans == "3"):
      dresser()
    if (ans == "4"):
      dresser()
    if (ans == "5"):
      print("hooray")
def Startup():
  if (where[1] == "1" and where[2] == "0"):
    print("You wake up in an empty room. Upon looking around, you see that the room is filled with nothing but a dresser, a desk, a broken radio, and door with a pattern that seems to change every time you look away from it.")
  else:
    print("m")
Startup()
ans = input("\nWhat do you do?\n")
if ("go" and "dresser" in ans):
  dresser()
if ("go" and "desk" in ans):
  desk()
if ("go" and "radio" in ans):
  radio()
if ("go" and "door" in ans):
  door()
