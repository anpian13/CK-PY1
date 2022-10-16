src = not False and True or False and not True

# TODO расписать упрощение выражения

# src = (not False) and True or False and (not True)
# избавляемся от отрицаний
# src = ((True) and True) or (False and (False))
# избавляемся от И
# src = (True) or (False)
# избавляемся от ИЛИ

src_new = True

result = src_new  # TODO подставить результат выражения

print(src == result)
