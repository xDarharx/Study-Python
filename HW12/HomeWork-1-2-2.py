#!/usr/bin/python3.8

# Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Ваша задача — вывести дату в текстовом виде,
# например: второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)

date = input('Введите дату в формате dd.mm.yyyy: ')
date_ls = date.split('.')

print(date_ls)

days = {1: "первое", 
        2: "второе", 
        3: "третье", 
        4: "четвертое", 
        5: "пятое", 
        6: "шестое", 
        7: "седьмое", 
        8: "восьмое", 
        9: "девятое", 
        10: "десятое", 
        11: "одиннадцатое", 
        12: "двенадцатое", 
        13: "тринадцатое", 
        14: "четырнадцатое", 
        15: "пятнадцатое", 
        16: "шестнадцатое", 
        17: "семнадцатое", 
        18: "восемнадцатое", 
        19: "девятнадцатое", 
        20: "двадцатое", 
        21: "двадцать первое",
        22: "двадцать второе",
        23: "двадцать третье",
        24: "двадцать четвертое",
        25: "двадцать пятое",
        26: "двадцать шестое",
        27: "двадцать седьмое",
        28: "двадцать восьмое",
        29: "двадцать девятое",
        30: "тридцатое", 
        31: "тридцать первое"}

monthes = { 1: "января",
            2: "февраля",
            3: "марта",
            4: "апреля",
            5: "мая",
            6: "июня",
            7: "июля",
            8: "августа",
            9: "сентября",
            10: "октября",
            11: "ноября",
            12: "декабря"}

day_txt = days[int(date_ls[0])]
month_txt = monthes[int(date_ls[1])]

print(day_txt, month_txt, date_ls[2], "года")

