#Given an array A and an integer B.
# A pair(i, j) in the array is a good pair if i != j and 
#(A[i] + A[j] == B). Check if any good pair exist or not.

def GoodPair(array,integer1):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            print(1)
            if array[i]+array[j]==integer1:
                return("Good Pair")
    return("Not a Good Pair")




array=[1,2,3,4]
integer1=7

print(GoodPair(array,integer1))