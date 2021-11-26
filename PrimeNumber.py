while True:
    a = input("\nEnter a number: ")
    prime = True
    try:
        a = int(a)
        if ( a == 1 ) or ( a == 0 ):
            print("{} is neither prime nor composite.".format(a))
            continue
        elif a > 2:
            for i in range(2, a):
                if a % i == 0:
                    prime = False
        elif a < -1:
            prime = False
        elif a == 2:
            prime = True
        if prime:
            print("{} is a prime number.".format(a))
        elif not prime:
            print("{} is not a prime number.".format(a))
    except:
        print("Enter a valid input!")