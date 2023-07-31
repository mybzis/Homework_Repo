# bucks = int(input("Введите вашу зарплату(месяц): "))
# ipo_percent = int(input("Сколько процентов от з\п уходит на ипотеку: "))
# life_percent = int(input("Сколько процентов от з\п уходит на жизнь: "))
# premia = int(input("Сколько раз приходит премия в год: "))

# god = 0
# god = int(12 * (bucks - 0.01 * ipo_percent * bucks - 0.01 * life_percent * bucks) + 0.5 * premia * bucks)

# ipoteka = 0
# ipoteka = int(12 * (bucks - (bucks - 0.01 * ipo_percent * bucks)))

# print(f"Было накоплено {god} рублей и выплачено {ipoteka} рублей из ипотеки")

# # bucks = 100000
# # y = 30

# # month = bucks - 0.01 * ipo_percent * bucks
# # ipo =int(bucks - (bucks - 0.01 * ipo_percent * bucks))

# # # print(12 * ipo)


# # year = int(12 * (bucks - (bucks - 0.01 * ipo_percent * bucks)))
# # print(year)


# phrase_1 = input("Введите первую фразу: ")
# phrase_2 = input("Введите вторую фразу: ")

# if len(phrase_1) > len(phrase_2):
#   print("Фраза 1 длиннее фразы 2")

# if len(phrase_1) < len(phrase_2):
#   print("Фраза 2 длиннее фразы 1")

# else:
#   print("Фразы равной длины")

# Получаем год в виде числа
year = int(input("Введите год: "))

# Проверяем условия для високосного года
if year % 4 == 0:
    # Если год делится на 4 без остатка, то он может быть високосным
    if year % 100 == 0:
        # Если год делится на 100 без остатка, то он может быть не високосным
        if year % 400 == 0:
            # Если год делится на 400 без остатка, то он високосный
            print("Високосный год")
        else:
            # Если год не делится на 400 без остатка, то он не високосный
            print("Обычный год")
    else:
        # Если год не делится на 100 без остатка, то он високосный
        print("Високосный год")
else:
    # Если год не делится на 4 без остатка, то он не високосный
    print("Обычный год")
