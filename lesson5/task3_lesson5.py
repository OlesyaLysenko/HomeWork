# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32


with open('text_3.txt', 'r', encoding="UTF-8") as file:
    surnames = []
    medium_salary = 0
    salary = 0
    for line in file:
        salary += 1
        surname, salary = (i for i in line.split())
        salary = float(salary)
        if salary < 20000:
            surnames.append(surname)
        medium_salary += salary
    medium_salary /= salary
print(*surnames, sep="\n")
print(medium_salary)
file.close()