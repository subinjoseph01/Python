#  ⁠If the BMI is below 18.5, print: Underweight
# •⁠  ⁠If the BMI is from 18.5 to 24.9, print: Normal
# •⁠  ⁠If the BMI is from 25 to 29.9, print: Overweight
# •⁠  ⁠If the BMI is from 30 to 40, print: Obese
# •⁠  ⁠If the BMI is outside the range 10 to 40, print: Invalid BMI

bmi = float(input("Enter a value :"))

# float_val = 18.5

# print(bmi)
# print(type(bmi))

# print(float_val)
# print(type(float_val))

# 10

if bmi > 0 and bmi <= 18.5: # 0.1....18.5.  ///.   if True and True:
    print("Under weight")
    
elif bmi > 18.5 and bmi <= 24.9: # 18.6 .... 24.9 
    print("Normal")
    
elif bmi >= 25 and bmi   <= 29.9: # 25.0 .... 30 
    print("Over weight")
    
elif bmi > 30 and bmi <= 40: # 30.1 .... 40
    print("Obese")
    
else:
    print("Invalid BMI") # .... 0, 40.1 ......
