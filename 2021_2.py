def func(num):
    if num == 1:
        return 1
    else:
        return func (num - 1)/2
    
while True:
    num = int(input("Enter Number: "))

    if num == -1:
        print("Finished!")
        break
    else:
        print("Output :",func(num))