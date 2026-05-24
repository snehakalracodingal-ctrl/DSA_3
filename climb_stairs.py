def ways(stairs):

    if stairs < 0:
        return 0

    elif stairs == 0:
        return 1

    else:
        return ways(stairs-1) + ways(stairs-2)


stairs = int(input("Enter number of steps : "))

print("Number of ways to climb :", ways(stairs))