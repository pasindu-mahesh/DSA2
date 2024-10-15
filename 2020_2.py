def sum(n):
    if n == 1:
        return 1
    else:
        return sum (n - 1) + 1
    
while True:
    num = int (input("Enter number"))

    if num == -1:
        print("finished!")
    break

    if num < 0:
        print("Non-negative integer")
    continue

sumofnum = sum(num)
pr
