"""
Тема 7: “Множества”
	•	Подсчитайте количество уникальных символов в высказывании Уильяма Шекспира:
	 “All the world’s a stage, and all the men and women merely players. They have their exits and their entrances;
	  and one man in his time plays many parts.”
	   (одна и та же буква в разных регистрах считается как один символ).
	   Согласно таблице ASCII какой из символов данного высказывания является минимальным, а какой максимальным?

	•	Дано два множества {1, 2, 3, 4, 5} и {4, 5, 6, 7, 8}. Найти:
	•	объединение множеств
	•	пересечение множеств
	•	симметричную разность множеств
	•	элементы из второго множества, входящие в первое, и удалить их из первого
	•	является ли второе множество супермножеством для {5, 7, 4} и {8, 4, 3}
	•	является ли второе множество правильным супермножеством для {5, 8, 4, 7, 6}

	•	Среди учеников старших классов провели олимпиады по физике и математике.
	 Результаты выглядят следующим образом: на олимпиаде по математике 1 место занял Матвей, 2 место - Евгения,
	 3 место - Михаил, 4 место - Максим и 5 место - Наталья, а в олимпиаде по физике призовая тройка выглядит следующим
	 образом: 1 место - Максим, 2 место - Матвей и 3 место - Александр. Администрацией школы было решено наградить всех
	 победителей, а также особый приз выдать ребятам, занявшим призовые места по двум дисциплинам сразу.
Создайте общий список победителей двух олимпиад. Список призеров в олимпиаде по математике отредактируйте и удалите из
него тех ребят, которые не вошли в тройку призеров в олимпиаде по физике, после чего удалите список призеров по физике.

"""

William = "All the world’s a stage, and all the men and women merely players. They have their exits and their entrances;" \
          " and one man in his time plays many parts."
new_s = William.lower()
print(len(set(new_s)))
max_s = max(new_s)
min_s = min(new_s)
print(max_s)
print(min_s)


first = {1, 2, 3, 4, 5}
second = {4, 5, 6, 7, 8}
join_f_s = first.union(second)
print(join_f_s)
peresechenie = first.intersection(second)
print(peresechenie)
raznost = first.symmetric_difference(second)
print(raznost)
rem_peresech = second.intersection(first)
first = first - rem_peresech
print(first)

third = {5, 7, 4}
fourth = {8, 4, 3}

super1 = second.issuperset(third)
print(super1)
super2 = second.issuperset(fourth)
print(super2)
fifth = {5, 8, 4, 7, 6}
super3 = second > fifth
print(super3)

math = {"Matvei", "Evgenia", "Mihail", "Maksym", "Natalya"}
physics = {"Maksym", "Matvei", "Aleksandr"}
all = math | physics
print("all of them:", set(all))
both = math & physics
print(both)
math = list(math) - list(physics)
print(math)

