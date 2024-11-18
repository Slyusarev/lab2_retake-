money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months_counter = 0  # Количество месяцев, которое можно прожить без долгов
spend_list = []
while money_capital >= 0:
    money_capital += salary - spend  # Уменьшаем подушку безопасности
    months_counter += 1
    spend *= (1 + increase)
    if money_capital >= 0:
        spend_list.append(money_capital)

print("Количество месяцев, которое можно протянуть без долгов:", len(spend_list))