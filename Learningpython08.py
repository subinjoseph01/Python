speed = int(input("Enter a speed :"))

if speed > 0 and speed <= 30:
    print("slow")

elif speed >30 and speed <=60 :
    print("normal")

elif speed >60 and speed <=100:
    print("fast")

elif speed > 100 and speed <=200:
    print("overspeed")

else:
    print("invalid speed")



# Question :
    
#  ⁠If the speed is from 0 to 30 km/h, print: Slow
# •⁠  ⁠If the speed is from 31 to 60 km/h, print: Normal
# •⁠  ⁠If the speed is from 61 to 100 km/h, print: Fast
# •⁠  ⁠If the speed is from 101 to 200 km/h, print: Over Speed
# •⁠  ⁠For any other value, print: Invalid speed

# here any number comes above 200 or less than 1 it will show invalid speed