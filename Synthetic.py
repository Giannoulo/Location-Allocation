import random
import time

start = time.time()

s_rest = open("Synthetic_hotels.txt","w")

for i in range (1000000):
    var1 = random.uniform(20, 40)
    var2 = random.uniform(-130, -50)
    line = "%d|%.6f|%.6f\n" % (i+1,var1, var2)
    s_rest.write(line)

s_rest.close()

end = time.time()

print(end - start)