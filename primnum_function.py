def primeNumbers(n,m):    
    for num in range(n,m):
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if prime:
           print num
primeNumbers(0,100)