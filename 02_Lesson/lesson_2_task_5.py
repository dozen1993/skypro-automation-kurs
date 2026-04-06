def month_to_season(n):
    if 1 <= n <=2 or n == 12:
        print('Это зимний месяц')
    elif 3<= n <=5:
        print('Это весенний месяц')
    elif 6<= n <=8:
        print('Это летний месяц')
    elif 9<= n  <=11:
        print('Это осенний месяц')
    else:print('Такого месяца не существует')
month_number=int(input('Введите номер месяца: '))
month_to_season(month_number)