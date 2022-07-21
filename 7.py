#Write a Python program to simulate a dice (Generate a random no between 1 to 6) using user defined function. The program should keep generating random number until user prompts to stop.
import random
def dice_simu():
    while True:
        print(random.randint(1,6))
        ch=input("Want to try more?()Y/N: ")
        if ch=="N" or ch=="n":
            break
dice_simu()

