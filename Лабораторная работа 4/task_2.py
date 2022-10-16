def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    char_dict = {}
    for letter in str_.lower():
        if letter.isalpha():
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1
    return char_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

# вторая функция, возвращающая словарь с процентным соотношением символов в словаре
def get_percent(char_dict):
    percent_dict = {}
    total_val = sum(char_dict.values())
    for letter,val in char_dict.items():
        percent_dict[letter] = round(100*val/total_val,3)
    return percent_dict

# print(get_percent(get_count_char(main_str)))