# Simple tip calculator using python basics

print(">>>>>>>>>>>>>>>>>>>>>>>>>")

print("Welcome to Tip Calculator!")

print("__________________________")


# Taking Inputs

total = float(input("What was the total bill? $"))

perc = float(input("What percentage tip would you like to give ? "))

no = float(input("How many people to split the bill? "))

new_total = total * ((perc/100) + 1)

final = (round(new_total,2)) / no

print(f"Each person should pay: ${final}")



