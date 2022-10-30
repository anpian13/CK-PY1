from random import sample
import string

def get_random_password(n: int = 8) -> str:
    ...  # TODO написать функцию генерации случайных паролей
    whole_str = string.digits + string.ascii_letters
    return ''.join(sample(whole_str, n))

print(get_random_password())