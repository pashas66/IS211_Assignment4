#IS211_Assignment4 Part 2 - Sort

import time
import random

#Functon for Insertion Sort
def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        #here we are searching for -1 element since we are doing a worst case analysis, we should search for an element we know.
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    return  time.time()-start #a_list

#Functon for shell Sort
def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
      
        sublist_count = sublist_count // 2
    return time.time()-start

#Helper Function for Shell Sort
def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value
        
#Wrapper functon for python Sort
def python_sort(a_list):
    start = time.time()
    a_list.sort()
    return time.time() - start

#this is a function for generating random numbers using the 'random' library
def generate_random(list_size):
    first_list = []
    for i in range(list_size):
        first_list.append(random.randint(1, list_size))
    return first_list

#this is the main function of this program to calculate long each function should take on average. 
#Main function creates 100 lists of each size and passes it to sort functions. Totals are then divided by 100 for the # avg.
#it cannot sort 10000 not possible because the algorithm is slow
def main():
    for item in [500,1000,10000]:  #creating an array 
        insr_sort = 0.0
        shl_sort = 0.0
        py_sort = 0.0    
        for i in range(0,100):            
            a_list=[]
            for i in range(1,item):
                a_list.append(random.randint(1,100))
            insr_sort += insertion_sort(a_list)
            shl_sort += shell_sort(a_list)
            py_sort += python_sort(a_list)
        print("For "+str(item)+" Size :")            
        print("Insertion Sort took %10.8f seconds to run, on average" % (insr_sort/100)) #Totals are then divided by 100 for the avg.
        print("Shell Sort took %10.8f seconds to run, on average" % (shl_sort/100)) 
        print("Python Sort took %10.8f seconds to run, on average" % (py_sort/100)) 


if __name__ == "__main__":
    main()

#end of the code