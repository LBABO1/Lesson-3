def prime(x):
    count = 0
    for i in range(1,x+1):
        if x%i == 0:
            count +=1
    
    if count == 2:
        print(True)

    else:
        print(False)


x = int(input("Enter number: \n"))

prime(x)