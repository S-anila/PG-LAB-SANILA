num=int(input("enter the limit"))
for i in range(num):
    for j in range(i):
        print("*",end="")
    print('')
    for i in range(num,0,-1):
        for j in range(i):
            print("*",end="")
        print('')
    