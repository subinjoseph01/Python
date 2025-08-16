# secret_number =1

# guess = 0

# while guess != secret_number:
#     guess = int(input("Guess the number : "))
#     if guess != secret_number:
#         print("Tryagain")


# while loop concept in python

password = "remo"

attempts = 3


while attempts >0 :
    guess = input("Enter a value :")
    if guess == password:
        print("Access Granted ")
        
        break
    
    else :
        attempts -=1
        print("wrong password ,Attempts left",attempts)
        
        if attempts ==0:
            print("Account is blocked")
            
            

        
        