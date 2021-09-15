# Grade11GameSoftware

Game Software – an interface combining 4 games(Sudoku, WordSearch, Hangman, Mastermind)

Members:
	•	Shreya Aiyer
	•	Advaita S
	•	Shivani Jayant
	•	Mansee Jain
	
**ALGORITHMS**

MENU 

1.	If the user types ‘A’ it takes them to the instructions for ‘Sudoku’.
2.	If the user types ‘B’ it takes them to the instructions for ‘Word Search’.
3.	If the user types ‘C’ it takes them to the instructions for ‘Hangman’.
4.	If the user types ‘D’ it takes them to the instructions for ‘Mastermind’.


SUDOKU
1.	The sudoku must be generated with no numbers repeating in the same row and column.
2.	A list with 9 nested lists is the basic empty grid.
3.	To generate a full grid (fillGrid):
a.	Generate a list values to hold the numbers from 1-9 that can be filled into the empty grid
b.	A loop is run with 81 iterations, from with the values of the present row and column is extracted. 
c.	The values list is shuffled.
d.	Based on the row and column values, and element of the grid (cell) is identified. If the cell has a zero value,
i.	A test value from the values list is taken and compared with the existing elements in the cell’s row, column and 3*3 square.
ii.	If the test value is valid, it is inserted into the main grid containing the Sudoku. 
iii.	If the grid is full, the function terminates here.
iv.	Else, the fillgrid function is called again – further elements are added within the recursive function. If no test value is valid for a given cell, it implies that one of the values filled before in the grid has caused the error. So the present function terminates and returns to the outer function that filled the previous cell value. This repeats until the point at which the element that broke the board is corrected
e.	The function terminates when the board is filled.
4.	To remove elements from the grid (removeEle):
a.	A random number is generated between 55 and 65 to determine the number of elements to be removed from the filled grid.
b.	The grid is copied to makes sure no erroneous changes affect the main grid.
c.	In the copied grid, a random cell value is changed to 0.
d.	The backsolver function is used to check if the grid can still be solved if that cell is empty by filling the grid along similar lines as the fillgrid function. 
e.	The flag variable checks the number of ways in which the grid can be solved.
f.	If the grid is unsolvable or has multiple solutions, the removed element is replaced.
5.	Once the final Sudoku is generated, it is printed.
6.	The user is allowed to enter values into the Sudoku, and can’t change any preexisting values.
7.	Once the user has finished the Sudoku, the entered values are compared with the computer generated solution. If the user has solved it correctly, the time taken is displayed with the message “YOU WIN!!”


WORDSEARCH
1.	Import the required modules.
2.	Print out instructions.
3.	Create a function to print out the nested list of the word search in the form of a 20x20 grid.
4.	Create a 20x20 nested list filled with ‘- ‘ at every index position.
5.	Create a function to replace all the ‘- ‘ with random letters in the alphabet.
6.	Create a function to add a word horizontally to the nested list with one letter at each index value.
7.	Create a similar function for vertical south direction.
8.	Create a similar function for diagonal southeast direction.
9.	Create a function to check validity of user’s input to prevent incorrect index inputs.
10.	Create .txt files of various topics with words of each.
11.	Read these files and convert them into lists in Python.
12.	Ask the user to input a valid topic.
13.	Search through the respective topic list and find 6 random unique words – 2 vertically, 2 horizontally and 2 diagonally.
14.	Add these words using the functions at 6, 7, 8 respectively into the nested list such that the value of the first and last indexes of its new position is recorded to check validity at step 9.
15.	Start the timer.
16.	Run the function in step 3 and print out the topics.
17.	Ask for the first and last index of a word allowing for a return to previous page or instructions page.
18.	Run the validity function in step 9. 
19.	If valid, replace the word with a line and remove the word from list of topics. If not, run the steps 16 to 19.
20.	Check if the list of topics is empty and if so, the user has won the game. Record the end time and output the time taken.
21.	If not, run the steps 16 to 20.


HANGMAN
1.	 Initialise- hangman(contains various patterns of hangman) &amp; dictionary (contains the topics)
2.	Display the topics
3.	Read the value of choice(choice of topic) from user.
4.	Pick a random word from the tuple of the particular topic in the dictionary
5.	Form the pattern of selected word
 Vowels are represented by “*”
Consonants are represented by “–“
6.	Define function: print_current_progress() 
 To display the users progress in guessing the word
7.	Define function: user_guess()
a)	Input a guess from user
b)	If letter has already been guessed, user gets to guess again
c)	Return the value of guess
8.	Define function: check_answer()
a)	If guessed letter is in the word:
             Update the pattern of word
b)	Return wrong_answers , so_far
9.	 Define function: print_result()
To display the result
10.	While no. of wrong answers is less than available guesses and the word guessed so far is not the actual word call functions in steps 6,7,8 and 9


MASTERMIND
1.	Generate a list of 6 numbers from 0-9.
2.	Ask the user to try to guess the code.
3.	Based on user input generate a list of ‘@’, ‘*’ and ‘  ‘:
4.	Add ‘@’ to the list for correct place of the number
5.	Add ‘*’ to the list for correct number in the correct place
6.	Add ‘  ’ to the list for unavailability of the number in the code.
7.	Display the user’s guess and the generated list.
8.	If before the end of 10 turns, the user has guessed the code correctly, display ‘YOU WIN!!!’ with the time taken.
9.	If the user does not guess the code or runs out of 10 turns it displays ‘You Lose’.
10.	 Exit to the menu page.

