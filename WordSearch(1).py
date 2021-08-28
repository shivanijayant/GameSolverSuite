def WordSearch():
 import random
 import time
 import os
#========================================================
#
# Function to print instructions
#
#========================================================
 def Instructions():
  os.system("cls")
  os.system("color 0a")
  print('''
INSTRUCTIONS:
1. Words will be hidden horizontally, vertically and diagonally within the 20x20 grid
2. Find the words and enter the indices as column,row
3. If you find all of the words mentioned below the grid... YOU WIN!!!
4. Type 'back' to return to the Menu.
5. Typr 'instructions' to return to this page.''')
  a=input("Press enter to start")

#========================================================
#
# Function to print the wordsearch
#
#========================================================

 def displaywordsearch(wordsearch):
  os.system("cls")
  os.system("color 0e")
  print("     1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20")  
  print("    _____________________________________________________________")
  for row in range(0,20):
    if (row<9):    
      line=str(row+1)+". | "
    else:
      line=str(row+1)+".| "
    print("   |                                                             |")
    for col in range(0,20):
      line = line + wordsearch[row][col] + "  "
    line = line + "|"
    print(line)
  print("   |_____________________________________________________________|")

#========================================================
#
# Function to replace all '-' with a random letter
#
#========================================================

 def randomreplace(wordsearch):
  LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for row in range(0,20):
    for col in range(0,20):
      if wordsearch[row][col]=="-":
        randomLetter = random.choice(LETTERS)
        wordsearch[row][col]=randomLetter
    
#========================================================
#
# Function to add word horizontally to the wordsearch
#
#========================================================

 def addWord_hor(word,wordsearch,FirstIndex,SecondIndex,List):
  row=random.randint(0,19)
  col=random.randint(0,19-len(word))
  FirstIndex.append(str(col+1)+','+str(row+1))
  for i in range(0,len(word)):
    if wordsearch[row][col+i]!='-':
      if wordsearch[row][col+i]!='-':
        #wordsearch[row][col+i]=word[i]
      #else:
        for j in range(0,len(word)):
          if j==i:
           continue
          else:
            wordsearch[row][col+j]='-'
        break
    else:
      wordsearch[row][col+i]=word[i]
  SecondIndex.append(str(col+i+1)+','+str(row+1))
  List.append(word)

#========================================================
#
# Function to add word diagonally to the wordsearch
#
#========================================================

 def addWord_diag(word,wordsearch,FirstIndex,SecondIndex,List):
  row=random.randint(0,19-len(word))
  col=random.randint(0,19-len(word))
  FirstIndex.append(str(col+1)+','+str(row+1))
  for i in range(0,len(word)):
    if wordsearch[row+i][col+i]!='-':
      if wordsearch[row+i][col+i]!='-':
       # wordsearch[row+i][col+i]=word[i]
      #else:
        for j in range(0,len(word)):
          if j==i:
            continue
          else:   
            wordsearch[row+j][col+j]='-'
        break
    else:
      wordsearch[row+i][col+i]=word[i]
  SecondIndex.append(str(col+i+1)+','+str(row+i+1))
  List.append(word)

#========================================================
#
# Function to add word vertically to the wordsearch
#
#========================================================

 def addWord_ver(word,wordsearch,FirstIndex,SecondIndex,List):
  row=random.randint(0,19-len(word))
  col=random.randint(0,19)
  FirstIndex.append(str(col+1)+','+str(row+1))
  for i in range(0,len(word)):
    if wordsearch[row+i][col]!='-':
      if wordsearch[row+i][col]!='-':
       # wordsearch[row+i][col]=word[i]
      #else:
        for j in range(0,len(word)):
          if j==i:
           continue
          else:
            wordsearch[row+j][col]='-'
        break
    else:
      wordsearch[row+i][col]=word[i]
  SecondIndex.append(str(col+1)+','+str(row+i+1))
  List.append(word)
  
#========================================================
#
# Function to check if the user's input is correct
#
#========================================================

 def isValid(n1,n2,FirstIndex,SecondIndex,List):
  if n1 in FirstIndex:
      if FirstIndex.index(n1)==SecondIndex.index(n2):
          return True
      else:
          return False
  return False
 List=[]
 FirstIndex=[]
 SecondIndex=[]
 
#========================================================
#
# Create empty wordsearch
#
#========================================================

 wordsearch = []
 for row in range(0,20):
     wordsearch.append([])
     for col in range(0,20):wordsearch[row].append("-")

 topics=['Food','Clothes','Countries','Flowers','Colours']

#========================================================
#
# Create list of values within topic
#
#========================================================

 fo=open('food.txt','r')
 food=fo.readlines()
 Food = [x.replace('\n', '') for x in food]
 [x.upper() for x in Food]
 #print(Food)

 cl=open('clothes.txt','r')
 clothes=cl.readlines()
 Clothes = [x.replace('\n', '') for x in clothes]
 [x.upper() for x in Clothes]
#print(Clothes)

 co=open('countries.txt','r')
 countries=co.readlines()
 Countries = [x.replace('\n', '') for x in countries]
 [x.upper() for x in Countries]
#print(Countries)

 fl=open('flowers.txt','r')
 flowers=fl.readlines()
 Flowers = [x.replace('\n', '') for x in flowers]
 [x.upper() for x in Flowers]
#print(Flowers)

 col=open('colours.txt','r')
 colours=col.readlines()
 Colours = [x.replace('\n', '') for x in colours]
 [x.upper() for x in Colours]
#print(Colours)

#========================================================
#
# Addition of words to wordsearch
#
#========================================================

 listwords=[]
 Instructions()

#========================================================
#
# Choosing of topic
#
#========================================================

 os.system("cls")
 c=1
 for i in topics:
    print(str(c)+'.',i)
    c+=1
 top=input("Please enter one of the above topics : ").capitalize()
 while top not in topics:
    top=input("Please enter a valid topic : ").capitalize()
 
#========================================================
#
# Food
#
#========================================================

 if top=='Food':
#horizontally
   for i in range(2):
    food=[]
    for j in Food:
      if j not in listwords:
        food.append(j)
    w=random.choice(food)
    addWord_hor(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)
#vertically
   for i in range(2):
    food=[]
    for j in Food:
      if j not in listwords:
        food.append(j)
    w=random.choice(food)
    addWord_ver(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)
#diagonally
   for i in range(2):
    food=[]
    for j in Food:
      if j not in listwords:
        food.append(j)
    w=random.choice(food)
    addWord_diag(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)

#========================================================
#
# Clothes
#
#========================================================

 elif top=='Clothes':
#horizontally
   for i in range(2):
    clothes=[]
    for j in Clothes:
      if j not in listwords:
        clothes.append(j)
    w=random.choice(clothes)
    addWord_hor(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)
#vertically
   for i in range(2):
    clothes=[]
    for j in Clothes:
      if j not in listwords:
        clothes.append(j) 
    w=random.choice(clothes)
    addWord_ver(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)
#diagonally
   for i in range(2):
    clothes=[]
    for j in Clothes:
      if j not in listwords:
        clothes.append(j) 
    w=random.choice(clothes)
    addWord_diag(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)

#========================================================
#
# Colours
#
#========================================================

 elif top=='Colours':
#horizontally
   for i in range(2):
    colours=[]
    for j in Colours:
      if j not in listwords:
        colours.append(j)
    w=random.choice(colours)
    addWord_hor(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)
#vertically
   for i in range(2):
    colours=[]
    for j in Colours:
      if j not in listwords:
        colours.append(j)
    w=random.choice(colours)
    addWord_ver(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)
#diagonally
   for i in range(2):
    colours=[]
    for j in Colours:
      if j not in listwords:
        colours.append(j)
    w=random.choice(colours)
    addWord_diag(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)

#========================================================
#
# Flowers
#
#========================================================

 elif top=='Flowers':
#horizontally
   for i in range(2):
    flowers=[]
    for j in Flowers:
      if j not in listwords:
        flowers.append(j)
    w=random.choice(flowers)
    addWord_hor(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)
#vertically
   for i in range(2):
    flowers=[]
    for j in Flowers:
      if j not in listwords:
        flowers.append(j)
    w=random.choice(flowers)
    addWord_ver(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)
#diagonally
   for i in range(2):
    flowers=[]
    for j in Flowers:
      if j not in listwords:
        flowers.append(j)
    w=random.choice(flowers)
    addWord_diag(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)

#========================================================
#
# Countries
#
#========================================================

 elif top=='Countries':
#horizontally
   for i in range(2):
    countries=[]
    for j in countries:
      if j not in listwords:
        countries.append(j)
    w=random.choice(Countries)
    addWord_hor(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)
#vertically
   for i in range(2):
    countries=[]
    for j in countries:
      if j not in listwords:
        countries.append(j)
    w=random.choice(Countries)
    addWord_ver(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)
#diagonally
   for i in range(2):
    countries=[]
    for j in countries:
      if j not in listwords:
        countries.append(j)
    w=random.choice(Countries)
    addWord_diag(w.upper(),wordsearch,FirstIndex,SecondIndex,List)      
    listwords.append(w)

 randomreplace(wordsearch)

#========================================================
#
# Start timer
#
#========================================================

 start = time.time()
 
#========================================================
#
# User interface with the computer to solve wordsearch
#
#========================================================

 x=True
 while(x):
    displaywordsearch(wordsearch)
    print(FirstIndex)
    p=1
    for i in List:
        print(str(p)+'.',(i.lower()).capitalize())
        p+=1
    n1=input("Enter first index:").lower()
    if n1=='back':
        return()
    elif n1=='instructions':
        Instructions()
        continue
    n2=input("Enter second index:").lower()
    if n2=='back':
        return()
    elif n2=='instructions':
        Instructions()
        continue
    if (isValid(n1,n2,FirstIndex,SecondIndex,List)):
     Q=FirstIndex.index(n1)
     List[Q]=' '
     N1=n1.split(',')
     N2=n2.split(',')
     a=int(N1[1])-1
     b=int(N2[1])
     c=int(N1[0])-1
     d=int(N2[0])
     if(a+1==b):
        for i in range(c,d):
            wordsearch[a][i]='-'
     elif(c+1==d):
        for i in range(a,b):
            wordsearch[i][c]='|'
     elif (a-c==b-d):
        while(a<b):
            wordsearch[a][c]='\\'
            a+=1
            c+=1
    else:
        print("ERROR: There is no word here.")
        y=input("Press enter to continue")
    
    if(List==[' ',' ',' ',' ',' ',' ']):
        print("YOU WIN!!!")
        end = time.time()
        print("You took",int(end - start),"seconds to complete the wordsearch.")
        x=False
 a=input("Press enter to continue")
