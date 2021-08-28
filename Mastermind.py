def Mastermind():
    import os
    import random
    import time
    
#========================================================
#
# Function to check if the users guess is valid
#
#========================================================

    def isValid(lst,guess):
        if len(guess) == 11:
            for i in lst:
                if int(i)<0 or int(i)>9:
                    print(i)
                    return False
                else:
                    return True

#========================================================
#
# Function to display the Mastermind board
#
#========================================================

    def display(L,ans,Output):
        os.system("cls")
        os.system("color 0e")
        print("    ------------- ")
        print('   |',end=' ')
        for i in ans:
            print(i,end=' ')
        print('|')
        print("   |-------------|")
        for i in range(10):
            if i <9:
                print(i+1,'. |',sep='',end=' ')
            else:
                print(i+1,'.|',sep='',end=' ')
            for j in range(6):
                print(L[9-i][j],end=' ')
            print('|',end=' ')
            for j in range(6):
                print(Output[9-i][j],end=' ')
            print()
        print("    ------------- ")

#========================================================
#
# MFunction to display the instructions
#
#========================================================

    def Instructions():
     os.system("cls")
     os.system("color 0a")
     print('''
INSTRUCTIONS:
1. Enter 6 numbers from 0 - 9.
2. The computer has generated a 6 digit code.
3. '*' - implies that the number is in the code but not in the correct place.
4. '@' - implies that the number is in the correct place.
5. '-' - implies that the number is not in the code.
6. You get 10 chances to guess the code.
7. If you guess the code within 10 tries... YOU WIN!!!
8. Type 'back' to return to the menu.
9. Type 'instructions' to return to this page.''')
     a=input("Press enter to continue")

    Instructions()
    start=time.time()
    ans=['X','X','X','X','X','X']
    L=[]
    Output=[]
    for i in range(10):
        L.append([' ',' ',' ',' ',' ',' '])
        Output.append([' ',' ',' ',' ',' ',' '])
    os.system("cls")
    os.system("color 0e")
    lcode=[]
    for i in range(6):
        lcode.append(random.randint(0,9))
    code=tuple(lcode)
    j=0
    while(j<10):
        display(L,ans,Output)
        print("Time's started!")
        print(10-j,"chances left")
        guess=input("Enter code with commas between the numbers : ").lower()
        lst=guess.split(',')
        lcode=list(code)
        if guess=='back':
            return()
        elif guess=='instructions':
            Instructions()
            continue
        
#========================================================
#
# To give results of the user's guess
#
#========================================================

        if (isValid(lst,guess)):
            output=['-','-','-','-','-','-']
            for i in range(6):
                if ((int(lst[i])) == lcode[i]):
                    output[i]='@'
                    lcode[i]=''
            for i in range(6):
                if (int(lst[i]) in lcode):
                    if output[i]!='@':
                       output[i]='*'
                       lcode[lcode.index(int(lst[i]))]=''
            Output[j]=output
            L[j]=lst
            j+=1
        else:
            print("Incorrect input")
            a=input("Press enter to continue")
            continue

#========================================================
#
# To check if the user won the game
#
#========================================================

        if output==['@','@','@','@','@','@']:
            end=time.time()
            ans=code
            display(L,ans,Output)
            print("YOU WIN!!!!!")
            print("You took",int(end - start),"seconds to find the code.")
            a=input("Press enter to continue")
            break
    else:
        print("You Lost :(")
        ans=code
        display(L,ans,Output)
        a=input("Press enter to continue")
        
        
