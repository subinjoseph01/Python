Age = int(input("Enter you age :"))

Ticket = input(" Ticket yes or no : ")

if(Age >18):
    if(Ticket == "yes"):
        print("welcome to the park")
    else:
        print("you need ticket to enter")
        
else:
    print("be 18 to  enter")
