print("Welcome to the tip 10calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num = int(input("How many people to split the bill?"))

total_bill = bill + (tip / 100) * bill
bill_per_person = total_bill / num
print(f"Each person should pay: ${round(bill_per_person, 2)}")

