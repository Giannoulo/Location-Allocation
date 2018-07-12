import numpy as np
from scipy.spatial import cKDTree
import random
from operator import itemgetter
import time


start_time = time.time()

#Create a list with the lat long pairs of each restaurant
rest_points = []

rest = open("rest.txt", "r")

for line in rest:
    
    lat = line.split("|")[3]
    long = line.split("|")[4]

    rest_points.append([lat,long])


#Convert the rest_points list to a numpy array so that it can be used as an input for
#the cKDTree class
restArray = np.asarray(rest_points)
    
    
#Construct the KDTree with the lat long pairs of the restaurants
restTree = cKDTree(restArray,leafsize=1)

#Print the time it took to construct the tree
print("The time spent to construct the KdTree is %s seconds ---" % (time.time() - start_time))

#Get the radius query details
hotelNumber = int(input("How many hotels? "))

r = float(input("What is the radius? "))

start_time = time.time()


#Construct a list with the id, latitude and longtitude of the hotels
hotels = open("hotels.txt", "r")

hotel_points = []

for line in hotels:
    
    ids = line.split("|")[0]
    lat = line.split("|")[4]
    long = line.split("|")[5]
    
    hotel_points.append([ids,lat,long])

    
#Get m random hotels from the list without replacement
mHotels = random.sample(hotel_points, hotelNumber)

   

#Query the KdTree and obtain the number of restaurants in the given radius for the 
#given hotel
scores = []
for i in mHotels:

    #Returns a list with the indices of the restaurants
    idx = restTree.query_ball_point((i[1:]), r)

    #Stores the id of the hotel along with the number of restaurants in the given radius
    scores.append([i[0],len(restArray[idx])])

#Calculate the average score
sum = 0
for i in scores:
    sum = sum + int(i[1])

av = sum/len(scores)
print("The average score is %d" % (av))


#Time to calculate the query    
print("The time spent to answer the radius query is --- %s seconds ---" % (time.time() - start_time))


#Sort the scores list and print
sorted_scores = sorted(scores, key=itemgetter(1))

print(sorted_scores[-10:])