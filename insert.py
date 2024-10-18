def insert(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1

        while(i > -1 and A[i] > key):
            A[i + 1] = A[i]
            i = i -1

        A[i + 1] = key

def findRange(A):
    range = A[-1] - A[0]
    return range

def findMedian(A):
    if (len(A)%2 == 0):
        meadian = (A[len(A)//2] + A[(A//2)] / 2)
        return meadian

def findSum(A):
    findSum = sum(A)
    return sum(A)

    
A = []
for i in range(9):
    num = int (input("enter number :"))
    A.append(num)

print("befr :",A)
insert(A)
print("After :",A)

print("range is :",findRange(A))
print("Meadian is :",findMedian(A))
print("sum of :",findSum(A))