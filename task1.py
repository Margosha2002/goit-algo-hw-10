from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem(name="production_maximization", sense=LpMaximize)

lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

model += lemonade + fruit_juice, "total_production"
model += 2 * lemonade + 1 * fruit_juice <= 100, "water_constraint"
model += 1 * lemonade <= 50, "sugar_constraint"
model += 1 * lemonade <= 30, "lemon_juice_constraint"
model += 2 * fruit_juice + 1 * lemonade <= 40, "fruit_puree_constraint"

model.solve()

print("Status:", model.status)
print("Optimal Production of Lemonade:", lemonade.varValue)
print("Optimal Production of Fruit Juice:", fruit_juice.varValue)
