def totalflips(number1,number2):
    flips = 0
    while(number1>1 or number2>0):
        t1 = (number1&1)
        t2 = (number2&1)
        if(t2 != t1):
            number1>>=1
            number2>>=1
    return flips
number1 =int(input("Enter your first number: "))
number2 =int(input("Enter your second number: "))
totalflips()