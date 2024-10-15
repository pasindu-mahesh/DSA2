def func (M,n):
    if n == 1:
        return M
    else:
        return M + func(M,n-1)
    
while True:
    M = int(input("Enter value 1:"))
    n = int(input("Enter value 2:"))

    if M == -1 or n == -1:
        print("Finished!")
        break

    output = func (M,n)
    print("output:",output)
