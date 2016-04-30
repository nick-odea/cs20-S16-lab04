# lab04Funcs.py     SOLO, Nick O'Dea, nicholas_odea@umail.ucsb.edu
# P. Conrad for CS8, 04/15/2014


from lab02Funcs import isList
from lab02Funcs import isSimpleNumeric


def notStringContainingE(word):
   """
   return True when word is a string that contains no letter 'e' (or 'E')
   It should work both for lower and upper case.
   When word isn't a string, returns True

   """

   if not (type(word)==str):
      return True
   for letter in word:
     if (letter == 'e' or letter == 'E'):   
       return False
   return True


def hasNoX(word):
   """
   return True when word is a string that contains no letter 'x' (and no letter 'X')
   It should work both for lower and upper case.
   When word isn't a string, return True 
   """
   
   if (type(word)!=str):
      return True
   for letter in word:
     if letter == 'x' or letter == 'X':
       return False
   return True


# The following function is provided for you as an example
# of how to write a Python function that checks if EVERY element
# of a list has some property.


def isListOfSimpleNumeric(theList):
   """
   indicates whether value of argument is a list of only simple numerics (int or float)
   Note: empty list should return True---it doesn't contain anything that ISN'T simple numeric
   theList can be anything, and it will return either True or False.
   """
   if (not isList(theList)):
      return False  # it isn't really a list!

   # Now we can assume that theList really is a list
   # But is it a list of all numerics?
   # If we find even a single item that isn't numeric, we can
   # immediately return false.  
   
   for item in theList:
     if not isSimpleNumeric(item):
       return False

   # If we get here and didn't return yet, then we know everything
   # in the list is a simple numeric!
   # (i.e. there isn't anything in the list that is NOT simple numeric)
   
   return True


def isListOfIntegers(theList):
   """
   indicates whether value of argument is a list of only int 
   Note: empty list should return True---it doesn't contain anything that ISN'T int
   theList can be anything, and it will return either True or False.
   """
   
   if isListOfSimpleNumeric(theList) != True:
      return False
   for item in theList:
      if type(item) != int:
         return False
   return True



def isListOfEvenIntegers(theList):
   """
   indicates whether value of argument is a list of only even integers
   Note: empty list should return True---it doesn't contain anything that ISN'T an even integer
   theList can be anything, and it will return either True or False.
   """
   if isListOfIntegers(theList) != True:
      return False
   for item in theList:
      if (item % 2) != 0:
         return False
   return True
    



def totalLength(listOfStrings):
    """
    returns total length of all the strings in a list of strings, False if argument not a list, 0 for empty list
    """
    
    if (not isList(listOfStrings)):
       return False
    totlen = 0
    for item in listOfStrings:
       if type(item) == str:
          totlen = totlen + len(item)
    return totlen
 

def lengthOfEach(listOfStrings):
    """
    given list of strings, returns list of ints correponding to length of each string, otherwise False.
    empty list yields empty list
    """
    if (not isList(listOfStrings)):
       return False
    lenlist = []
    for item in listOfStrings:
       if type(item) != str:
          lenlist = lenlist + ["not str"]
       else:
          lenlist = lenlist + [len(item)]
    return lenlist
    


def countEvens(listOfInts):
    """
    given a list of ints, counts even ints in list.  Otherwise, returns False.
    yields 0 for empty list, or list of ints with no evens in it
    """
    
    if isListOfIntegers(listOfInts) != True:
       return False
    numeven = 0
    for item in listOfInts:
       if (item%2 == 0):
          numeven = numeven + 1
    return numeven



def onlyEvens(listOfInts):
    """
    given a list of ints, return new list with only the even ones.  Otherwise, return false.
    empty list yields empty list
    """

    if isListOfIntegers(listOfInts) != True:
       return False
    listeven = []
    for item in listOfInts:
       if (item%2 == 0):
          listeven = listeven + [item]
    return listeven
 
    



