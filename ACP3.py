def findLength(arr):
    if arr == []:
        return 0
    return 1 + findLength(arr[1:])
arr = [10, 20, 30, 40, 50]

print("Length of list :", findLength(arr))