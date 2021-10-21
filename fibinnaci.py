def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))

    #take input from user
nterms = int(input("how many terms?"))
#check if the number is valid
if nterms <=0:
    print("please enter a positive integer")
else:
    print("Fibinacci sequence:")
    for i in range(nterms):
        print(fibo(i))
