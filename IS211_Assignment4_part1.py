#IS211_Assignment4 Part 1 - Search

import random 
import time 

#this is a function for generating random numbers using the 'random' library
def generate_random(list_size):
    first_list = []
    for i in range(list_size):
        number = random.randint(0,list_size)
        first_list.append(number)

    return first_list
    
#here we are creating a function for sequential_search
def sequential_search(first_list):
    pos = 0 #initializing the # count to 0
    found = False

    while pos < len(first_list) and not found:
#here we are searching for -1 element since we are doing a worst case analysis, we should search for an element we know.
        if first_list[pos] == -1:
            found = True
        else:
            pos = pos + 1
    return found

#Function performs the ordered sequential search.  List is sorted.
def ordered_sequential_search(first_list):
    pos = 0
    found = False
    stop = False

    while pos < len(first_list) and not found and not stop:
        if first_list[pos] == -1:
            found = True

        elif first_list[pos] > -1:
            stop = True
        else:
            pos = pos + 1
    return found

#Function performs the iterative binary search.  List is sorted.
def binary_search_iterative(first_list):
    first = 0
    last = len(first_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if first_list[midpoint] == -1:
            found = True
        elif -1 < first_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return found

#Function performs the recursive binary search.  List is sorted.
def binary_search_recursive(first_list):
    if len(first_list) == 0:
        return False
    else:
        midpoint = len(first_list) // 2
    if first_list[midpoint] == -1:
        return True
    elif -1 < first_list[midpoint]:
        return binary_search_recursive(first_list[:midpoint])
    else:
        return binary_search_recursive(first_list[midpoint + 1:])

if __name__ == "__main__":
#this is the main function of this program to calculate long each function should take on average. 
    list_sizes = [500, 1000, 10000] #creating an array 

#this is the algorithm for sequential_search to sort the list 
# we use the same algorithm for each 4 functions
    total_time = 0
    for list_size in list_sizes:
        for i in range(100): #generating 100 seperate list 
            first_list = generate_random(list_size)
            start = time.time()
            sequential_search(first_list)
            end = time.time()
            sorted_time = end - start
            total_time += sorted_time
            avg_time = total_time / 100 #Totals are then divided by 100 for the avg.
        print(f"Sequential Search took {avg_time:0.8f} in list sizes {list_size}.")
    print("\n")

#ordered_sequential_search
    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            first_list = generate_random(list_size)
            start = time.time()
            ordered_sequential_search(sorted(first_list))
            end = time.time()
            sorted_time = end - start
            total_time += sorted_time
            avg_time = total_time / 100
        print(f"Ordered Sequential Search took {avg_time:0.8f} in list sizes {list_size}.")
    print("\n")
    
# binary_search_iterative
    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            first_list = generate_random(list_size)
            start = time.time()
            binary_search_iterative(sorted(first_list))
            end = time.time()
            sorted_time = end - start
            total_time += sorted_time
            avg_time = total_time / 100
        print(f"Binary Search Iterative took {avg_time:0.8f} in list sizes {list_size}.")
    print("\n")
#binary_search_recursive
    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            first_list = generate_random(list_size)
            start = time.time()
            binary_search_recursive(sorted(first_list))
            end = time.time()
            sorted_time = end - start
            total_time += sorted_time
            avg_time = total_time / 100
        print(f"Binary Search Recursive took {avg_time:0.8f} in list sizes {list_size}.")
        
        #end of the code