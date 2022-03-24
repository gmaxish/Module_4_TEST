"""
Тема 4: “Последовательности”
	1•	Дан список, состоящий из 4х элементов: ‘abc’, ‘xyz’, ‘aba’, ‘1221’.
	Проверить для каждого элемента выполнение следующих условий: длина элемента больше 2х
	и первый и последний символ у него совпадают.

	2•	Дан список цветов: ‘red’, ‘green’, ‘white’, ‘black’, ‘pink’, ‘yellow’.
	 Создайте еще один список и переместите в него 1-ый, 5-ый и 6-ой элементы.

	3•	Даны несколько списков: [-8, 1, 2, -2, 0], [1, 1, 0, 0, 2, -2, -2],
	[1, -1, 0, -9, 4, -5], [1, 4, 0, 23, 6, 34].
	 Для каждого из списков найти второе наименьшее значение в нем (правильные ответы выделены жирным шрифтом).

	4•	Дан список гостей, посетивших вечеринку, причем гости в этом списке располагаются в порядке их прибытия:
	 Adela, Fleda, Owen, May, Mona, Gilbert, Ford (Adela приехала на вечеринку первая, а Ford - последний).
	  Гость, прибывший после того, как половина гостей уже была на вечеринке, считается в меру опоздавшим,
	   в то время как гость, прибывший последним, считается опоздавшим неприлично.
	   Определите, попадают ли в одну из этих категорий (и если да, то в какую) следующие гости: May, Fleda, Gilbert и Ford.

	5•	Спортивный обозреватель хранит записи о каждой спортивной команде следующим образом:
	 первым в списке идет имя тренера команды, затем - капитана, и далее имена всех участников в соответствии
	  с их порядковым номером игрока. Также у него имеется список всех спортивных команд, первое место в котором
	   занимает лучшая команда, и далее по убывающей к самой худшей. Выведите на экран имя капитана худшей команды.

	6•	Дано некоторое целое число. Вывести на экран сумму всех целых чисел от 0 и до заданного числа включительно.
"""

print("#1_____________________")
sp = ["abc", "xyz", "aba", "1221"]
e1 = sp[0]
print(e1, len(e1) > 2 and e1[0] == e1[-1])
e1 = sp[1]
print(e1, len(e1) > 2 and e1[1] == e1[-1])
e1 = sp[2]
print(e1, len(e1) > 2 and e1[2] == e1[-1])
e1 = sp[3]
print(e1, len(e1) > 2 and e1[3] == e1[-1])


print("#2_____________________")
spisok = ["red", "green", "white", "black", "pink", "yellow"]
element1 = spisok.__getitem__(0)
element2 = spisok.__getitem__(4)
element3 = spisok.__getitem__(5)

new_spisok = [element1, element2, element3]

print(new_spisok)
print("")

print("#3_____________________")
spisok1 = [-8, 1, 2, -2, 0]
spisok2 = [1, 1, 0, 0, 2, -2, -2]
spisok3 = [1, -1, 0, -9, 4, -5]
spisok4 = [1, 4, 0, 23, 6, 34]

spisok1 = sorted(set(spisok1))
spisok2 = sorted(set(spisok2))
spisok3 = sorted(set(spisok3))
spisok4 = sorted(set(spisok4))


print(spisok1)
min_spisok1 = min(spisok1[1:])
print(min_spisok1)
print(spisok2)
min_spisok2 = min(spisok2[1:])
print(min_spisok2)
print(spisok3)
min_spisok3 = min(spisok3[1:])
print(min_spisok3)
print(spisok4)
min_spisok4 = min(spisok4[1:])
print(min_spisok4)
print("")

print("#4_____________________")
guests = ["Adela", "Fleda", "Owen", "May", "Mona", "Gilbert", "Ford"]
print(len(guests))
less_latest = guests[4:]
print(less_latest)

latest = guests[-1:]
print(latest)
print("")

print("#5_____________________")

team1 = ["Ivan", "Sergei", "Maksym", "Aleksei", "Darina"]
team2 = ["Sergei", "Dima", "Jenya", "Ira", "Yra"]
team3 = ["Nikalay", "Ruslan", "Dima", "Anya", "Nikita"]

print(team3[1:2])
print("")

print("#6_____________________")
s = 56

l = range(0, s+1)
sum_l = sum(l)
print(sum_l)
