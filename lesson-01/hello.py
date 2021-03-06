is_student = True

name = input('Введите имя:')
print('Hello,', name, '!')

# Что такое тип данных?

"""
Сколько памяти отводится, какие операции можно производить с объектами.
Скалярные типы данных: только одно значение переменная может хранить в один момент времени (хранится в stack).
	bool -- логический (Истина/Ложь -- True/False);
	int -- целочисленный;
	float -- с плавающей точкой (дробный);
	str -- строковый.
"""
i1 = 555
i2 = 0x59 # шестнадцатеричная СС (x is for hex)
i3 = 0b10101 # двоичная (b is for binary)
i4 = 0o255 # восьмеричная (o is for octave)

f1 = 1.23
f2 = 12e-3
f3 = 12e-3

s1 = 'Some\n' # \n -- перенос строки
s2 = "Something" # разницы между кавычками нет, но удобнее пользоваться одинарными. Или экранировать возможные двойные внутри строки: \"
s3 = r'Raw string' # сырые строки -- Питон не производит манипуляций со строкой (не экранировал и т.д.)
s4 = u'Hello' # Unicode-строка. В третьем Питоне все строки юникодные, а во втором по умолчанию -- нет.
# bytes -- байтовая строка:
s5 = b'byte' # строка без кодировки, просто набор байтов.
# Для переноса строки:
s6 = '''

'''
s7 = """
1.      848n
""" # все пробелы и прочее останутся.

# Комплексные числа -- complex
c1 = 3.14j


# Структурированные (сложные)

# Могут одновременно содержать много значений разных типов -- как скалярных, так и структурированных же.
# tuple, list, set, dict, object

# Кортежи -- tuple
t1 = (1,)
t2 = (True, 6, 1.3, 'string', (1,2,3))

# Списки -- list
lst1 = [[1], [2], 3, False]

# Множества -- set
set1 = {1, 2, 3.14, True, 'str'}
set2 = set() # пустое множество

# Элементы в множестве не повторяются: написав {1, 2, 3, 3, 3}, на выходе получим 1, 2, 3. Так можно оставить только уникальные данные в наборе.
# К элементам кортежей и списков обращаемся так:

print(t2[1]) # нумерация с нуля, это обратились к шестёрке в t2
print(t2[1], lst1[2], lst1[0][0]) # последнее -- обращение к эл-ту вложенного списка

# Словари -- dict

d = {
	'id': 1,
	'name': 'Вася',
	'is_student': True,
	'skills': ('python', 'linux')
}

# Специальный тип данных None -- пустота

a = None