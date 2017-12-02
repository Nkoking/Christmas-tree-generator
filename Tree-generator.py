import random
import math
#random characters for decorations
chars = ["#", "@","*"]

#measurements
def tree(height):
    width = height * 2
    standwidth = height * 2
    standbottom = str(chr(9620) * 5)
    #print the star
    print(" " * math.ceil(width/2 + 2) + "★" + " " * round(width/2 + .5))
    #For the length of the tree print the tree
    for layer in range(1,height):
        #print whitespace and a pineneedle
        print(" " * math.ceil(width/2) + "<", end="")
        #for loop to print random characters
        for i in range(layer * 2 + 1):
            print(random.choice(chars), end="")
        #print pineneedles
        print(">")
        #delete whitespace
        width -= 2
    #print the stand
    print(" " * math.ceil(standwidth/2) + "|" + "  " + "|")
    print(" " * math.ceil(standwidth/2 - 1) + standbottom)

height = input("Tree height: ")
tree(int(height))