
def debug_print(debug_msg=None, **kwargs):

    if debug_msg:
        print(debug_msg)

    for key, value in kwargs.items():
        print("{}: {}".format(key, value))


def mergesort(array):
<<<<<<< HEAD
=======
    debug_print(array=array)
>>>>>>> dd8c56cede9b109c1df7bda13abc1b1b7b79ed0b
    if len(array) <= 1:
        return array

    m = len(array) // 2
<<<<<<< HEAD
=======
    debug_print(m=m)
>>>>>>> dd8c56cede9b109c1df7bda13abc1b1b7b79ed0b

    left = mergesort(array[:m])
    right = mergesort(array[m:])

    return merge(left, right)


def merge(left, right):
<<<<<<< HEAD
=======
    debug_print(debug_msg="Merging...", left=left, right=right)

>>>>>>> dd8c56cede9b109c1df7bda13abc1b1b7b79ed0b
    merged = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    if len(left) > 0:
        merged += left
    else:
        merged += right

<<<<<<< HEAD
=======
    debug_print(merged=merged)
>>>>>>> dd8c56cede9b109c1df7bda13abc1b1b7b79ed0b
    return merged


if __name__ == "__main__":
    input_str = input("Enter numbers, separated by ',': ")
<<<<<<< HEAD
    input_list = input_str.split(",")
=======

    input_list = input_str.split(",")
    debug_print(input_list=input_list)

>>>>>>> dd8c56cede9b109c1df7bda13abc1b1b7b79ed0b
    value_list = []
    for x in input_list:
        try:
            value_list.append(int(x))
        except ValueError as err:
            print("Invalid input.")
            quit(1)

<<<<<<< HEAD
=======
    debug_print(value_list=value_list)

>>>>>>> dd8c56cede9b109c1df7bda13abc1b1b7b79ed0b
    sorted_list = mergesort(value_list)
    print(sorted_list)
