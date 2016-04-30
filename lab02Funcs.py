# lab02Funcs.py     Define a few sample functions in Python
# Nick O'Dea for CMPTGCS 20, Spring 2016, nicholas_odea@umail.ucsb.edu


def perimRect(length,width):
   """
   Compute perimiter of rectangle
   """
   length = float(length)
   width = float(width)
   return 2*length + 2*width


def areaRect(length,width):
    """
    Computer area of rectangle
    """
    length = float(length)
    width = float(width)

    return length*width

def isList(x):
   """
   returns True if argument is of type list, otherwise False
   """
   
   return ( type(x) == list )


def isString(x):
    """
    return True if x is a string, otherwise False
    """
    
    return ( type(x) == str) 

def isAdditivePrimaryColor(color):
    """
    return True if color is a string equal to "red", "green" or "blue",
    otherwise False
    """
    
    return ( (color == "red" ) or (color == "green" ) or (color == "blue") )


def isSimpleNumeric(x):
   """
   returns True if x is has type int or float; anything else, False 
   """
   
   return ( (type(x) == int) or (type(x) == float) ) 
