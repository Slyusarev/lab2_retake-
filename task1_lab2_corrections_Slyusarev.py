salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
all_spend = 0
spend_list = []
for i in range (months):
    all_spend = spend * (1+0.03)**i
    spend_list.append(all_spend)
money_capital = sum(spend_list) - salary * months

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
if money_capital > round(money_capital):
    print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital)+1)
else: print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
