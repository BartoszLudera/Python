def reversing(L, left, right):
    left = int(left)
    right = int(right)

    i = 0
    half = (right - left) // 2
    while i <= half:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp

        left += 1
        right -= 1
        i += 1

def reversing_recursive(L, left, right):

    if left >= right:
        return

    left = int(left)
    right = int(right)

    temp = L[left]
    L[left] = L[right]
    L[right] = temp

    reversing_recursive(L, left + 1, right - 1)

print("Enter the elements of the array, '-' ends the input")

L = []

while True:
    input_element = input('?> ')
    if input_element == '-':
        break
    L.append(input_element)

print("Entered list:")
print(L)

left_element = input("Enter the starting element: ")
right_element = input("Enter the ending element: ")

print("Reversed list:")
reversing(L, left_element, right_element)
print(L)

print("Reversed list using recursion:")
reversing_recursive(L, left_element, right_element)
reversing_recursive(L, left_element, right_element)
print(L)
