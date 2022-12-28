import threading       # a library used in Python specifically for the use of multithreading
import time            # library used to measure run time  


def merge(arr, l, m, r):         # where 'l' is left, 'm' is middle and 'r' is right 
  # helper function to merge two sorted subarrays
  n1 = m - l + 1
  n2 = r - m
  L = [0] * (n1)
  R = [0] * (n2)

  for i in range(0 , n1):
    L[i] = arr[l + i]

  for j in range(0 , n2):
    R[j] = arr[m + 1 + j]

  i = 0
  j = 0
  k = l

  while i < n1 and j < n2:
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1

  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1

  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1

# The merge_sort function in this code is a implementation of the merge sort algorithm. 
# It takes an array arr and two indices l and r that mark the start and end of the portion of the array that needs to be sorted.  
# Each of these threads is started using the start() method and then joined using the join() method after they have completed their task.

def merge_sort(arr, l, r):
    # The function first checks if l is less than r.  If it is, 
    # then it divides the portion of the array between l and r into two halves and creates four threads to sort each half concurrently using the merge_sort function again.
    if l < r:     
        m = (l+(r-1))//2
 
        t1 = threading.Thread(target=merge_sort, args=(arr, l, m))          # Creating threads via threading module
        t2 = threading.Thread(target=merge_sort, args=(arr, m+1, r))
        t3 = threading.Thread(target=merge_sort, args=(arr, m+1, r))
        t4 = threading.Thread(target=merge_sort, args=(arr, m+1, r))
        
        t1.start()
        t2.start()
        t3.start()
        t4.start()
  
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        
        merge(arr, l, m, r)    # Calls the merge function, which takes the sorted subarrays produced by the threads and combines them into a single sorted array.


# The sort function is used to start the sorting process by calling the merge_sort function and passing it the entire array to be sorted, 
# along with the indices marking the start and end of the array. 

def sort(arr):
    l = 0
    r = len(arr) - 1
    
    # The sort function also starts a timer before the sorting begins and stops the timer after the sorting is complete, printing the elapsed time.

    # Start the timer
    start_time = time.time()
    
    merge_sort(arr, l, r)
    
    # End the timer and print the elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time:", elapsed_time)

# test the implementation
size = int(input("Enter the size of the array: "))
arr = []

for i in range(size):
    element = int(input("Enter element {}: ".format(i+1)))
    arr.append(element)

sort(arr)
print("The sorted array becomes: ")
print(arr) # should print the sorted array 

# MAC ADDRESS of my system having 4 cores: 10-C3-7B-6C-DC-8A
import uuid
  
# joins elements of getnode() after each 2 digits.

print ("The MAC address for the current system is : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))