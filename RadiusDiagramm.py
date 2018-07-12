import numpy as np
from scipy.spatial import cKDTree
import random
from operator import itemgetter
import time


start_time = time.time()

#Create a list with the lat long pairs of each restaurant
rest_points = []

rest = open("Synthetic_rest.txt", "r")

for line in rest:
    
    lat = line.split("|")[1]
    long = line.split("|")[2]

    rest_points.append([lat,long])


#Convert the rest_points list to a numpy array so that it can be used as an input for
#the cKDTree class
restArray = np.asarray(rest_points)
    
    
#Construct the KDTree with the lat long pairs of the restaurants
restTree = cKDTree(restArray,leafsize=1)

#Print the time it took to construct the tree
print("The time spent to construct the KdTree is %s seconds ---" % (time.time() - start_time))

r = 0.01
m = 10000

output = open("RadiusHotels.txt","w+")

while m < 1000000:

    
    start_time = time.time()


    #Construct a list with the id, latitude and longtitude of the hotels
    hotels = open("Synthetic_hotels.txt", "r")

    hotel_points = []

    for line in hotels:
        
        ids = line.split("|")[0]
        lat = line.split("|")[1]
        long = line.split("|")[2]
        
        hotel_points.append([ids,lat,long])

        
    #Get m random hotels from the list without replacement
    mHotels = random.sample(hotel_points, m)

    

    #Query the KdTree and obtain the number of restaurants in the given radius for the 
    #given hotel
    scores = []

    for i in mHotels:

        #Returns a list with the indices of the restaurants
        idx = restTree.query_ball_point((i[1:]), r)

        #Stores the id of the hotel along with the number of restaurants in the given radius
        scores.append([i[0],len(restArray[idx])])

    m += 30000
    #Time to calculate the query    
    output.write("%d|%.6f\n" % (m,(time.time() - start_time)))
    

output.close()