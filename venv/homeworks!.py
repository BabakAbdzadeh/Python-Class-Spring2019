# First Ex.
# Calculate the BMI of body by using formula BMI= weight(kg) / height(kg)^2


mass_var = float(input("Please enter your weight in kg: "))
height_var = float(input("please enter you height in meter: "))
bmi_var = float(mass_var / (height_var * height_var))
print(bmi_var)
