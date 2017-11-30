import random
#random characters for decorations
chars = ["0","o","@"," *"]

#measurements
width = 40
standwidth = 40
standbottom = str(chr(9620) * 4)
#print the star
print(" " * round(width/2 + .5) + "★" + " " * round(width/2 + .5))
#For the length of the tree print the tree
for layer in range(1,20):
    #print whitespace and a pineneedle
    print(" " * round(width/2 + .5 - 1) + "<", end="")
    #for loop to print random characters
    for i in range(layer):
        print(random.choice(chars), end="")
        #print pineneedles and whitespace
    print(">" + " " * round(width/2 + .5 - 1))
    #delete whitespace
    width -= 1
#print the stand
print(" " * round(standwidth/2 - 1) + "|" + "  " + "|" + " " * round(standwidth/2 - 3.5))
print(" " * round(standwidth/2 - 2) + standbottom + " " * round(standwidth/2))

