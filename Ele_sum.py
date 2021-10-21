#This problem has been asked in Google Interview.
# Though this is not a optimum solution.
# its Complexity is O(nxn).
array = [1,2,3,4,5,6]

sum = 6
def eleSum(arr,sum):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == sum :
                return print("Yes")
    return print("NOPE")

eleSum(array,sum)

# The given approach is brute force approach.
