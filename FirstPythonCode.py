#first python output
print('Hello, world!')

                                       #Check the Python Version
#sys is a built-in module that contains many system-specific parameters and functions, including the python version in use
#before using it, we must explicity import it
import sys
print(sys.version)

                                       #Types of objects in Python

#Integer => 11
#Float => 2.14
#String => "Hello, Python 101!"

#You can get Python to tell you the type of an expression by using the built-in type() function.

type(12) #returns type of 12
type(2.14) #return type of 2.14
type(-1) #return type of -1
type("Hello, Python 101!") # returns type of "Hello, Python 101!"

                             #Converting from one object to a different object type

float(2) #convert 2 to a float
type(float(2)) #convert integer 2 to a float and check its type
int(1.1) # Casting 1.1 to integer will result in loss of information
int('1 or 2 people') #convert a string into a integer with error
float('1.2') #convert the string "1.2" into a float
str(1) #convert an integer to a string
str(1.2) #convert a float to a string

                                    #Boolean data type
True #Value true
False #Value false

type(True) #type of true
type(False)  #type of false

int(True) #convert True to int
bool(1) #convert 1 to boolean
bool(0) #convert 0 to boolean
float(True) #convert True to float

