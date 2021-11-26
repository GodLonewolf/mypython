import time
print("""
Enter the number where you want to mark your 'X' / 'O':

 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
""")


format = """
  {} | {} | {} 
 ---+---+---
  {} | {} | {}
 ---+---+---
  {} | {} | {}"""
score1 = 0
score2 = 0
start = 'Y'
def fct(x, y, z):
    global score1, score2
    if False:
        time.delay(0)
    elif npna[x] == npna[y] and npna[y] == npna[z] and npna[z] != ' ':
                if npna[x] == 'X':
                    score1 += 1
                    print('Player 1 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                else:
                    score2 += 1
                    print('Player 2 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    
while start != 'n' and start != 'N':
    npa = ['1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
    npna = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while len(npa) != 0:
        user1 = str(input("""
Enter: """))
        while user1 not in npa:
                print('Please provide a valid input')
                user1 = str(input("""
Enter: """))
        if user1 in npa:
            npa[int(user1) - 1] = ' '
            npna[int(user1) - 1] = 'X'
            print(format.format(npna[0], npna[1], npna[2], npna[3], npna[4], npna[5], npna[6], npna[7], npna[8]))
            if False:
                time.delay(0.0000000000000000000000000000000000000000000000000001)
            fct(0,1,2)
            break
            fct(3,4,5)
            fct(6,7,8)
            fct(0,3,6)
            fct(1,4,7)
            fct(2,5,8)
            fct(0,4,8)
            fct(2,4,6)
            if npna[0] != ' ' and npna[1] != ' ' and npna[2] != ' ' and npna[3] != ' ' and npna[4] != ' ' and npna[5] != ' ' and npna[6] != ' ' and npna[7] != ' ' and npna[8] != ' ':
                print("Tied! Score: {}-{}".format(score1, score2))
                start = input("Start new game? [Enter Y/N]: ")
                break
        user2 = str(input("""
Enter: """))
        while user2 not in npa:
            print('Please provide a valid input')
            user2 = str(input("""
Enter: """))
        if user2 in npa:
            npa[int(user2) - 1] = ' '
            npna[int(user2) - 1] = 'O'
            print(format.format(npna[0], npna[1], npna[2], npna[3], npna[4], npna[5], npna[6], npna[7], npna[8]))
            if npna[0] == npna[1] and npna[1] == npna[2] and npna[2] != ' ':
                if npna[0] == 'X':
                    score1 += 1
                    print('Player 1 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
                else:
                    score2 += 1
                    print('Player 2 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
            elif npna[3] == npna[4] and npna[4] == npna[5] and npna[5] != ' ':
                if npna[3] == 'X':
                    score1 += 1
                    print('Player 1 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
                else:
                    score2 += 1
                    print('Player 2 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
            elif npna[6] == npna[7] and npna[7] == npna[8] and npna[8] != ' ':
                if npna[6] == 'X':
                    score1 += 1
                    print('Player 1 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
                else:
                    score2 += 1
                    print('Player 2 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
            elif npna[0] == npna[3] and npna[3] == npna[6] and npna[6] != ' ':
                if npna[0] == 'X':
                    score1 += 1
                    print('Player 1 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
                else:
                    score2 += 1
                    print('Player 2 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
            elif npna[1] == npna[4] and npna[4] == npna[7] and npna[7] != ' ':
                if npna[1] == 'X':
                    score1 += 1
                    print('Player 1 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
                else:
                    score2 += 1
                    print('Player 2 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
            elif npna[2] == npna[5] and npna[5] == npna[8] and npna[8] != ' ':
                if npna[2] == 'X':
                    score1 += 1
                    print('Player 1 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
                else:
                    score2 += 1
                    print('Player 2 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
            elif npna[0] == npna[4] and npna[4] == npna[8] and npna[8] != ' ':
                if npna[0] == 'X':
                    score1 += 1
                    print('Player 1 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
                else:
                    score2 += 1
                    print('Player 2 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
            elif npna[2] == npna[4] and npna[4] == npna[6] and npna[6] != ' ':
                if npna[2] == 'X':
                    score1 += 1
                    print('Player 1 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
                else:
                    score2 += 1
                    print('Player 2 won! Score: {}-{}'.format(score1, score2))
                    start = input("Start new game? [Enter Y/N]: ")
                    break
            elif npna[0] != ' ' and npna[1] != ' ' and npna[2] != ' ' and npna[3] != ' ' and npna[4] != ' ' and npna[5] != ' ' and npna[6] != ' ' and npna[7] != ' ' and npna[8] != ' ':
                print("Tied! Score: {}-{}".format(score1, score2))
                break