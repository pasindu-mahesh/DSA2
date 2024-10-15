def func (num):
    if num == 1:
        return 1
    else:
        return func(num -1 ) + num -1
    
while True:
    num = int(input("Enter Number:"))

    if num == -1:
        print("Finished!")
        break

    print("Output:",func(num))