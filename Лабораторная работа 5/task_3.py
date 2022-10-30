from random import randint

def get_unique_list_numbers() -> list[int]:
    ... # TODO написать функцию для получения списка уникальных целых чисел

    list_ = []
    for i in range(15):
        rand = randint(-10, 10)
        while rand in list_:
            rand = randint(-10, 10)
        list_.append(rand)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
