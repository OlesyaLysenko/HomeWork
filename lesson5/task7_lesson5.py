# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
with open('text_7.txt', 'r', encoding='UTF-8') as file:
    profit = {}
    aver_profit = {}
    total_profit = 0
    plus_profit = 0
    i = 0

    for line in file:
        name, firm, revenue, expenses = line.split()
        profit[name] = int(revenue) - int(expenses)
        if profit.setdefault(name) > 0:
            plus_profit = plus_profit + profit.setdefault(name)
            i += 1
    if i != 0:
        total_profit = plus_profit / i
        print(f'Прибыль компаний составляет: {total_profit:.2f}')
    else:
        print(f'Прибыль отсутствует. Компании работают в убыток.')
    aver_profit = {'Средняя прибыль': round(total_profit)}
    profit.update(aver_profit)
    print(f'Прибыль каждой компании - {profit}')

    with open('text_7.txt', 'w') as write_js:
        json.dump(profit, write_js)

        js_str = json.dumps(profit)
        print(f'Создан файл с расширением json со следующим содержимым: \n '
              f' {js_str}')