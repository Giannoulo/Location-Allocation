import numpy as np
from scipy.spatial import cKDTree
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


n = int(input("How many neighbors? "))
start_time = time.time()


#Construct a list with the id, latitude and longtitude of the hotels
hotels = open("hotels.txt", "r")

hotel_points = []

for line in hotels:
    
    ids = line.split("|")[0]
    lat = line.split("|")[4]
    long = line.split("|")[5]
    
    hotel_points.append([ids,lat,long])




#Query the KdTree and obtain the id of the hotel along with the minimum distance
#of the k nearest neighbors
scores = []
for i in hotel_points:
    
    #Returns two lists d, i. The d list contains the distances of the neighbors
    #and the l list contains the location of the neighbors in the data
    d,l = restTree.query((i[1:]), k = n)
    
    #Stores the id of the hotel along with the mimimum radius in which k neighbors are contained
    scores.append([i[0],max(d)])

#Time to calculate the query    
print("The time spent to answer the kNN query is --- %s seconds ---" % (time.time() - start_time))

#Sort the scores list and print [hotel id, radius]
sorted_scores = sorted(scores, key=itemgetter(1))
print(sorted_scores)