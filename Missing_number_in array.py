# Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

N = int(input("Enter size of array: "))
A = []

for i in range(1,N):
    A.append(int(input()))

for i in range(1, N):
    if(i not in A):
        print(i)
        
        
    
