money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
# если сначала расходы покрыть подушкой безопасности, а в конце прибавить ЗП к подушке
while money_capital >= spend:
    money_capital -= spend - salary
    spend *= 1 + increase
    month += 1

print(month)
