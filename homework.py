#Given 2 sorted arrays "a" and "b" merge both arrays into array "a". Array "a" has enough room to fit all elements.
# a = [5,15,20,None,None,None]
# b = [7,10,18]
# expected output [5,7,10,15,18,20]

def merge_array(inputA: list, inputB: list):
    a = inputA
    b = inputB
    pointer = len(b) - 1
    bottomA = -1
    bottomB = -1
    
    while pointer >= 0 and bottomB >= len(b) - len(a):
        if a[pointer] > b[bottomB]:
            a[bottomA] = a[pointer]
            bottomA -= 1
            pointer -= 1
        elif a[pointer] < b[bottomB]:
            a[bottomA] = b[bottomB]
            bottomB -= 1
            bottomA -= 1

    return print(a)

merge_array([5,15,20,None,None,None], [7,10,18])



