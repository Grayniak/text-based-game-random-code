from main import ans
from main import BRpocket
from main import BLpocket
from main import FRpocket
from main import FLpocket
while ("inv" in ans):
  global FRpocket
  global BLpocket
  global FLpocket
  global ans
  while (ans == "inv"):
    if not (ans == "close"):
      print("\nBack Right Pocket = " + BRpocket + "\nBack Left Pocket = " + BLpocket + "\nFront Left Pocket = " + FLpocket + "\nFront Right Pocket = " + FRpocket)
      ans = input('When you want to close the inventory type "close" to go back to the game.\n\n')