list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

ind_max = 0

# find max
for ind,val in enumerate(list_numbers):
    if val > list_numbers[ind_max]:
        ind_max = ind

list_numbers[ind_max],list_numbers[-1] = list_numbers[-1],list_numbers[ind_max]

print(list_numbers)
