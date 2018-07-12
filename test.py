    
idx1 = [1,2,3,4,5,6]
idx2 = [1,2,3,7,8,0]
idx1.extend(x for x in idx2 if x not in idx1)
print(idx1)