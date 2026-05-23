def takeInput():

    num = int(input("Enter a number : "))
    if num < 0:
        print("Negative number entered")
        return

    print("You entered :", num)
    takeInput()
takeInput()