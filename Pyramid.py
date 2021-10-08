def pypart (n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")

#Drivers code
n = 5
pypart(n)