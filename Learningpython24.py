                                            #  Function basic 
def house():
    print("joolpa")
    
    
                                                # User input 
def yolo():
    yolo = input("Enter a value: ")
    house()
    print(f"what did you say mate {yolo}")
    
yolo()



#                                             Function with parameters


def school_students(principal , master):
    
    print(f"school people incharge names are {principal} and {master} ")
    
    
school_students ("jothika", "rani")


                                                #    Return function
                                                
                                                
    #   This how division works in function  
    #   because in normal way we cannot do division in function beacause it create error and stop the other codes                                        
def add (a,b):
   
    if b==0:
        print('u cannot divide a number by 0')
    else:
        return a/b

values = add(5,0)
print(values)


                                   # addition  , multi , substract 


def add (a,b):
    
    return (a+b)

result = add(2 ,2)

print(result)


                                   # function with default parameter



def hello(default = "itsok" ):
    
    print(f"Default name is {default}")
    
hello("raj")

#   THE DEFAULT NAME , IN Hello ADD A NAME then print it will replace the default name to given name 