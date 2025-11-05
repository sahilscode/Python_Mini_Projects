#The code is to calculate the total rent for a given number of months, including a fixed monthly maintenance fee.and split between roomates.

def calculate_total_rent():
    Rent = int(input("Enter the rent amount: "))
    Maintenance = int(input("Enter the maintenance fee: "))
    Food = int(input("Enter the food expense: "))
    Electricity = int(input("Enter the electricity Unit Spent: "))
    Unit_Cost = int(input("Enter the cost per unit: "))
    num_roommates = int(input("Enter the number of roommates: "))

    electicity_bill = Electricity * Unit_Cost
    total_expense = Rent + Maintenance + Food + electicity_bill
    per_person = total_expense/num_roommates
    print(f"Total expencse is {total_expense}")
    print(f"Each roommate should pay: {per_person}")

calculate_total_rent()