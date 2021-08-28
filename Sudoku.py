def Sudoku():
 import time
 import random
 import copy
 import os
#========================================================
#
# Function to print the sudoku
#
#========================================================
 def printGrid(grid):
    os.system("cls")
    os.system("color 0e")
    print("   1 2 3   4 5 6   7 8 9")
    print("   ---------------------")
    for i1 in range(3):
        print(i1+1,"|",sep=" ",end='')
        for j1 in range(3):
            print(grid[i1][j1], end = " ")
        print("|", end=" ")
        for j2 in range(3,6):
            print(grid[i1][j2], end=" ")
        print("|", end=" ")
        for j3 in range(6,9):
            if j3<8:
                print(grid[i1][j3], end=" ")
            else:
                print(grid[i1][j3], end="")
        print("|")

    print("  |------+-------+------|")

    for i2 in range(3,6):
        print(i2+1,"|",sep=" ",end='')
        for j1 in range(3):
            print(grid[i2][j1], end=" ")
        print("|", end=" ")
        for j2 in range(3,6):
            print(grid[i2][j2], end=" ")
        print("|", end=" ")
        for j3 in range(6,9):
            if j3<8:
                print(grid[i2][j3], end=" ")
            else:
                print(grid[i2][j3], end="")
        print("|")

    print("  |------+-------+------|")

    for i3 in range(6,9):
        print(i3+1,"|",sep=" ",end='')
        for j1 in range(3):
            print(grid[i3][j1], end=" ")
        print("|", end=" ")
        for j2 in range(3,6):
            print(grid[i3][j2], end=" ")
        print("|", end=" ")
        for j3 in range(6,9):
            if j3<8:
                print(grid[i3][j3], end=" ")
            else:
                print(grid[i3][j3], end="")
        print("|")
    print("   ---------------------")
#========================================================
#
# Function checks if the number is in the row
#
#========================================================
 def checkRow(testVal, row, grid):
    return bool(testVal in grid[row])


#========================================================
#
# Function checks if the number is in the column
#
#========================================================
 def checkCol(testVal, col, grid):
    colList = []
    for i in range(9):
        colList.append(grid[i][col])
    return bool(testVal in colList)

#========================================================
#
# Function checks if the number is in the square (3*3)
#
#========================================================
 def checkSquare(testVal, row, col, grid):
    square = []

    #To identify which (3*3) square the cell belongs to
    #square (list) is the list of all values in the (3*3) square
    if row < 3:
        if col < 3:
            square = [grid[i][0:3] for i in range(0, 3)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(0, 3)]
        else:
            square = [grid[i][6:9] for i in range(0, 3)]
    elif row < 6:
        if col < 3:
            square = [grid[i][0:3] for i in range(3, 6)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(3, 6)]
        else:
            square = [grid[i][6:9] for i in range(3, 6)]
    else:
        if col < 3:
            square = [grid[i][0:3] for i in range(6, 9)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(6, 9)]
        else:
            square = [grid[i][6:9] for i in range(6, 9)]

    return bool(testVal in square[0]+square[1]+square[2])

#========================================================
#
# Function to check if the grid is filled
#
#========================================================
 def isGridFilled(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c]==0:
                return False
    else:
        return True

#========================================================
#
# Function to generate a full sudoku
#
#========================================================
 def fillGrid(grid, tracker):
 
    values= [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for cellNo in range(81):
            row = cellNo // 9
            col = cellNo % 9

            random.shuffle(values)
            if grid[row][col] == 0:

                for testVal in values:
                    # 1. in the row
                    # 2. in the col
                    # 3. in the square

                    r1 = checkRow(testVal, row, grid)
                    r2 = checkCol(testVal, col, grid)
                    r3 = checkSquare(testVal, row, col, grid)

                    if r1 == False and r2 == False and r3 == False:
                        #If testVal is unique in its row, column and (3*3) square
                        grid[row][col] = testVal

                        if isGridFilled(grid):
                            return True
                        else:
                            if fillGrid(grid, cellNo):
                               return True

                break 
    grid[row][col] = 0

#==========================================================================
#
# Function to check if the sudoku with removed elements can still be solved
#
#===========================================================================
 def backSolver(copy):
    global flag
    for cellNo in range(81):
            row = cellNo // 9
            col = cellNo % 9

            if grid[row][col] == 0:

                for testVal in range(1,10):
                    # 1. in the row
                    # 2. in the col
                    # 3. in the square

                    r1 = checkRow(testVal, row, copy)
                    r2 = checkCol(testVal, col, copy)
                    r3 = checkSquare(testVal, row, col, copy)

                    if r1 == False and r2 == False and r3 == False:
                        #If testVal is unique in its row, column and (3*3) square
                        copy[row][col] = testVal

                        if isGridFilled(copy):
                            flag+=1 
                            return True
                        else:
                            if backSolver(copy):
                               return True

                break 
    copy[row][col] = 0

#========================================================
#
# Function to remove elements from the full sudoku
#
#========================================================
 def removeEle(grid):
    global flag
    x=random.randint(55,65)
    for i in range(x):
        
        row = random.randint(0,8)
        col = random.randint(0,8)
    
        orgVal = grid[row][col]
        copyGrid = copy.deepcopy(grid)

        flag = 0
        backSolver(copyGrid)
        

        if flag > 1:
            copyGrid[row][col] = orgVal
            print("going to orgval")
        else:
            grid[row][col] = 0

#================================================================
#
# Function to replace all zeroes in the sudoku with blank spaces
#
#================================================================
 def replaceZero(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                grid[i][j] = " "
                
#================================================================
#
# Function to create a list of indices having a number already
#
#================================================================
 def CreateList(lst,grid):
     for num in range(9):
         for num1 in range(9):
             if grid[num][num1] !=0:
                 st=str(num1+1)+','+str(num+1)
                 lst.append(st)
     
                 
#================================================================
#
# Condition to end sudoku
#
#=================================================================
 def condition(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c]==' ':
                return True
    else:
        return False
        
#=============================================================================== 

 def Instructions():
  os.system("cls")
  os.system("color 0a")
  print("""
INSTRUCTIONS:
1. Fill in the rows columns and each 3x3 grid with numbers from 1 to 9 with no repition.
2. ' ' - is an unfilled spot.
3. Already filled spots cannot be changed.
4. The game is over once every box in the 9x9 grid is filled.
5. If all numbers are entered correctly... YOU WIN!!!
6. Enter all inputs in format of column,row,value
7. Type 'back' to return to Menu.
8. Type 'instructions' to return to this page.""")
  a=input("Press enter to start")
 Instructions()
 lst=[]
 exit = False
 while exit == False:        
    grid = []
    for i in range(9):
        #create empty grid
        grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

    #To handle exceptions in case of recursion errors
    try:
        fillGrid(grid, 1)
        L=[]
        for i in grid:
            L.append(tuple(i))
        #Flag tracks how many ways in which the sudoku can be solved (used while back solving)
        flag = 0

        removeEle(grid)
        CreateList(lst,grid)
        replaceZero(grid)        
        exit = True
        
    except:
        print("")
 start = time.time()
 print("Time's started!!")
 while(condition(grid)):
    printGrid(grid)
    ip=input("Enter in format column,row,value:")
    if ip=='back':
        return()
    elif ip=='instructions':
        Instructions()
        continue
    elif(len(ip)==5):
        if(ip[0:3] in lst):
             print("ERROR: You cannot change this value")
             a=input("Press enter to continue")
        else:
             l=ip.split(',')
             col=int(l[0])
             row=int(l[1])
             val=int(l[2])
             if(col>9 or col<0 or row>9 or row<0 or val<0 or val>9):
                print("ERROR: Your column, row or value number is out of range")
                a=input("Press enter to continue")
             else:
                grid[row-1][col-1]=val
    else:
        print("ERROR: Your input format is incorrect")
        a=input("Press enter to continue")
   
 for i in range(9):
     if grid[i]!=list(L[i]):
        print("You Lost :(")
        break
 else:
     print("YOU WIN!!!")
     end = time.time()
     a=input(int(end - start),"seconds were taken to complete the wordsearch.")

