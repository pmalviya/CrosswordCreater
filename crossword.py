# ============
#  Crosswords
# ============
# 
# PROBLEM
# =======
# 
# Ampush team engineers love to play crosswords in their spare time. 
# However, they solve way too many puzzles. They can go on for hours
# solving these puzzles. They're really freak.
# 
# The problem is that it's not so easy to find the amount of crossword
# games that they need. Probably would be better if they had an automated 
# way to generate their crossword games. They would be much happier.
# 
# TASK
# ====
# 
# Write a program that:
# 
#   * Reads 'n' strings from stdin
#   * Writes a crosswords puzzle to stdout containing the strings 
# 
# Also respect these few rules:
# 
#   * Words can only be written from top to bottom or from left to right.
#   * The crosswords puzzle size should be 10x10.
#   * The strings should be randomly displayed on the puzzle
#   * All the other letters in the puzzle should be random [A-Z]



##Analysis##
#It looks like a NP Complete problem to me and I have used Brute force way for
# solving it
# Following is the psuedocode for the implemented solution
#1. Read words and row/col size of the grid
#2. Random shuffle the list of words to generate puzzle for random ordered words
#3. Initialize empty Grid 
#4. For each word in the words list
#     i. Try to place it horizontally at each valid position on Grid
#     ii. And recursively call step one i other words 
#    iii. Try to place word vertically at each position on the Grid and
#    iv. And recursively call step i for other words
#5. Exit the recursion when either length of words become 0 or we accumulate certain number of results for display
#6. Randomly pick one possible solution to print


#Execution python crossword.py

#Here is the sample output
#How many words do you want in your puzzle?4
#Enter Grid row/column size:10
#Enter word 1:AMPUSH
#Enter word 2:CARS
#Enter word 3:TEAM
#Enter word 4:POKER
#P,  O,  K,  E,  R,  A,  T,  E,  A,  M,  

#C,  C,  C,  C,  C,  M,  C,  C,  C,  C,  

#C,  C,  C,  C,  C,  P,  C,  C,  C,  C,  

#C,  C,  C,  C,  C,  U,  C,  C,  C,  C,  

#C,  C,  C,  C,  C,  S,  C,  C,  C,  C,  

#C,  C,  C,  C,  C,  H,  C,  C,  C,  C,  

#A,  C,  C,  C,  C,  C,  C,  C,  C,  C,  

#R,  C,  C,  C,  C,  C,  C,  C,  C,  C,  

#S,  C,  C,  C,  C,  C,  C,  C,  C,  C,  

#C,  C,  C,  C,  C,  C,  C,  C,  C,  C,  


import copy
import sys
import random

class  Grid():
        def __init__(self, nrows, ncols):
                self.grid = [["0" for i in range(nrows)] for j in range(ncols)]
                self.nrows = nrows
                self.ncols = ncols

        def printGrid(self):
            letters ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*+='
            replaceLetter = random.choice(letters)
            for i in range(self.nrows):
                for j in range(self.ncols):
                    if(self.grid[i][j] == "0"):
                        self.grid[i][j] = replaceLetter
                    print self.grid[i][j] + ", ",
                print "\n"

        def addHorizontal(self, word, srow, scol):
                self.grid[srow][scol:len(word)] = list(word)

        def addVertical(self, word, srow, scol):
                count = 0
                for char in list(word):
                        self.grid[srow+count][scol] = char
                        count += 1


possible_solutions  = []
def placeHorizontal(grid, word, srow, scol):
    word_len = len(word)
    if scol + word_len > grid.ncols:
        return False
    count = 0
    for char in list(word):
        if grid.grid[srow][scol + count] != "0" and grid.grid[srow][scol + count] != char:
            return False
        count += 1
    return True

def placeVertical(grid, word, srow, scol):
    word_len = len(word)
    if srow + word_len > grid.nrows:
        return False
    count = 0
    for char in list(word):
        if grid.grid[srow + count][scol] != "0" and grid.grid[srow + count][scol] != char:
            return False
        count += 1
    return True

def getCompletePuzzle(grid, words):
  if len(words) == 0 :
    possible_solutions.append(grid)
    return 
  if(len(possible_solutions)>20):
        return

  word =words[0]
  for ii in range(grid.nrows):
    for jj in range(grid.ncols):
       if placeHorizontal(grid, word, ii, jj):
         new_grid = copy.deepcopy(grid)
         new_grid.addHorizontal(word, ii, jj)
         getCompletePuzzle(new_grid, words[1:])
       if placeVertical(grid, word, ii, jj):
         new_grid = copy.deepcopy(grid)
         new_grid.addVertical(word, ii, jj)
         getCompletePuzzle(new_grid, words[1:])

def main(nrows, ncols, words):
    grid = Grid(nrows, ncols)
    getCompletePuzzle(grid, words)

if __name__ == "__main__":
    #words = ['AMPUSH', 'POKER', 'TEAM', 'CATS']
    wordslength = input("How many words do you want in your puzzle?")
    n = input("Enter Grid row/column size:")
    words =[]
    try:
        i=0
        while(i<int(wordslength)):
            word = raw_input("Enter word " + str(i+1) +":")
            if(len(word)>n):
                print "word length can't be greater than grid size"
                i=i-1
            else:
                words.append(str(word))
            i+=1
    except ValueError:
        print "Validation failed, try again"
        
    random.shuffle(words)
    
    main(int(n), int(n), words)
    #main(10, 10, words)
    if(len(possible_solutions) == 0):
        print "Sorry couldn't find appropriate solutions for the given words and grid size"
    else:
        solution = possible_solutions[random.randint(0, len(possible_solutions))]
        print solution.printGrid()
