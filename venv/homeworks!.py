# First Ex.
# Calculate the BMI of body by using formula BMI= weight(kg) / height(kg)^2


mass_var = float(input("Please enter your weight in kg: "))
height_var = float(input("please enter you height in meter: "))
# extra work for stupid people who write their height in Cm
if height_var > 3:
    height_var = height_var / 100
    if height_var > 3:
        Print("get the hell out of here you idiot!")

bmi_var = float(mass_var / (height_var * height_var))

if bmi_var > 30:
    print("your bmi is :  ", bmi_var, " and its  'Obesity' ")
elif 25 < bmi_var <= 30:
    print("your BMI is:", bmi_var, " and its 'Overweight'")
elif 18.5 < bmi_var <= 25:
    print("your BMI is:", bmi_var, " and its 'Normal'")
else:
    print("your BMI is:", bmi_var, " and its 'Underweight'")
