def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def determine_weight_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = calculate_bmi(weight, height)
weight_category = determine_weight_category(bmi)

print("BMI:", bmi)
print("Weight category:", weight_category)

output:
  
Enter weight in kilograms: 67
Enter height in meters: 123
BMI: 0.004428580871174565
Weight category: Underweight
