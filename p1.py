notThousandth = True
count = 1
number = 3
print "prime number is ",number
while notThousandth:
    isPrime = True
    for j in range(2,number-1) :
        if number%j == 0:
            isPrime = False
            break
    if isPrime:
        print "prime number is ",number
        count += 1
        
    if count == 1000:
        notThousandth = False
        print "Thousnadth Prime number is:",number
    number+=1
        
