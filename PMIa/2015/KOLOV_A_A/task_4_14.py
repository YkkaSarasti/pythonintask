﻿# Задача 4. Вариант 14.
# Напишите программу, которая выводит имя, под которым скрывается Михаил Ефимович Фрилянд. Дополнительно необходимо вывести область интересов указанной личности, место рождения, 
# годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). 
# Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Kolov A.A
# 27.04.2016

name = "Моисей Фридлянд"
alias = "Михаил Ефимович Фридлянд"
dateBirth = 1898
dateDeath = 1940
placeBirth = "Киев"
hobbies = "журналист, писатель, общественный деятель"
ageDeath = dateDeath - dateBirth

print(name+"("+alias+")")
print("Направлоения деятальности: " + hobbies)
print("Родился в " + str(dateBirth) + " году")
print("Скончался в " + str(dateDeath) + " году "+ "в возрасте " +str(ageDeath)+" лет")
input("Нажмите Enter")