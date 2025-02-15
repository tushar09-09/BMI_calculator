def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

def main():
    print("🔹 Welcome to the BMI Calculator 🔹")

    try:
        weight = float(input("Enter your weight in kg: "))
        height_cm = float(input("Enter your height in cm: "))

        if weight <= 0 or height_cm <= 0:
            print("❌ Error: Please enter valid positive values for weight and height.")
            return

        bmi, category = calculate_bmi(weight, height_cm)
        print(f"\n📊 Your BMI: {bmi:.2f}")
        print(f"📝 Category: {category}")

    except ValueError:
        print("❌ Error: Please enter numeric values for weight and height.")


if __name__ == "__main__":
    main()
