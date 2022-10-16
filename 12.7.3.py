per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4}
money = int(input('Введите сумму депозита: '))
a = int(money / 100 * per_cent['ТКБ'])
b = int(money / 100 * per_cent['СКБ'])
c = int(money / 100 * per_cent['ВТБ'])
d = int(money / 100 * per_cent['СБЕР'])
deposit = [a, b, c, d]
print(deposit)
