"""
Тема 6: “Бинарные последовательности”
	•	Дана байтовая строка. Заменить в ней все вхождения первого символа на знак доллара $, кроме самого первого символа.
	 Например, строка b’restart’ должна превратиться в строку b’resta$t’.

	•	Дана строка: “Th$e *ly-ri cs; i!s >no>t *th&at$ p=oo+r!$”. Представить данную строку в виде массива байт и
	 удалить из нее каждый третий символ, начиная с третьего. Вывести полученную строку на экран.

	•	Вам пришло закодированное методом cp037 сообщение:
 '\xe6\x88\x81\xa3@\x89\xa2@\xa8\x96\xa4\x99@\x86\x81\xa5\x96\xa4\x99\x89\xa3\x85@\x97\x99\x96\x87\x99\x81\x94\x94
 \x89\x95\x87@\x93\x81\x95\x87\xa4\x81\x87\x85o'.

Напишите ответ и закодируйте его тем же методом. В случае возникновения ошибки кодирования-декодирования, проигнорируйте ее.
"""
byte_str = b'fulloforfdeff'
first_byte_str = byte_str[0:1]
print(first_byte_str)
new_byte_str = first_byte_str + byte_str[1:].replace(first_byte_str, b"$")
print(new_byte_str)

stroka = "Th$e *ly-ri cs; i!s >no>t *th&at$ p=oo+r!$"
array_stroka = bytearray(stroka.encode())
print(array_stroka)
del array_stroka[2::3]
print(array_stroka.decode())

coded_msg = b'\xe6\x88\x81\xa3@\x89\xa2@\xa8\x96\xa4\x99@\x86\x81\xa5\x96' \
            b'\xa4\x99\x89\xa3\x85@\x97\x99\x96\x87\x99\x81\x94\x94\x89\x95' \
            b'\x87@\x93\x81\x95\x87\xa4\x81\x87\x85o'
encoded_msg = coded_msg.decode(encoding="cp037")
print(encoded_msg)
answer = "Python!"
print(answer.encode(encoding="cp037"))
