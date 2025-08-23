try:
    
    Row =int(input("Enter a value 1 :"))
    hey = int(input("Enter a value 2 :")) # user input 
    a = Row/hey
    
    printt("The answer is ",a) # error made in 
    
except ValueError as raj:
    print("Enter a number pls : ",raj)
      
        
except ZeroDivisionError as j:
    print("cannot divide by 0",j)  # number error for 0
    
except NameError as h:
        print("The error is ",h)     # name error
    
except Exception as e:
        print("The error is ",e)     #
        
