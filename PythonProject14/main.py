per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input()
money = int(money)
d = list(per_cent.values())
d1 = int(d[0] * money / 100)
d2 = int(d[1] * money / 100)
d3 = int(d[2] * money / 100)
d4 = int(d[3] * money / 100)
dep = [d1, d2, d3, d4]
print("deposites =", dep)
print(dep.index(max(dep)))