import csv
print("----------------------------------Daily Expense Tracker & Predictor----------------------------------")
print("-----------------------------------------------------------------------------------------------------")

expenses = [
    {"item": "Cabbage", "cost": 230, "category": "Food"},
    {"item": "Book", "cost": 500, "category": "Stationary"},
    {"item": "Momo", "cost": 250, "category": "Food"},
    {"item": "Pathao Ride", "cost": 180, "category": "Transport"},
    {"item": "Milk Tea", "cost": 40, "category": "Food"},
    {"item": "Pen Pack", "cost": 120, "category": "Stationary"},
    {"item": "Bus Fare", "cost": 35, "category": "Transport"},
    {"item": "Chicken Chowmein", "cost": 220, "category": "Food"},
    {"item": "Notebook", "cost": 150, "category": "Stationary"},
    {"item": "Ncell Data Pack", "cost": 299, "category": "Utilities"},
    {"item": "Apples 1kg", "cost": 320, "category": "Food"},
    {"item": "Toothpaste", "cost": 160, "category": "Personal Care"},
    {"item": "Samosa Tarkari", "cost": 90, "category": "Food"},
    {"item": "InDrive Ride", "cost": 240, "category": "Transport"},
    {"item": "Coffee", "cost": 180, "category": "Food"},
    {"item": "Marker Set", "cost": 210, "category": "Stationary"},
    {"item": "Electricity Bill", "cost": 1450, "category": "Utilities"},
    {"item": "Eggs Crate", "cost": 480, "category": "Food"},
    {"item": "Shampoo", "cost": 350, "category": "Personal Care"},
    {"item": "Petrol", "cost": 1000, "category": "Transport"},
    {"item": "Laphing", "cost": 100, "category": "Food"},
    {"item": "Sticky Notes", "cost": 80, "category": "Stationary"},
    {"item": "Internet Bill", "cost": 1350, "category": "Utilities"},
    {"item": "Rice 5kg", "cost": 650, "category": "Food"},
    {"item": "Face Wash", "cost": 420, "category": "Personal Care"}
]

print(" ".join(f"{k:>15}" for k in expenses[0].keys()))
for entry in expenses:
    print(" ".join(f"{str(v):>15}" for v in entry.values()))

total = 0
for entry in expenses:
    total += entry["cost"]

print("Total money spended", total)

def mostExpensive():
    exprice = 0
    exitem = ""
    for entry in expenses:
        if entry["cost"] > exprice:
            exprice = entry["cost"]
            exitem = entry["item"]
    print(f"Most expensive item: {exitem} ({exprice})")

mostExpensive()

with open("expense.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["item", "cost", "category"])
    writer.writeheader()
    writer.writerows(expenses)
    writer.writerow({"item": "Total money spended", "cost": total, "category": ""})

print("expense.csv saved successfully")
