import random
import math
from colorama import *
init()
#random characters for decorations
chars = ["#", "@","*","o"]

#measurements
def tree(height):
    width = height * 2
    standwidth = height * 2
    standbottom = str(chr(9620) * 5)
    #print the star
    print(" " * math.ceil(width/2 + 2) + Fore.YELLOW + "★")
    #For the length of the tree print the tree
    for layer in range(1,height):
        #print whitespace and a pineneedle
        print(" " * math.ceil(width/2) + Fore.GREEN + "<", end="")
        #for loop to print random characters with color
        for i in range(layer * 2 + 1):
            randchar = random.choice(chars)
            if randchar == "#":
                print(Fore.GREEN + "#", end="")
            elif randchar == "o":
                print(Fore.CYAN + "o", end="")
            elif randchar == "*":
                print(Fore.RED + "*", end="")
            elif randchar == "@":
                print(Fore.YELLOW + "@", end="")
            else: pass
        #print pineneedles
        print(Fore.GREEN + ">")
        #delete whitespace
        width -= 2
    #print the stand
    print(Fore.BLUE + " " * math.ceil(standwidth/2) + "|" + "  " + "|")
    print(" " * math.ceil(standwidth/2 - 1) + standbottom)

height = input("Tree height: ")
tree(int(height))