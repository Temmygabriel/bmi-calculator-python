# BMI Calculator
# Weight in kilograms
# Height in feet and inches

weight_kg = float(input("Enter your weight in kilograms: "))
feet = int(input("Enter your height (feet): "))
inches = int(input("Enter remaining height (inches): "))

total_inches = feet * 12 + inches
height_m = total_inches * 0.0254

bmi = weight_kg / (height_m ** 2)

if bmi <= 18.5:
    category = "Underweight"
elif bmi <= 25:
    category = "Normal weight"
elif bmi <= 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is: {bmi:.2f}")
print("BMI Category:", category)