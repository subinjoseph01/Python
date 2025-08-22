def calculation(first , second, carol):
        sumi= first + second
        print("positive" , sumi)
        carol()
    
    
def summing():
        print("Negative")
        
calculation(3,3,summing)


# Define two function 
# call the second in first function 
# then add in first function
# call the call back function in first function / passing the value to the second function