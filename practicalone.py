import random
#keep imports to the top
#imports a random number generator

y0 = 50
x0 = 50
y1 = 50
x1 = 50
#variable set up (may as well keep this together)

#random.random generates a random number between 0 to 1
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1


if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1

print (y0, x0)

#random.random generates a random number between 0 to 1
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1


if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1

print (y0, x0)

#random.random generates a random number between 0 to 1
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1


if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1

print (y1, x1)

#random.random generates a random number between 0 to 1
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1


if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1

print (y1, x1)

answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer)
#this is the equation to figure out the distance between points