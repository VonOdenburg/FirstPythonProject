# Write your code here
items = (
    ("Bubblegum", 202),
    ("Toffee", 118),
    ("Ice cream", 2250),
    ("Milk chocolate", 1680),
    ("Doughnut", 1075),
    ("Pancake", 80))

print("Earned amount:")

income = 0

for item in items:
    print(item[0] + ": $" + str(item[1]))
    income += item[1]

print()
print("Income: $" + str(income))

print("Staff expenses:")
staff = int(input())
print("Other expenses:")
other = int(input())

print("Net income: $" + str(income - staff - other))
