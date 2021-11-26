while True:
    a = int(input("\nEnter the number for which you want the table: "))
    b = int(input("Enter upto which number you want to multiply:: ".format(a)))
    for i in range(1, b+1):
        print("{} * {} = {}".format(a,i,a*i))