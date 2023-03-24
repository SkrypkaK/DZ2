# 1. Напишите функцию, которая будет вычислять выражение от двух переменных по следующим правилам:
#    f(x, y) = 2 * x + y     | x > 10, y > 10
#    f(x, y) = x + 2 * y + 1 | x > 5
#    f(x, y) = -x - y        | x > 0
#    f(x, y) = x / y         | Для всех остальных случаев
#   Примечание: Не забудьте, что на 0 делить нельзя! В случае ошибки верните строку "Error"
# def f(x, y):
#     pass
#
# def test_f():
#     def test_f(x, y):
#         if x > 10 and y > 10:
#             return 2 * x + y
#         elif x > 5:
#             return x + 2 * y + 1
#         elif x > 0:
#             return -x - y
#         else:
#             try:
#                 return x / y
#             except ZeroDivisionError:
#                 return "Error"



# 2. Напишите функцию, которая определяет, является ли введённый год високосным.
# Високосным является год, номер которого кратен или 4, или 400.
# Обратите внимание, что год, который кратен 100, но не (например 1700, 1800, 2100, 2300) високосным не является.
# При вводе отрицательного числа верните строку "Error"
#
# Подсказка: вам потребуется функция, возвращающая остаток от деления одного числа на другое
# Это функция %. Например, 4 % 2 вернёт 0, а 5 % 2 вернёт 1

# def is_leap_year(year):
#     if year < 0:
#         return "Error"
#     elif year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     if year % 4 == 0:
#         return True
#     else:
#         return False
#
# def test_is_leap_year():
#     assert is_leap_year(2000) == True
#     assert is_leap_year(1900) == False
#     assert is_leap_year(1600) == True
#     assert is_leap_year(2016) == True
#     assert is_leap_year(2018) == False
#     assert is_leap_year(-4) == "Error"

# 3. Напишите функцию, которая принимает дату в формате (год, месяц, день) и определяет её корректность.
# # Подсказка: Не забудьте про високосные года.

# def is_correct_date(year, month, day):
#     pass
# def is_correct_date(year, month, day):
#     if year < 1 or month < 1 or month > 12 or day < 1:
#         return False
#     days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap_year(year):
#         days_in_month[1] = 29
#     if day > days_in_month[month-1]:
#         return False
#     return True
# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# def test_is_correct_date():
#     assert is_correct_date(-2020, 1, 1) == False
#     assert is_correct_date(2020, -1, 1) == False
#     assert is_correct_date(2025, 1, -1) == False
#     assert is_correct_date(2025, 1, 1) == True
#     assert is_correct_date(2025, 2, 29) == False
#     assert is_correct_date(2024, 2, 29) == True
#     assert is_correct_date(2023, 3, 31) == True
#     assert is_correct_date(2023, 4, 31) == False
#     assert is_correct_date(2023, 8, 31) == True
#     assert is_correct_date(2023, 8, 32) == False
#     assert is_correct_date(2023, 9, 30) == True
#     assert is_correct_date(2023, 9, 31) == False
#     assert is_correct_date(2023, 12, 0) == False
#     assert is_correct_date(342, 1, 31) == True

# 4. Напишите функцию, которая будет перемножать все числа от N до M (для простоты предположим, что N всегда не больше M)
# def multiplyNM(n,m):
#     aggregator =1
#     for  i in range(n,m +1):
#         aggregator *= i
#     return aggregator
#
# def test_multiplyNM():
#     assert multiplyNM(1, 5) == 120
#     assert multiplyNM(-1, 5) == 0
#     assert multiplyNM(-7, -3) == -2520
#     assert multiplyNM(10, 20) == 6704425728000
#     assert multiplyNM(3, 3) == 3

# 5. Напишите функцию, которая будет считывать числа с консоли и печатать его, умножив на 2
# Программа должна работать до тех пор, пока не будет введено число 0, после чего выводить "Done" и завершать работу
#
while True:
    number = int(input("Enter a number (enter 0 to exit): "))
    if number == 0:
        print("Done")
        break
    else:
        print(number * 2)

if __name__ == "__main__":
    # test_is_leap_year()
    # test_is_correct_date()
    # test_f()
    # test_multiplyNM()
