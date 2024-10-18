def insertSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1

        while(i > -1 and A[i] > key):
            A[i + 1]= A[i]
            i = i -1

        A[i + 1] = key

def findRange(A):
    range = A[-1] - A[0]
    return range

def findMedian(A):
    if len(A) % 2 == 0:
        median = (A[len(A) // 2] + A[len(A)] // 2 - 1) / 2

    else:
        median = A[len(A) // 2]

    return median

def findSum(A):
    findSum = sum(A)

    return sum(A)

A = []

for i in range(5):
    num = int (input("Enter marks :"))
    A.append(num)

print("Before sort :", A)
insertSort(A)
print("After sort : ",A)


print("Range is :",findRange(A))
print("Median is :",findMedian(A))
print("Sum of Marks :", findSum(A))