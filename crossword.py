

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
