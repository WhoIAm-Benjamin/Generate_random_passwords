from random import choice as c
from threading import Thread as Th
from time import sleep as sl
from os.path import exists as e
from sys import argv as a

passwords = None

def joiner():
    global passwords
    try:
        with open('passwords.txt', 'r', encoding = 'utf-8') as f:
            passwords = f.read().split('\n')
    except FileNotFoundError:
        passwords = []

def checker():
    ############################### сделать разделение файлов по именам для дальнейшей подстановки в MEDUSA
    if not e('passwords.txt'):
        open('passwords.txt', 'w').close()
        ind = 0
    else:
        ind = len(passwords)
    while True:
        sl(30)
        l = len(passwords)
        with open('passwords.txt', 'a', encoding = 'utf-8') as f:
            for i in range(ind, l):
                f.write(passwords[i] + '\n')
            ind = l

def generator():
    joiner()
    try:
        length = a[1]
    except IndexError:
        length = 8
    alphabet = '0123456789abcdefjhigklmnopqrstuvwxyzABCDEFJHIGKLMNOPQRSTUVWXYZ' \
               'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    length_passwords = 0
    while True:
        password = ''
        for i in range(0, length):
            password += c(alphabet)
        if password not in passwords:
            passwords.append(password)
        if len(passwords) == length_passwords + len(alphabet) ** length:
            length += 1

def main():
    th1 = Th(target = generator)
    th2 = Th(target = checker)
    th1.start()
    th2.start()

if __name__ == '__main__':
    main()