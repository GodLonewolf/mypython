import time
tallies = {
    'I' : 1,
    'V' : 5,
    'X' : 10
}
left = ''
right = ''
while True:
    roman = input("Enter roman: ")
    sum = 0
    for i in range(len(roman)-1):
        left = roman[i]
        right = roman[i+1]
        print(left, right)
        if left < right:
            sum -= tallies[left]
            print(left, right, sum)
        else:
            sum += tallies[left]
            print(left, right, sum)
    sum += tallies[roman[-1]]
    print(left, right, sum)