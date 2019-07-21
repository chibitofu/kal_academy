import math

#1. Find the element that appears once in a sorted array where all other elements appear twice one after another. Find that element in 0(logn) complexity.
#Input:   arr[] = {1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8}
#Output:  4    

def find_element(input: list):
    #When there's only 1 element left, you have your answer.
    if len(input) == 1:
        return print(input)
    #If an array with even length gets passed through, there are either no singluar elements or more than one singluar elements.
    elif len(input)%2 == 0:
        raise Exception("Invalid array {}".format(input))

    pivot = math.ceil(len(input)/2)
    left_seg = input[:pivot]
    right_seg = input[pivot:]

    #Compares last element of left and first element of right. If equal chop the off and the odd side has the single element.
    if left_seg[-1] == right_seg[0]:
        left_seg = left_seg[:-1]
        right_seg = right_seg[1:]
        #Pass the odd side through the function again.
        if len(left_seg)%2 == 0:
            find_element(right_seg)
        else:
            find_element(left_seg)

    #If left last and right first don't match. Then check left to see if last 2 elements match. If they don't pass left seg though again. If they do pass right seg.
    else:
        if left_seg[-2] == left_seg[-1]:
            find_element(right_seg)
        else:
            find_element(left_seg)

a = [1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]

find_element(a)

#2. A magic index in an array A[0…n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index if one exists, in an array A. FOLLOW UP: What if the values are not distinct?

def magic_index(input: list):
    i = 0
    v = input[i]
    while i != v or i == (len(input) - 1):
        #Magic index not posssible if value is greater than index.)
        if v > i:
            raise Exception("No magic index")
        else:
            i += 1
            v = input[i]
    
    if input[i] == i:
        return print(i)
    else:
        raise Exception("No magic index")

b = [-2,-1,0,3,5,6,9]

magic_index(b)

#3. Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order.

def rotated_number(input: list, element: int):
    if element < input[0]:
        i = -1
        while input[i] != element:
            i -= 1
            if input[i] < element:
                raise Exception("Element not found.")
    else:
        i = 0
        while input[i] != element:
            i += 1
            if input[i] > element:
                raise Exception("Element not found.")
    
    if i < 0:
        i = len(input) + i

    return print("Element found at index {}".format(i))

c = [6,1,2,3,4,5]

rotated_number(c, 4)

#4. Given an array that contains numbers from 1 to n-1 and exactly 1 duplicate, find that duplicate.

def find_dupe(input: list):
    #Has to either be first 2 or last 2 elements.
    if len(input) == 3:
        if input[-1] == input[-2]:
            return print("The duplicate is {}.".format(input[-1]))
        else:
            return print("The duplicate is {}.".format(input[0]))

    pivot = math.ceil(len(input)/2)
    left_seg = input[:pivot]
    right_seg = input[pivot:]

    #If the last element of the left segment is equal to the pivot(index + 1). Then the dupe is in the right segment.
    #pivot = 6
    #index [0,1,2,3,4,5] [6,7,8,9,10,11]
    #input [1,2,3,4,5,6] [7,8,8,9,10,11]
    if left_seg[-1] == right_seg[0]:
        return print("The duplicate is {}.".format(input[-1]))
    elif left_seg[-1] == pivot:
        find_dupe(right_seg)
    else:
        find_dupe(left_seg)

d = [1,2,3,4,5,6,7,8,8,9,10,11]

find_dupe(d)

#5. Search an element in an array where difference between adjacent elements is 1.
#For example: arr[] = {8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3}
#Search for 3 and Output: Found at index 7

def find_adjacent_element(input: list, element: int):
    i = 0
    if input[i] == element:
        return print(i)
    
    #Find min elements between starting element and search element. Increment i to that index. Then repeat till you find the search element.
    while input[i] != element:
        if element < input[0]:
            i += input[i] - element
        else:
            i += element - input[i]

    return print("Element is found at index {}.".format(i))

e = [8,7,6,7,6,5,4,3,2,3,4,3]    

find_adjacent_element(e, 3)

#6. Given an array of numbers, split the array into two where one array contains the sum of n-1 numbers and the other array with all the n-1 elements.
#[4,3,8,15]

def find_sum_of_elements(input: list):
    sum_arr = None
    for i in range(0, len(input)):
        #Compares first and last element to rest of array. Since array cannot be split on first or last element.
        if i == 0:
            sum_arr = sum(input[1:])
            if sum_arr == input[i]:
                return print([input[i]], input[1:])
        elif i == len(input) - 1:
            sum_arr = sum(input[:-1])
            if sum_arr == input[i]:
                return print([input[i]], input[:i])
        else:
            #Splits array on pivot(i). Adds both segments together and compares to pivot element. If not equal moves pivot one index.
            left_seg = input[:i]
            right_seg = input[i+1:]
            sum_arr = sum(left_seg) + sum(right_seg)
            if sum_arr == input[i]:
                return print([input[i]], left_seg + right_seg)
    
    raise Exception("Invalid Array")

f = [4,3,8,15]

find_sum_of_elements(f)

