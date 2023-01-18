# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import groupby, starmap
from os import path


def new_file(text="text.txt"):
    if path.exists(text):
        with open(text, "w", encoding="utf-8") as file:
            S = str(input("Введите строку: "))
            file.write(f"{S}\n")
    else:
        print("File {text} doesn't foud")

def rle_coding(text="text.txt", code_text="code_text.txt"):
    if path.exists(text):
        with open(text) as my_f_1, \
                open(code_text, "w") as my_f_2:
            for i in my_f_1:
                my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("File {text} doesn't foud")

def rle_decoding(name):
    if path.exists(name):
        with open(name) as my_f:
            n = ""
            for k in my_f:
                word_nums = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        word_nums.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x * y, word_nums)))
    else:
        print("File {name} doesn't foud")
                
new_file()
rle_coding()
rle_decoding("code_text.txt")