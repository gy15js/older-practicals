#keep imports to the top

import random
#imports a random number generator
import operator
#imported to look at the largest x coordinate instead of y
import matplotlib.pyplot
#imports the plotting graph

num_of_agents = 10
#number of agents

num_of_iterations = 100
#changes number of times coordinates change

agents = []
#this is an empty list
#below is a for loop to create as many agents as we like
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents.append ([random.randint(0,99),random.randint(0,99)])
    #this appends the list, adding the coordinates in without having to make variables first
#because of the use of i here change the agents from [0][0] to [i][0] etc

#random.random generates a random number between 0 to 1
if random.random() < 0.5:
    agents[i][0] = (agents[i][0] + 1) % 100
else:
    agents[i][0] = (agents[i][0] - 1) % 100
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1
#change y0 and x0 to agents [0][0] and agents [0][1]
#%100 is to ensure no points fall off the graph

if random.random() < 0.5:
    agents[i][0] = (agents[i][1] + 1) % 100
else:
    agents[i][0] = (agents[i][1] - 1) % 100
#control flows saying if the random number is below 0.5 either
    #add 1 to it or (else) subtract 1


print (agents)

print (max(agents, key=operator.itemgetter(1)))
#operator.itemgetter gets the second element of the coordinate

'''answer = (((agents [0][0] - agents [1][0])**2) + ((agents [0][1] - agents [1][1])**2))**0.5
print(answer)'''
#this is the equation to figure out the distance between points

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()
#need for for loop here to ensure all 10 agents are included
