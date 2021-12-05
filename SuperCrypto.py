import PyInstaller
import pyAesCrypt
import os
import sys
import random
from colorama import init, Fore, Back, Style

init()
def console_picture():
    print(Style.BRIGHT + Fore.YELLOW)
    print("                **    **  ********  **        **            **      ")
    print("               **    **  ********  **        **         **     **   ")
    print("              ********  **        **        **         **      **  ")
    print("             ********  ********  **        **         **      **  ")
    print("            **    **  **        **        **         **      **  ")
    print("           **    **  ********  ********  ********    **    **   ")
    print("          **    **  ********  ********  ********       **     \n")
console_picture()

print('Программа шифровки by Pashok ')
print('Выберите действие- ')
action = input('1 - шифрование библиотеки'
               '         2 - расшифровка библиотеки \n')

loop = 0

while loop == 0:
    if action == '1':

        def encryption(file, password):
            buffer_size = 512 * 1024

            pyAesCrypt.encryptFile(str(file), str(file) + '.crp', password, buffer_size)

            print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")
            os.remove(file)


        def walking_by_dirs(dir, password):

            for name in os.listdir(dir):
                path = os.path.join(dir, name)

                if os.path.isfile(path):
                    try:
                        encryption(path, password)
                    except Exception as ex:
                        print(ex)

                else:
                    walking_by_dirs(path, password)


        local = input('Введите путь до директории для шифрования:  '
                      'Пример - C:/Users/Name/****/**** \n')


        def rand_word():
            list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u',
                    'v', 'w', 'x', 'y', 'z']
            return str((random.choice(list) + random.choice(list) + random.choice(list)))


        password = rand_word() + str(random.randrange(100000, 999999)) + rand_word()
        print('Ваш пароль для будущей расшифровки - \n', '***', password, '***\n')

        walking_by_dirs(local, password)
        print('Повторный вывод пароля - ', '***', password, '***')


    if action == '2':

        def decryption(file, password):
            buffer_size = 512 * 1024

            pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)

            print("[Файл '" + str(os.path.splitext(file)[0]) + "' дешифрован]")

            os.remove(file)


        def walking_by_dirs(dir, password):
            for name in os.listdir(dir):
                path = os.path.join(dir, name)

                if os.path.isfile(path):
                    try:
                        decryption(path, password)
                    except Exception as ex:
                        print('Введен неправильный пароль. \n')
                else:
                    walking_by_dirs(path, password)


        local = input('Введите путь до директории:  '
                      'Пример -C:/Users/Name/****/**** \n')
        password = input("Введите пароль для расшифровки: \n")
        walking_by_dirs(local, password)

