# імпортування бібліотек
import pymorphy2
from pymorphy2 import analyzer
import csv

#імпортування словника української мови
morph = pymorphy2.MorphAnalyzer(lang='uk')

#відкриття файлу
file=open('D:\ВИШ\СУМ\Морфемологія СУМ\verbs.csv','r', encoding = 'utf-8')
# подача файлу у формі списку рядків
lines_list = file.read().split('\n')
#видалення останнього елемента списку рядків, бо чомусь програма бачить останній рядок порожнім (мабуть, у самому файлі xlsx стоять пробіли в клітинках після останнього дієслова)
lines_list.pop()
#обрізання першого елемента зі списку рядків, бо першим рядком є назви стовпчиків у таблиці дієслів
lines_list = lines_list[1:104]
#цикл для роботи зі складовими елементів списку рядків
for counter in range(len(lines_list)):
    lines_list[counter] = lines_list[counter].split(';')
for i in range(len(lines_list)):
    #print(lines_list[i][1]) #початкове слово
    butyavka1 = morph.parse(lines_list[i][1])[0]#відмінювання
    #print(butyavka1.tag.POS)
#утворення форми третьої особи множини теперішнього часу (для дієслів недоконаного виду)
    try:
        present = butyavka1.inflect({'plur', '3per', 'pres'})[0] #бажана словоформа
        print(present)
    except TypeError:
        print(" ")
#утворення дієприслівників теперішнього часу
    if present[-2:] == 'ся':
       present = present[:-4]
       print(present + 'чись')
    else:
       present = present[:-2]
       print(present + 'чи')
#утворення дієприслівників минулого часу
    past = lines_list[i][1]
    if past[-2:] == 'ся':
       past = past[:-4]
       print(past + 'вшись')
    else:
       past = past[:-2]
       print(past + 'вши')
