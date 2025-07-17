print("Welcome to tip Calculator")
bill = float(input("What was the total bill?"))
tip = float(input("How much tip would you like to give? 10,12 or 15 percent?"))
split = float(input("How many people will split the bill?"))

person_pay = (bill + (bill * tip/100))/split
final_amount = round(person_pay,2)

print(f"Each person should pay {final_amount}")
