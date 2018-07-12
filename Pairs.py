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

#Print the time it took to construct the restaurant tree
print("The time spent to construct the restaurant KdTree is %s seconds ---" % (time.time() - start_time))

start_time = time.time()


#Construct a list with the id and a list with the latitude and longtitude of the hotels
hotels = open("hotels.txt", "r")

hotel_points = []
hotel_ids = []

for line in hotels:
    
    ids = line.split("|")[0]
    lat = line.split("|")[4]
    long = line.split("|")[5]
    
    hotel_points.append([lat,long])
    hotel_ids.append(ids)
    
hotelArray = np.asarray(hotel_points)

#Construct the KDTree for the hotels
hotelTree = cKDTree(hotelArray,leafsize=1)


#Print the time it took to construct the hotel tree
print("The time spent to construct the hotel KdTree is %s seconds ---" % (time.time() - start_time))

#Get the radius
k = float(input("What is the radius? "))

start_time = time.time()

#The pairs of the hotels that are less than 2r distance apart
pairs = hotelTree.query_pairs(r=(2*k),output_type ='ndarray')

print("The time spent to query the hotel tree for pairs is %s seconds ---" % (time.time() - start_time))



start_time = time.time()


pair_score = []
score= []

for i in pairs:

    #Returns a list with the indices of the restaurants
    idx1 = restTree.query_ball_point((hotel_points[i[0]]), k)
    idx2 = restTree.query_ball_point((hotel_points[i[1]]), k)
    
    
    idx1.extend(x for x in idx2 if x not in idx1)

    #Stores the id of the hotel along with the number of restaurants in the given radius
    pair_score.append([hotel_ids[i[0]],hotel_ids[i[1]],len(idx1)])




#Time to calculate the query    
print("The time spent to answer the combination query is --- %s seconds ---" % (time.time() - start_time))

#Sort the pair_score list and print
print(sorted(pair_score, key=itemgetter(2))[-10:])