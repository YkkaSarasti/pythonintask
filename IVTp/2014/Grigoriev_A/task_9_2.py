﻿#Задача 9. Вариант 2.
#1-50. Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.

#Григорьев А.О.
#10.04.2016
import random
words = ("питон","анаграмма","простая","сложная","ответ","подстаканник")
word=random.choice(words)
dlin=len(word)
live=5
print('''
                    Игра угадай слово.
    Компьютер загадывает слово. Вы должны угадать его.
                   У вас есть 5 жизней.
                         Удачи!
''')
print("Длинна слова",dlin)
vvod=input("Введите букву:")

while vvod!=word or live==0:
    if(vvod in list(word)):
        print("Да")
        live-=1
        print("Осталось {} жизней".format(live))
    else:
        print("Нет")
        live-=1
        print("Осталось {} жизней".format(live))
    if(live==0):
        break
    vvod=input("Введите букву:")
while vvod !=word:
    input("Введите слово: ")
input("\n\nНажмите Enter, чтобы выйти")