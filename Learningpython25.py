def add(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def multi(a,b):
    c=a*b
    return c

def div(a,b):
    if b==0:
        print('NOT DIVISIBLE BY 0')
    else:
        c = a/b
    return c


def cal():
    while True:
        
        a = int(input("Enter a value :"))
        b = int(input("Enter a value :"))
        c = int(input("1 add , 2 sub , 3 multi , 4 div , 5 exit : "))
        
        if c==1:
            result = add(a,b)
            
        elif c==2:
            result = sub(a,b)
            
        elif c==3:
            result = multi(a,b)
        elif c==4:
            result = div(a,b)
        elif c ==5:
            print(" you are exit")
            
            break 
        else:
            ("Enter a valid input")
        print(f"your value is {result}")
        
        
cal()
        
            
            
# Here we have done the return in functions 