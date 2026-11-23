print("----------------------------------Daily Expense Tracker & Predictor----------------------------------" \
      "-----------------------------------------------------------------------------------------------------")

dir = {
    "item":['Cabbage','Book'],
    "cost":['230','500'],
    "category":['food','stationary']
}

print(" ".join(f"{k:>15}" for k in dir.keys()))
for entry in zip(*dir.values()):
    print(" ".join(f"{str(v):>15}" for v in entry))
