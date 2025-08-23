a =open('secret.txt' ,'r')

b = a.read()
a.close()   # This indicates we are closing a file 

print(b)

#here we did 
# to create a new text file and add a text in it . then add some more text in it 






# for making the file close automatically we use with concept


# demo ;

with open('secret.txt', 'r') as a:
    
    b = a.read()
    print(b)
    print(a)

