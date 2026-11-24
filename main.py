import csv
print("----------------------------------Daily Expense Tracker & Predictor----------------------------------")
print("-----------------------------------------------------------------------------------------------------")

expenses = [
    {"item": "Cabbage", "cost": 230, "category": "food"},
    {"item": "Book", "cost": 500, "category": "stationary"}
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
