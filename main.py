import csv
print("----------------------------------Daily Expense Tracker & Predictor----------------------------------")
print("-----------------------------------------------------------------------------------------------------")
      

dir = {
    "item":['Cabbage','Book'],
    "cost":['230','500'],
    "category":['food','stationary']
}

print(" ".join(f"{k:>15}" for k in dir.keys()))
for entry in zip(*dir.values()):
    print(" ".join(f"{str(v):>15}" for v in entry))

total = 0
for i in dir["cost"]:
    total += int(i)

print(f"Total money spended",total)

with open("expense.csv","w",newline="") as file:
    writer = csv.writer(file)

    writer.writerow(dir.keys())

    for i in zip(*dir.values()):
        writer.writerow(i)

    writer.writerow([])
    writer.writerow(["Total money spended",total,""])

print("expense.csv saved successfully")
