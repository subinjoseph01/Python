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
    
    Exception key concepts :
        
#        An exception is an error that happens while the program is running.
# 👉 Example:
# If you try to divide a number by zero.

# Or if you try to open a file that doesn’t exist.

# So basically: An exception = a problem that stops the program while it’s running.

        
#         Try : You put the code that might cause an error (exception) inside a try block.
# If an error happens, Python jumps to the except block to handle it, instead of crashing the program.
        
# except: Tells the program what to do when a certain error happens.

# else: Runs only if no error happens in the try block.

# Final : Always runs, whether there was an error or not. Usually used to clean things up. ✅