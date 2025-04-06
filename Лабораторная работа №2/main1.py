money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
i = salary - spend + money_capital #бюджет в первый месяц
#print(i, spend)
time = 1 #первый месяц
while True: #бюджет второго месяца
    j = spend * (1 + increase)
    i = salary - j + i
    #print(i, j)
    while True: #бюджет с третьего месяца
        j = j * (1 + increase)
        i = salary - j + i
        #print(i, j)
        time += 1 #количество месяцев
        if i < 0:
            break
    if i < 0:
        break
print("Количество месяцев, которое можно протянуть без долгов:", time)
