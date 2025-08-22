# Exception handling in python is a technique that allows you to deal with
# errors that occurs during programming execution
#  , instead of letting the program crash you can catch and hand the errors or exception gracefully

# To make your code , more robust and user friendly 

try:                               # this about manage it if the code is mistake  still run
    printr("Hellow world")  
    
except Exception as correction:    # this except will find the error and save in exception and give which is error
    print("The error is : ",correction)
    
finally:                 # it prints anyway 
    print("Fail")