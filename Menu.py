import os
import Sudoku
import WordSearch
import Hangman
import Mastermind
import time
while(True):
   os.system("cls")
   os.system("color 0b")
   print('''
*********     ***     ***     ***  *********  *********
*********   *******   ****   ****  *********  *********
***        ***   ***  ***** *****  **         **       
***        ***   ***  *** *** ***  ********   *********
***  ****  *********  ***  *  ***  ********   *********
***    **  *********  ***     ***  **                **
*********  ***   ***  ***     ***  *********  *********
*********  ***   ***  ***     ***  *********  *********''')
   print()
   print()
   print("Press 'A' for Sudoku")
   print("Press 'B' for Wordsearch")
   print("Press 'C' for Hangman")
   print("Press 'D' for Mastermind")

#========================================================
#
# To check which game the user wants to play
#
#========================================================

   ans=input().upper()
   if ans=="A":
    Sudoku.Sudoku()
   elif ans=="B":
    WordSearch.WordSearch()
   elif ans=="C":
    Hangman.Hangman()
   elif ans=="D":
    Mastermind.Mastermind()
   else:
    print("Incorrect Input")
    a=input("Press enter to continue")
