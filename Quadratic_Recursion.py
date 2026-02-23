def quad(n):
    if n <= 1:
        return
    
    for i in range(n):
        print("*", end="")
    print()
    
    quad(n - 1)

n = int(input("Enter number: "))
quad(n)