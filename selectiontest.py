import sys 
A = [64, 25, 12, 22, 11]
A1 = [64, 25, 12, 22]
A2 = [-64, 25, 12]
A3 = []

# Traverse through all array elements 
for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i]

print ("Sorted array 1") 
for i in range(len(A)): 
    print("%d" %A[i]), 
print ("Sorted array 2") 
for i in range(len(A1)): 
    print("%d" %A1[i]),
print ("Sorted array 3") 
for i in range(len(A2)): 
    print("%d" %A2[i]),
print ("Sorted array 4") 
for i in range(len(A3)): 
    print("%d" %A3[i]), 
