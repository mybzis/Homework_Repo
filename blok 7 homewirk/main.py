# Number 1 & 2

# Импортируем модуль datetime для работы с датами
import datetime

# Определяем функцию date_range с двумя параметрами: start_date и end_date
def date_range(start_date, end_date):
    # Создаем пустой список для хранения дней
    days = []
    # Пытаемся преобразовать строки start_date и end_date в объекты datetime
    try:
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    # Если возникает ошибка ValueError, значит формат дат неверный
    except ValueError:
        # Возвращаем пустой список
        return days
    # Проверяем, что start_date не больше end_date
    if start > end:
        # Возвращаем пустой список
        return days
    # Используем цикл while для перебора дней от start_date до end_date
    while start <= end:
        # Добавляем текущий день в формате YYYY-MM-DD в список days
        days.append(start.strftime("%Y-%m-%d"))
        # Прибавляем один день к текущему дню
        start += datetime.timedelta(days=1)
    # Возвращаем список days
    return days

# Пример использования функции date_range с корректными датами
print(date_range("2023-10-23", "2023-10-31"))
# Вывод: ['2023-10-23', '2023-10-24', '2023-10-25', '2023-10-26', '2023-10-27', '2023-10-28', '2023-10-29', '2023-10-30', '2023-10-31']

# Пример использования функции date_range с некорректными датами
print(date_range("2023-13-23", "2023-10-31"))
# Вывод: []



# 3


# Импортируем модуль datetime для работы с датами
import datetime

# Определяем функцию check_dates с одним параметром: stream
def check_dates(stream):
    # Создаем пустой список для хранения результатов проверки
    results = []
    # Используем цикл for для перебора дат в потоке
    for date in stream:
        # Пытаемся преобразовать строку date в объект datetime
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
            # Если нет ошибки ValueError, значит дата корректна
            results.append(True)
        # Если возникает ошибка ValueError, значит дата некорректна
        except ValueError:
            results.append(False)
    # Возвращаем список results
    return results

# Пример использования функции check_dates с данным потоком дат
print(check_dates(['2018-04-02', '2018-02-29', '2018-19-02']))
# Вывод: [True, False, False]
