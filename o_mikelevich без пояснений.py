import os
import sys
import copy
import secrets
import collections
list_1 = [int(s) for s in input("Введите через пробел числа для первого массива ").split()]
list_2 = [int(s) for s in input("Введите через пробел столько же чисел для второго массива ").split()]
brother_of_list_1 = copy.deepcopy(list_1)
sister_of_list_2 = copy.deepcopy(list_2)
counter_of_matches = 0
lets_count1 = collections.Counter(dict.fromkeys(list_1,0))
lets_count1[0] = 0
lets_count = collections.OrderedDict(sorted(lets_count1.items(), key=lambda t: t[0]))

how_long = int(input("Сколько раз провести сравнение массивов? "))
for number in range(how_long):
    if list_1 != brother_of_list_1 or list_2 != sister_of_list_2:
        brother_of_list_1 = copy.deepcopy(list_1)
        sister_of_list_2 = copy.deepcopy(list_2)
    for number in range(len(list_1)):
        a = secrets.choice(brother_of_list_1)
        brother_of_list_1.remove(a)
        b = secrets.choice(sister_of_list_2)
        sister_of_list_2.remove(b)
        if a == b:
            counter_of_matches += 1
        else:
            continue
    for key in lets_count:
        if key == counter_of_matches:
            lets_count[key] += 1
            break
    counter_of_matches = 0

for key in lets_count:
    print(key, " совпадений: ", lets_count[key], ' раз(а), ', round(lets_count[key]/how_long*100, 5), "%")

restart = input("Желаете начать с начала? [y/n] > ")
if restart == "y":
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
else:
    input("\nНажмите Enter для выхода")
    sys.exit(0)