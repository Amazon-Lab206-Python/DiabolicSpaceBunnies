def oddeven():
    for x in range(1, 20):
        if x % 2 == 0:
            print x, "number is {}, this is an even number."
        else:
            print x, "number is {}, this is an odd number."


oddeven()


def multiply_5(arr, num):
    for y in range(0, len(arr)):
        arr[y] *= num
    return arr


numbers_array = [1, 3, 5, 7]
print multiply_5(numbers_array, 5)
