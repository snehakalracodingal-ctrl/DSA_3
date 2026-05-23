# Program to check if number is power of 2 using recursion

n = int(input("Enter your number : "))

def checkIfPower(n):

    # if number is less than or equal to 0
    if n <= 0:
        return False

    # base case
    if n == 1:
        return True

    # if divisible by 2 continue recursion
    if n % 2 == 0:
        return checkIfPower(n // 2)

    return False


if checkIfPower(n):
    print("Power of 2")
else:
    print("Not power of 2")