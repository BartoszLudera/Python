def draw_ruler(len):
    ruler = "|"
    numbers = "0"

    for i in range(1, len + 1):
        ruler += "....|"
        if i < 10:
            numbers += "    " + str(i)
        else:
            numbers += "   " + str(i)

    print(ruler)
    print(numbers)

len = int(input("Enter the len of the ruler: "))
draw_ruler(len)
