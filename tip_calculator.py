print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

### OPTION 1 ###
#bill += bill * (tip / 100)
#bill /= people
#bill = round(bill, 2)

### OPTION 2 ###
total = round((bill + (bill * (tip / 100)))/people, 2)

print(f"Each person should pay: ${total:.2f}")
