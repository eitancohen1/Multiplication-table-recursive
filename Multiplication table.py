def recMult(i,n):
    if i>n:
        return
    for j in range(1,n+1):
        print(i*j,end="\t")
    print()
    recMult(i+1,n)

n=int(input("enter a number: "))
recMult(1,n)
