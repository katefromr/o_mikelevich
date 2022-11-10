import os
import sys
import copy
import secrets
import collections

# вводятся числа для первого массива через пробел
list_1 = [int(s) for s in input("Введите через пробел числа для первого массива ").split()]
# вводятся числа для второго массива через пробел
list_2 = [int(s) for s in input("Введите через пробел столько же чисел для второго массива ").split()]
# вводится необходимое количество проверок на наличие совпадений
how_long = int(input("Сколько раз провести сравнение массивов? "))

# создаются две копии массивов, которые будут изменяться в процессе проверок.
# исходные массивы останутся неизменными
brother_of_list_1 = copy.deepcopy(list_1)
sister_of_list_2 = copy.deepcopy(list_2)

# создаётся пустой массив для записи количества будущих совпадений
list_of_matches = []
# создаётся счётчик количества совпадений, который будет после записи в
# массив обнуляться для каждого последующего опыта
counter_of_matches = 0

# далее начинается сравнение массивов
# в каждом опыте делается следующее:
for number in range(how_long):
	# проверяется, соответствуют ли копии своим исходным массивам. Если нет, то они перезаписываются
	if list_1 != brother_of_list_1 or list_2 != sister_of_list_2:
		brother_of_list_1 = copy.deepcopy(list_1)
		sister_of_list_2 = copy.deepcopy(list_2)
	# если копии в порядке, то для каждой позиции в пределах длины массива производятся сравнения
	for number in range(len(list_1)):
		# в переменную а записывается случайно выбранное число из копии первого массива
		a = secrets.choice(brother_of_list_1)
		# и сразу же уаляется из этой копии массива во избежание повторного взятия того же числа
		brother_of_list_1.remove(a)
		# в переменную b записывается случайно выбранное число из копии второго массива
		b = secrets.choice(sister_of_list_2)
		# и сразу же уаляется из этой копии массива во избежание повторной проверки того же числа
		sister_of_list_2.remove(b)
		# если переменные a и b совпали, то в счётчик +1 совпадение и сравнение продолжается
		if a == b:
			counter_of_matches += 1
		else:
			continue
	list_of_matches.append(counter_of_matches)
	counter_of_matches = 0

lets_count = collections.Counter(list_of_matches)

for key in lets_count:
	print(key, " совпадений: ", lets_count[key], ' раз(а), ', lets_count[key] / how_long * 100, "%")

restart = input("Желаете начать с начала? [y/n] > ")
if restart == "y":
	os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
else:
	input("\nНажмите Enter для выхода")
	sys.exit(0)