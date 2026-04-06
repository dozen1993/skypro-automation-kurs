def is_year_leap(year):
    return True if year%4==0 else False

meaning_year= int(input('Введите год'))
result=(is_year_leap(meaning_year))
print(result)