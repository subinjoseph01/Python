# we have used for loop and used if or else  to get a value 20 to 50 
#but also we have given a  step condition where it multiply by 2 

for geeta in range(20 , 50 ,2):
    if geeta == 32:   # this is a condition where loop decide to match and stop 
        
        break # break will stop 
    
    continue # it will skip the condition geeta part (egsample here number 32 will be skipped if we use continue)
               # insted of break 
    else:
        print(geeta)