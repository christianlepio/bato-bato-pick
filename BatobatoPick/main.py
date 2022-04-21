import random

option = ('BATO', 'GUNTING', 'PAPEL')
score1 = 0
score2 = 0

while score1 < 5 and score2 < 5:
    print('\n====================LET\'S PLAY BATO BATO PICK====================\n')

    userInput = input('User\'s Choice\t\t: ')
    userInput = userInput.upper()
    bot = random.choice(option)
    print('Computer\'s Choice\t: ',bot)
    if (userInput=="BATO" and bot=="GUNTING") or (userInput=="GUNTING" and bot=="PAPEL") or (userInput=="PAPEL" and bot=="BATO"):
        print('USER WIN!\n')
        score1+=1

    elif (userInput=="GUNTING" and bot=="BATO") or (userInput=="PAPEL" and bot=="GUNTING") or (userInput=="BATO" and bot=="PAPEL"):
        print('USER LOSE!\n')
        score2+=1

    elif userInput == bot:
        print('IT\'S A TIE!\n')
    else:
        print('INVALID INPUT, PLEASE TRY AGAIN!....')
        break
    print('SCORES:\nUSER\t: ',score1,'\nCOMPUTER\t: ',score2,'\n')

    if score1 == 5 or score2 == 5:
        if score1==5:
            print('===================USER WINS!!!!!===================')
            print('==================CONGRATULATIONS!===================')
        elif score2==5:
            print('===================COMPUTER WINS!!!!!===================')
            print('==================BETTER LUCK NEXT TIME!===================')
        option2 = input('\n Play Again? [Y]-Yes || [N]-No: \t')
        option2 = option2.upper()
        if option2 == 'Y':
            score1 = score2 = 0
            print('\n\n')
            continue
        elif option2 == 'N':
            print('\n========THANK YOU FOR PLAYING BATO BATO PICK=========')
            break
        else:
            print('========INVALID INPUT, PLEASE TRY AGAIN!!!=========')
            break