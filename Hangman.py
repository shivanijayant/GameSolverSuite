def Hangman():
 import random
 import os
 import time
 hangman=(
        """
         ------
         |    |
         |
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   -+-
         | 
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-\\
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-\\
         |    |
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-\\
         |    |
         |    |
         |   | 
         |   | 
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-\\
         |    |
         |    |
         |   | |
         |   | |
         |  
        ----------
        """)

 d={
# List of animals and birds
   1:('WOODPECKER','SPIDER MONKEY','CHIPMUNK','ASIAN BLACK BEAR','POISON DART FROG','WOLVERINE','RED FOX','RHINOCEROS','PORCUPINE','ARCTIC FOX','SNOWSHOE HARE','ARCTIC HARE','RED SQUIRREL','HUMMINGBIRD','KINGFISHER','NIGHTINGALE','BALD EAGLE'),
# List of countries
   2:('ARGENTINA','BANGLADESH','CAMBODIA','CENTRAL AFRICAN REPUBLIC','ETHIOPIA','INDONESIA','LUXEMBOURG','MADAGASCAR','NEW ZEALAND','SAUDI ARABIA','SWITZERLAND','UNITED STATES OF AMERICA','UNITED KINGDOM','ZIMBABWE'),
# List of sports
   3:('BADMINTON','BOWLING','BOXING','SKATEBOARDING','FIGURE SKATING','FENCING','GYMNASTICS','KARATE','VOLLEYBALL','WEIGHTLIFTING','BASKETBALL','HIGH JUMPING','HANG GLIDING','CAR RACING','TABLE TENNIS','HORSE RACING'),
# List of rivers
   4:('AMAZON','MISSISSIPPI','MISSOURI','MACKENZIE','RIO GRANDE','BRAHMAPUTRA','MURRAY','ZAMBEZI','COLORADO','TIGRIS','YANGTZE','MEKONG','URUGUAY','CHURCHILL','TENNESSEE'),
# List of flowers
   5:('DAFFODIL','BLUEBELL','CHERRY BLOSSOM','CHRYSANTHEMUM','GERANIUM','WATER LILY','DANDELION','HYACINTH','MARIGOLD','SWEET PEA','PANSY VIOLET','NASTURTIUM','LAVENDER','CAMELLIA','MAGNOLIA'),
# List of colours
   6:('AQUAMARINE','BRONZE','BEIGE','COPPER','CRIMSON','EMERALD','INDIGO','IVORY','LAVENDER','LILAC','MAGENTA','MUSTARD','NAVY BLUE','OLIVE GREEN','SAFFRON','SCARLET','TURQUOISE'),
# List of jobs
   7:('ACCOUNTANT','AMBASSADOR','ASTRONAUT','BIOLOGIST','CARDIOLOGIST','DERMATOLOGIST','ENGINEER','ENTREPRENEUR','GEOLOGIST','JOURNALIST','LECTURER','MUSICIAN','PALEONTOLOGIST','PEDIATRICIAN','SALESPERSON','TRAVEL AGENT')
  }

 comments = ("Well done!", "Awesome!", "Good job!")

#========================================================
#
# Main play
#
#========================================================

 def play():
        Instructions()
        os.system("cls")
        os.system("color 0e")
        print("\t\t\t ********** HANGMAN **********")
        print("1.ANIMALS AND BIRDS")
        print("2.COUNTRIES")
        print("3.SPORTS")
        print("4.RIVERS")
        print("5.FLOWERS")
        print("6.COLOURS")
        print("7.JOBS")

#========================================================
#
# Get topic from the user
#
#========================================================

        choice=' '
        n=0
        while(n==0):
                choice=input("Enter a topic number from 1-7: ")
                if choice.isdigit():
                        if(1<=int(choice)<=7):
                                n=int(choice)
                                WORDS=d[n]
                        else:
                                print("Invalid choice")
                elif choice=='back':
                        return()
                elif choice=='instructions':
                        Instructions()
                        continue
                else:
                        print("Invalid choice")

#========================================================
#
# To choose a random word from the topic chosen
#
#========================================================

        word = random.choice(WORDS)

#========================================================
#
# To form the pattern of the word
#
#========================================================

        so_far=''
        for i in word:
                if(i in ('A','E','I','O','U')):
                        so_far+='*'
                
                elif (i==' '):
                        so_far+=' '
                else:
                        so_far+="-"
        used = []
        wrong_answers = 0

#========================================================
#
# Function to check if the user has made too many wrong guesses
#
#========================================================

        while wrong_answers < len(hangman) and so_far != word:
            print_current_progress(wrong_answers,so_far,used)
            guess = user_guess(used)
            wrong_answers,so_far = check_answer(guess,word,wrong_answers,comments,so_far)

        print_result(wrong_answers,word)

#========================================================
#
# Function to display the current progress of the game
#
#========================================================

 def print_current_progress(wrong_answers,so_far,used):
        os.system("cls")
        print(hangman[wrong_answers])
        print("Word so far: ", so_far)
        print("Letters used: ", used)
        print("Remaining guesses: ",len(hangman)-(wrong_answers))

#========================================================
#
# Function to input the user's guess
#
#========================================================

 def user_guess(used):
        guess = input("Guess a letter: ").upper()
        if guess=='BACK':
            return()
        elif guess=='INSTRUCTIONS':
            Instructions()
        print()
        while guess in used:
            print("Try again... You've already used this letter")
            guess = input("Guess a letter: ").upper()
            print()
        if (guess.isalpha() and len(guess)==1):
                used.append(guess)
        used.sort()
        
        return guess

#========================================================
#
# Function to check whether the user's guess is correct
#
#========================================================

 def check_answer(guess,word,wrong_answers,comments,so_far):
        c=0
        for i in range(len(word)):
                if guess == word[i]:
                        so_far = so_far[:i] + guess + so_far[i+1:]
                        c+=1
        if guess in word:
                print(random.choice(comments))
                a=input("Press enter to continue")
        if(c==0):
                print("INCORRECT! Try again!")
                a=input("Press enter to continue")
                wrong_answers += 1
        return wrong_answers,so_far

#========================================================
#
# Function to display the result of the user's guess
#
#========================================================

 def print_result(wrong_answers,word):
        print()
        os.system("cls")
        end = time.time()
        print("Calculating result...")
        print()
        if wrong_answers == len(hangman):
            print("Better luck next time!")
            print("Right answer: ",word)
            a=input("Press enter to continue")
        else:
            print("Answer: ",word)
            print("WINNER! Congratulations!")
            print("You took",int(end - start),"seconds to find the word.")
            a=input("Press enter to continue")

#========================================================
#
# Function to display the instructions
#
#========================================================

 def Instructions():
  os.system("cls")
  os.system("color 0a")
  print("""
INSTRUCTIONS:
1. Input letters that you think fit in the word.
2. '*' - represents a vowel.
3. '-' - represnts a consonant
4. The game is over once you guess the word or the Hangman is complete.
5. If you guess the word correctly... YOU WIN!!!
6. Type 'back' to return to Menu.
7. Type 'instructions' to return to this page.""")
  a=input("Press enter to start")
 start=time.time() 
 play()
 
