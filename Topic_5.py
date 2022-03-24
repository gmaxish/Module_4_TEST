"""
Тема 5: “Текстовые последовательности”
	•	Напишите программу, которая позволит выполнять проверку пароля на сложность в соответствии со следующими критериями:
	•	длина пароля не менее 5 символов
	•	содержит буквы латинского алфавита как в верхнем, так и в нижнем регистре: A-Z, a-z
	•	содержит цифры от 0 до 9
	•	содержит хотя бы один из символов: @, #, %, &

	•	Вы находитесь в квест-комнате по мультфильму WALL-E! Вы нашли записку:
"In a distant, but not so unrealistic, future where mankind has abandoned earth because it has become covered
 with trash from products sold by the powerful multi-national Buy N Large corporation, WALLE,
  a garbage collecting robot has been left to clean up the mess. Mesmerized with trinkets of Earth's
  history and show tunes, WALLE is alone on Earth except for a sprightly pet cockroach. One day, EVE,
   a sleek (and dangerous) reconnaissance robot, is sent to Earth to  find proof that life is once again sustainable."
Чтобы выбраться из комнаты, необходимо выполнить следующие шаги:
	•	вывести на экран длину текста в обнаруженной записке
	•	вывести на экран весь текст в нижнем регистре
	•	заменить все вхождения некорректно написанного имени WALLE на его правильную форму WALL-E.
	•	подсчитать, сколько раз в тексте было использовано слово Earth.

"""
pswd = "psWd1"

rule_1 = len(pswd) >= 5
rule_2 = not pswd.isupper() and not pswd.islower()
rule_3 = len({"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"} & set(pswd)) > 0
rule_4 = len({"@", "#", "%", "&"} & set(pswd)) > 0

result = (rule_1 and rule_2 and rule_3 and rule_4)
print(result)

letter = "In a distant, but not so unrealistic, future where mankind has abandoned earth because it has become covered" \
         "with trash from products sold by the powerful multi-national Buy N Large corporation, WALLE, a garbage" \
         " collecting robot has been left to clean up the mess. Mesmerized with trinkets of Earth's history and show" \
         " tunes, WALLE is alone on Earth except for a sprightly pet cockroach. One day, EVE, a sleek (and dangerous)" \
         " reconnaissance robot, is sent to Earth to  find proof that life is once again sustainable."
print("Длина текста: ", len(letter))
print(letter.lower())
print(letter.replace("WALLE", "WALL-E"))
print(letter.count("Earth"))



