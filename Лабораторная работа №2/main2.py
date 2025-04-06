salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital_1 = salary - spend #подушка на первый месяц
j = spend * (1 + increase) #пересчёт расходов на второй месяц
money_capital_2 = salary - j #подушка на второй месяц
total = 0
for m in range(3,months+1): #подушка с третьего месяца
    j = j * (1 + increase)
    money_capital = salary - j
    total += money_capital #подушка в период с третьего по десятый месяц
money_capital_total = round(-(total + money_capital_2 + money_capital_1), 2)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital_total)
