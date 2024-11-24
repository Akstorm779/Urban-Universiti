my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

Nstr = 0

while Nstr < len(my_list):

    if my_list[Nstr] < 0:
        break

    if my_list[Nstr] > 0:
        print(my_list[Nstr])

    Nstr += 1