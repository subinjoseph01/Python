# Ask the user to enter age and check whether today is a public holiday (yes/no).
# •⁠  ⁠If their age is below 13:
# o	If it is a public holiday, print: "Child ticket: ₹100"
# o	Otherwise, print: "Child ticket: ₹70"
# •⁠  ⁠If age is 13 or above:
# o	If it is a public holiday, print: "Adult ticket: ₹200"
# o	Otherwise, print: "Adult ticket: ₹150"

Age = int(input("Enter your age :"))

publicholiday = input("yes or no :")


if Age < 13 :
    if publicholiday == "yes":
        print("Child ticket : 100")
    else:
        print("Child ticket is 70")
        
else:
    if publicholiday == "yes":
            print("Adult ticket 200")
    else:
            print("Adult ticket 150")
        
            

            
            
        
        
        # print("child ticket is 70")
        
        # if Age > 13:
        #     if publicholiday == ("yes"):
        #         print("Adult ticket 200")
        #         print("adult ticket 150")
            # else:
            #     ("Enter a valid input")
