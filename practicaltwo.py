#keep imports to the top
import random
#imports a random number generator
import operator
#imported to look at the largest x coordinate instead of y
import matplotlib.pyplot


agents = []
#this is an empty list
agents.append ([random.randint(0,99),random.randint(0,99)])
#this appends the list, adding the coordinates in without having to make variables first


#random.random generates a random number between 0 to 1
if random.random() < 0.5:
    agents [0][0] += 1
else:
    agents [0][0] -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1
#change y0 and x0 to agents [0][0] and agents [0][1]

if random.random() < 0.5:
    agents [0][1] += 1
else:
    agents [0][1] -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1


#random.random generates a random number between 0 to 1
if random.random() < 0.5:
    agents [0][0] += 1
else:
    agents [0][0] -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1


if random.random() < 0.5:
    agents [0][1] += 1
else:
    agents [0][1] -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1


#variable set up for y1 and x1 -now just added into agents list again
#randint generates a point between the range in the brackets
agents.append ([random.randint(0,99),random.randint(0,99)])


#random.random generates a random number between 0 to 1
if random.random() < 0.5:
    agents [1][0] += 1
else:
    agents [1][0] -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1


if random.random() < 0.5:
    agents [1][1] += 1
else:
    agents [1][1] -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1


#random.random generates a random number between 0 to 1
if random.random() < 0.5:
    agents [1][0] += 1
else:
    agents [1][0] -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1


if random.random() < 0.5:
    agents [1][1] += 1
else:
    agents [1][1] -= 1
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1

print (agents)

print (max(agents, key=operator.itemgetter(1)))
#operator.itemgetter gets the second element of the coordinate

answer = (((agents [0][0] - agents [1][0])**2) + ((agents [0][1] - agents [1][1])**2))**0.5
print(answer)
#this is the equation to figure out the distance between points

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()
