"""
Тема 8: “Словари”
	•	Перечень сетевых интерфейсов и основная информация о них представлены в виде следующей структуры данных:
	[{‘interface’: ‘Ethernet0’, ‘ip’: ‘1.1.1.1’, ‘status’: ‘up’}, {‘interface’: ‘Ethernet1’, ‘ip’: ‘2.2.2.2’, ‘status’:
	 ‘down’}, {‘interface’: ‘Serial0’, ‘ip’: ‘3.3.3.3’, ‘status’: ‘up’}, {‘interface’: ‘Serial1’, ‘ip’: ‘4.4.4.4’,
	  ‘status’: ‘up’}].
	•	выведите на экран общее количество интерфейсов
	•	выведите на экран информацию (название, ip-адрес и статус), соответствующую второму интерфейсу в списке
	•	выведите на экран статус последнего интерфейса в списке
	•	проверьте, добавлена ли графа ‘notes’ для первого интерфейса и выведите ее содержимое на экран.
	Если такой графы нет, то сперва добавьте ее с текстом “need to reset”
	•	добавьте в список еще один ethernet интерфейс с ip-адресом, как у третьего интерфейса, и статусом ‘down’.
	После этого измените ip-адрес третьего интерфейса на ‘3.3.3.4’
	•	выведите на экран содержимое графы ‘notes’ первого интерфейса, а затем удалите ее
	•	переведите четвертый интерфейс в состояние ‘down’, а затем удалите его из списка
	•	Дан список товаров и их цены: {‘smart watch’: 550, ‘phone’: 1000, ‘playstation’: 500, ‘laptop’: 1550, ‘
	music player’: 600, ‘tablet’: 400}.
	•	выведите на экран общую стоимость всех товаров
	•	выведите на экран названия товаров в алфавитном порядке, а затем наоборот
	•	все музыкальные плееры кроме одного были распроданы, поэтому на последний экземпляр магазин решил сделать
	50% скидку. Внесите соответствующие изменения в список товаров.
	•	сколько планшетов необходимо продать магазину, чтобы превысить выручку, полученную от продажи пяти телефонов
	и трех ноутбуков?
	•	магазин решил провести лотерею среди своих постоянных покупателей. Выберите произвольным образом приз для
	победителя лотереи, а затем удалите его из списка.
	•	в магазин поступило несколько новых устройств: ‘iphone’ - 1300, ‘music player’ - 850, ‘headphones’ - 200.
	Обновите список товаров и их цены.

"""
from math import ceil

net = [{"interface": "Ethernet0", "ip": "1.1.1.1", "status": "up"},
       {"interface": "Ethernet1", "ip": "2.2.2.2", "status": "down"},
       {"interface": "Serial0", "ip": "3.3.3.3", "status": "up"},
       {"interface": "Serial1", "ip": "4.4.4.4", "status": "up"}]
print(len(net))
print(net[1])
print(net[-1])

net[0].setdefault("notes", "need to reset")
print(net[0])

net.append({"interface": "Ethernet2", "ip": net[2]["ip"], "status": "down"})
net[2]["ip"] = " 3.3.3.4"
print(net)

print(net[0]["notes"])
print(net[0].pop("notes"))
print(net)

net[3]["status"] = "down"
print(net[3])
del net[3]
print(net)

s = {"smart watch": 550, "phone": 1000, "playstation": 500, "laptop": 1550, "music player": 600, "tablet": 400}

print(sum(s.values()))
print(sorted(s.keys()))
print(sorted(s.keys(), reverse=True))
s["music player"] = int(s["music player"] * 0.5)
print(s)

sum = 5 * s["phone"] + 3 * s["laptop"]
count_tablet = sum / s["tablet"]
print(ceil(count_tablet))

print(s.popitem())
print(s)

s.update({"iphone": 1300, "music player": 850, "headphones": 200})
print(s)


