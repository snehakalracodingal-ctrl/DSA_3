
# Change Calculator Program

amount = int(input("Enter the amount: "))

ways = 0
coins = [1, 2, 5]

# Count ways using loops
for one in range(amount + 1):
    for two in range(amount // 2 + 1):
        for five in range(amount // 5 + 1):

            total = (one * 1) + (two * 2) + (five * 5)

            if total == amount:
                ways += 1

print("Number of ways =", ways)