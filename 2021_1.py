def func(num):
    if num == 1:
        return 1
    else:
        return num + (func(num -1))

while True: 
    num = int(input("Entre numbers :"))

    if num == -1:
        print("Finished!")
        break

    else:
        
        print("output : ",func(num))