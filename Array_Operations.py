#Arrays are one of the most commonly-used data structures
#The elements of an array are stored in contiguous memory locations
#Arrays are of two types : Static and Dynamic
#Static arrays have fixed, pre-defined amount of memory that they can use, whereas in dynamic arrays this is flexible
#In Python we only have dynamic arrays

Array = ['a', 'b', 'c', 'd', 'e']
first =Array[0]
last = Array[4]

Array.insert(2, 'y')

Array.remove('y')

Array.count('a')
#Push/Pop
#Push corresponds to pushing or adding an element at the end of the array.
#Similarly, pop corresponds to removing the element at the end of the array.
#Since the index of the end of the array is known, finding it and pushing or popping an element will only require O(1) time
Array.append('s')

Array.reverse()

Array.pop(1)
#popping operation means deleting the last element in the array.

print(Array)
print(first, last)

