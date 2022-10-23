# Script asking the user for the bill
print("Welcome to the tip calculator by Vector Inc! 😉")
bill = float(input("What was the total bill? $"))
tip = int(
    input(
        "How much tip would you like to give to the waiter ? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

#calculation on the bill and percentage 
tip_percent = tip / 100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount
bill_per_person = total_bill / people
round(bill_per_person, 2)

#formatting to two decimal places
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")

#Coded with ❤️ by Vector 👍

