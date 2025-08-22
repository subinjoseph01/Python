def hey(a):
    
    b = int(input("Enter a value :"))
    if (b <11):
        print("sir")
        a()

def hi():
    print("happy")

hey(hi)


# This method we defined as call back function 
# in the if part we had given if statement to make it true