##########################################################################################################################################
##########################################################################################################################################
# імпортування потрібних для роботи бібліотек
##########################################################################################################################################
##########################################################################################################################################
from ast import comprehension
import pymorphy2
from pymorphy2 import analyzer
import operator
import math
# from collections import Counter
# import matplotlib.pyplot as plt # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import sqlite3
# import re

##########################################################################################################################################
##########################################################################################################################################
# відкриття файлів (прописання шляхів)
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

file_1 = open(r'C:\\Users\\Ирина\\Desktop\\Quantitative linguistcs\\Sample prose Zhadan.txt')

############################################################### ВИБІРКА 2 ###############################################################

file_2 = open(r'C:\\Users\\Ирина\\Desktop\\Quantitative linguistcs\\Sample poetry Zhadan.txt')

# file = file.translate(str.maketrans('', '', string.punctuation))
# lines_list = file.read().split()

##########################################################################################################################################
##########################################################################################################################################
# створення змінної text_1, значенням якої є текст у файлі і
# до якої потрібно звертатися, щоб далі працювати з текстом файлу
# (прочитання тексту з файлу за допомогою методу read())
# тут і в наступних поясненнях програми описуватиму тільки
# роботу однієї з вибірок, бо ця програма працює однаково для обох вибірок
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

text_1 = file_1.read()

############################################################### ВИБІРКА 2 ###############################################################

text_2 = file_2.read()

##########################################################################################################################################
##########################################################################################################################################
# очищення тексту від розділових знаків
# для цього створюємо змінну punctuations,
# значенням якої є всі вручну прописані розділові знаки,
# окрім дефіса (по-перше, є слова з дефісами, а
# в дібраних текстах немає переносів слів з рядка на рядок),
# далі створюємо змінну text_without_punctuation1,
# значенням пустий простір, який можна заповнити
# типом даних str (тип даних рядок)
##########################################################################################################################################
##########################################################################################################################################
punctuations = '''.,<>?/~`!@'#№$"%^&*()_–+=:;/][}{'''

############################################################### ВИБІРКА 1 ###############################################################

text_without_punctuation_1 = ""

############################################################### ВИБІРКА 2 ###############################################################

text_without_punctuation_2 = ""

##########################################################################################################################################
##########################################################################################################################################
# у циклі говоримо програмі пройтися по всіх символах у тексті,
# і якщо символа немає в змінній punctuations,
# то в змінну text_without_punctuation_1, у якої поки пустий простір для str даних, додати символ
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################
for char in text_1:
    if char not in punctuations:
        text_without_punctuation_1 = text_without_punctuation_1 + char

############################################################### ВИБІРКА 2 ###############################################################
for char in text_2:
    if char not in punctuations:
        text_without_punctuation_2 = text_without_punctuation_2 + char
# print(text_without_punctuation[:100])

##########################################################################################################################################
##########################################################################################################################################
# створюємо змінну text_without_punctuation_and_lowered_1, значенням якої є текст з малими літерами
# (до змінної text_without_punctuation_1 застосовано метод lower(), який перетворює великі літери на малі)
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

text_without_punctuation_and_lowered_1 = text_without_punctuation_1.lower()

############################################################### ВИБІРКА 2 ###############################################################

text_without_punctuation_and_lowered_2 = text_without_punctuation_2.lower()

##########################################################################################################################################
##########################################################################################################################################
# створення змінної text_as_a_list_1, значенням якої є список (елементи - словоформи)
# (до змінної text_without_punctuation_and_lowered_1 застосовано метод split())
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

text_as_a_list_1 = text_without_punctuation_and_lowered_1.split()

############################################################### ВИБІРКА 2 ###############################################################

text_as_a_list_2 = text_without_punctuation_and_lowered_2.split()

##########################################################################################################################################
##########################################################################################################################################
# скорочення кількости словоформ у списку text_as_a_list_1
# (створення змінної text_ready_to_work_as_a_word_list_1, значенням якої є список (елементи - словоформи)
# (до змінної text_as_a_list_1 застосовано обрізання списку до 20 000 елементів))
# отже, змінна text_ready_to_work_as_a_word_list_1 є вибіркою, з якою будемо працювати
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

text_ready_to_work_as_a_word_list_1 = text_as_a_list_1[:20000]

############################################################### ВИБІРКА 2 ###############################################################

text_ready_to_work_as_a_word_list_2 = text_as_a_list_2[:20000]

##########################################################################################################################################
##########################################################################################################################################
# поділ списку text_ready_to_work_as_a_word_list_1 на 20 списків
# (у цих 20 списках елементами також є словоформи)
# (знову застосовано обрізання списку до 1 000 елементів)
# бачимо, що новостворені змінні subsample_1_1, subsample_2_1 тощо є підвибірками
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

subsample_1_1 = text_ready_to_work_as_a_word_list_1[:1000]
subsample_1_2 = text_ready_to_work_as_a_word_list_1[1001:2001]
subsample_1_3 = text_ready_to_work_as_a_word_list_1[2001:3001]
subsample_1_4 = text_ready_to_work_as_a_word_list_1[3001:4001]
subsample_1_5 = text_ready_to_work_as_a_word_list_1[4001:5001]
subsample_1_6 = text_ready_to_work_as_a_word_list_1[5001:6001]
subsample_1_7 = text_ready_to_work_as_a_word_list_1[6001:7001]
subsample_1_8 = text_ready_to_work_as_a_word_list_1[7001:8001]
subsample_1_9 = text_ready_to_work_as_a_word_list_1[8001:9001]
subsample_1_10 = text_ready_to_work_as_a_word_list_1[9001:10001]
subsample_1_11 = text_ready_to_work_as_a_word_list_1[10001:11001]
subsample_1_12 = text_ready_to_work_as_a_word_list_1[11001:12001]
subsample_1_13 = text_ready_to_work_as_a_word_list_1[12001:13001]
subsample_1_14 = text_ready_to_work_as_a_word_list_1[13001:14001]
subsample_1_15 = text_ready_to_work_as_a_word_list_1[14001:15001]
subsample_1_16 = text_ready_to_work_as_a_word_list_1[15001:16001]
subsample_1_17 = text_ready_to_work_as_a_word_list_1[16001:17001]
subsample_1_18 = text_ready_to_work_as_a_word_list_1[17001:18001]
subsample_1_19 = text_ready_to_work_as_a_word_list_1[18001:19001]
subsample_1_20 = text_ready_to_work_as_a_word_list_1[19001:]

############################################################### ВИБІРКА 2 ###############################################################

subsample_2_1 = text_ready_to_work_as_a_word_list_2[:1000]
subsample_2_2 = text_ready_to_work_as_a_word_list_2[1001:2001]
subsample_2_3 = text_ready_to_work_as_a_word_list_2[2001:3001]
subsample_2_4 = text_ready_to_work_as_a_word_list_2[3001:4001]
subsample_2_5 = text_ready_to_work_as_a_word_list_2[4001:5001]
subsample_2_6 = text_ready_to_work_as_a_word_list_2[5001:6001]
subsample_2_7 = text_ready_to_work_as_a_word_list_2[6001:7001]
subsample_2_8 = text_ready_to_work_as_a_word_list_2[7001:8001]
subsample_2_9 = text_ready_to_work_as_a_word_list_2[8001:9001]
subsample_2_10 = text_ready_to_work_as_a_word_list_2[9001:10001]
subsample_2_11 = text_ready_to_work_as_a_word_list_2[10001:11001]
subsample_2_12 = text_ready_to_work_as_a_word_list_2[11001:12001]
subsample_2_13 = text_ready_to_work_as_a_word_list_2[12001:13001]
subsample_2_14 = text_ready_to_work_as_a_word_list_2[13001:14001]
subsample_2_15 = text_ready_to_work_as_a_word_list_2[14001:15001]
subsample_2_16 = text_ready_to_work_as_a_word_list_2[15001:16001]
subsample_2_17 = text_ready_to_work_as_a_word_list_2[16001:17001]
subsample_2_18 = text_ready_to_work_as_a_word_list_2[17001:18001]
subsample_2_19 = text_ready_to_work_as_a_word_list_2[18001:19001]
subsample_2_20 = text_ready_to_work_as_a_word_list_2[19001:]

##########################################################################################################################################
##########################################################################################################################################
# вирахування частот словоформ
# для цього написано функцію, яка утворює частотний словник словоформ
# (ключ - словоформа, значення - частота появи в тексті))
# функція працює з кількома аргументами, про що свідчить напис "*args",
# це для того, щоб при виклику функції відразу працювати з усіма підвибірками
# і тим самим скоротити кількість рядків коду
# (хоча функція може працювати і з усією вибіркою)
# усередині функції створено порожній частотний словник словоформ frequency_word_usage_dict,
# цикл, який проходиться по загаданим при виклику функції аргументам (по підвибіркам), і
# цикл, який проходиться по елементам аргументів (по словоформах підвибірок), та
# методом get() рахує частоту знайдених словоформ
# і водночас додає ключі (словоформи) і  значення (абсолютна частота) у словник frequency_word_usage_dict,
# потім створюємо нову змінну sorted_in_descending_order_frequency_word_usage_dict,
# яка є поки що порожнім частотним словником словоформ, для того,
# щоб посортувати значення ключів (абсолютні частоти словоформ) і додати в sorted_in_descending_order_frequency_word_usage_dict
# у порядку спадання
# при виклику функція повертає sorted_in_descending_order_frequency_word_usage_dict
# (частотний словник словоформ з абсолютними частотами у порядку спадання)
##########################################################################################################################################
##########################################################################################################################################
def frequencyWordUsage(*args):
    '''
    The function makes a dict where
    key is a word form from a subsample and
    value is a quantity of this word form usage.
    '''
    frequency_word_usage_dict = {}

    for arg in args:
        for i in arg:
            frequency_word_usage_dict[i] = frequency_word_usage_dict.get(i, 0) + 1
    
    sorted_in_descending_order_frequency_word_usage_dict = dict(sorted(frequency_word_usage_dict.items(), key=operator.itemgetter(1), reverse=True))

    return sorted_in_descending_order_frequency_word_usage_dict

##########################################################################################################################################
# print("ЧС СЛОВОФОРМ 1.1: ", frequencyWordUsage(subsample_1_1), "ЧС СЛОВОФОРМ 1.2: ", frequencyWordUsage(subsample_1_2))
##########################################################################################################################################

##########################################################################################################################################
# print("ЧС СЛОВОФОРМ 2.1: ", frequencyWordUsage(subsample_2_1), "ЧС СЛОВОФОРМ 2.2: ", frequencyWordUsage(subsample_2_2))
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# створення змінної morph, яка зв'язуватиме досліджувані словоформи з бібліотекою pymorphy2
# у дужках пишемо мову, з якою працюємо (українська)
##########################################################################################################################################
##########################################################################################################################################
morph = pymorphy2.MorphAnalyzer(lang="uk")

##########################################################################################################################################
##########################################################################################################################################
# створення порожніх списків для того, щоб потім додати в них лексеми
# кожен список відповідає за окрему підвибірку
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

sample_1_lexemes = []

subsample_1_1_lexemes = []
subsample_1_2_lexemes = []
subsample_1_3_lexemes = []
subsample_1_4_lexemes = []
subsample_1_5_lexemes = []
subsample_1_6_lexemes = []
subsample_1_7_lexemes = []
subsample_1_8_lexemes = []
subsample_1_9_lexemes = []
subsample_1_10_lexemes = []
subsample_1_11_lexemes = []
subsample_1_12_lexemes = []
subsample_1_13_lexemes = []
subsample_1_14_lexemes = []
subsample_1_15_lexemes = []
subsample_1_16_lexemes = []
subsample_1_17_lexemes = []
subsample_1_18_lexemes = []
subsample_1_19_lexemes = []
subsample_1_20_lexemes = []

############################################################### ВИБІРКА 2 ###############################################################

sample_2_lexemes = []

subsample_2_1_lexemes = []
subsample_2_2_lexemes = []
subsample_2_3_lexemes = []
subsample_2_4_lexemes = []
subsample_2_5_lexemes = []
subsample_2_6_lexemes = []
subsample_2_7_lexemes = []
subsample_2_8_lexemes = []
subsample_2_9_lexemes = []
subsample_2_10_lexemes = []
subsample_2_11_lexemes = []
subsample_2_12_lexemes = []
subsample_2_13_lexemes = []
subsample_2_14_lexemes = []
subsample_2_15_lexemes = []
subsample_2_16_lexemes = []
subsample_2_17_lexemes = []
subsample_2_18_lexemes = []
subsample_2_19_lexemes = []
subsample_2_20_lexemes = []

##########################################################################################################################################
##########################################################################################################################################
# написано 40 циклів у циклі для кожної підвибірки з двох вибірок
# говоримо програмі пройтися по елементах у списку словоформ певної підвибірки
# і створити змінну language_variable, значенням якої є розпарсована словоформа з підвибірки
# (парсинг здійснено шляхом застосування методу parse() до змінної morph
# (у методі parse() у дужках написана назва елементу списку словоформ,
# щоб програма розуміла, що парсити потрібно кожну словоформу)),
# потім у цьому ж циклі написано цикл, який говорить програмі
# пройтися по елементах у змінній language_variable
# (нагадування: результатом парсингу в pymorphy2 є список (елементи - різна інформація про словоформу))
# і створити змінну lemma_variable, значенням якої є початкова форма словоформи (метод normal_form),
# далі в межах циклу (того, що ззовні, який проходиться по словоформах у списку словоформ)
# говоримо програмі додати змінні lemma_variable до порожнього списку лексем subsample_1_1_lexemes
# шляхом застосування методу append() (у методі append () у дужках написано назву змінної lemma_variable,
# щоб програма розуміла, що конкретно треба додавати у список лексем)
# описана процедура здійснюється 40 разів (бо підвибірок 40)
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

for item in text_ready_to_work_as_a_word_list_1:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    sample_1_lexemes.append(lemma_variable)

for item in subsample_1_1:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_1_lexemes.append(lemma_variable)
for item in subsample_1_2:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_2_lexemes.append(lemma_variable)
for item in subsample_1_3:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_3_lexemes.append(lemma_variable)
for item in subsample_1_4:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_4_lexemes.append(lemma_variable)
for item in subsample_1_5:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_5_lexemes.append(lemma_variable)
for item in subsample_1_6:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_6_lexemes.append(lemma_variable)
for item in subsample_1_7:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_7_lexemes.append(lemma_variable)
for item in subsample_1_8:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_8_lexemes.append(lemma_variable)
for item in subsample_1_9:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_9_lexemes.append(lemma_variable)
for item in subsample_1_10:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_10_lexemes.append(lemma_variable)
for item in subsample_1_11:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_11_lexemes.append(lemma_variable)
for item in subsample_1_12:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_12_lexemes.append(lemma_variable)
for item in subsample_1_13:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_13_lexemes.append(lemma_variable)
for item in subsample_1_14:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_14_lexemes.append(lemma_variable)
for item in subsample_1_15:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_15_lexemes.append(lemma_variable)
for item in subsample_1_16:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_16_lexemes.append(lemma_variable)
for item in subsample_1_17:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_17_lexemes.append(lemma_variable)
for item in subsample_1_18:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_18_lexemes.append(lemma_variable)
for item in subsample_1_19:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_19_lexemes.append(lemma_variable)
for item in subsample_1_20:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_1_20_lexemes.append(lemma_variable)

############################################################### ВИБІРКА 2 ###############################################################

for item in text_ready_to_work_as_a_word_list_2:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    sample_2_lexemes.append(lemma_variable)

for item in subsample_2_1:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_1_lexemes.append(lemma_variable)
for item in subsample_2_2:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_2_lexemes.append(lemma_variable)
for item in subsample_2_3:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_3_lexemes.append(lemma_variable)
for item in subsample_2_4:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_4_lexemes.append(lemma_variable)
for item in subsample_2_5:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_5_lexemes.append(lemma_variable)
for item in subsample_2_6:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_6_lexemes.append(lemma_variable)
for item in subsample_2_7:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_7_lexemes.append(lemma_variable)
for item in subsample_2_8:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_8_lexemes.append(lemma_variable)
for item in subsample_2_9:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_9_lexemes.append(lemma_variable)
for item in subsample_2_10:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_10_lexemes.append(lemma_variable)
for item in subsample_2_11:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_11_lexemes.append(lemma_variable)
for item in subsample_2_12:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_12_lexemes.append(lemma_variable)
for item in subsample_2_13:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_13_lexemes.append(lemma_variable)
for item in subsample_2_14:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_14_lexemes.append(lemma_variable)
for item in subsample_2_15:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_15_lexemes.append(lemma_variable)
for item in subsample_2_16:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_16_lexemes.append(lemma_variable)
for item in subsample_2_17:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_17_lexemes.append(lemma_variable)
for item in subsample_2_18:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_18_lexemes.append(lemma_variable)
for item in subsample_2_19:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_19_lexemes.append(lemma_variable)
for item in subsample_2_20:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    subsample_2_20_lexemes.append(lemma_variable)

##########################################################################################################################################
##########################################################################################################################################
# вирахування частот лексем
# функція працює так само, як уже описана функція створення частотного словника словоформ
# (називається ця вже описана функція frequencyWordUsage)
##########################################################################################################################################
##########################################################################################################################################
def frequencyLexemes(*args):
    '''
    The function makes a dict where
    key is a result of normal_form method (pymorphy2)
    taken from subsample and
    value is a quantity of this result usage.
    '''
    frequency_lexemes_dict = {}

    for arg in args:
        for i in arg:
            frequency_lexemes_dict[i] = frequency_lexemes_dict.get(i, 0) + 1

    sorted_in_descending_order_frequency_lexemes_dict = dict(sorted(frequency_lexemes_dict.items(), key=operator.itemgetter(1), reverse=True))

    return sorted_in_descending_order_frequency_lexemes_dict
# print("Частотний словник ЛЕКСЕМ: ", frequencyLexemes(text_ready_to_work_as_a_word_list)) # цей рядок не потрібен

##########################################################################################################################################
# print("ЧС ЛЕКСЕМ 1.1: ", frequencyLexemes(subsample_1_1_lexemes), "ЧС ЛЕКСЕМ 1.2: ", frequencyLexemes(subsample_1_2_lexemes))
##########################################################################################################################################

##########################################################################################################################################
# print("ЧС ЛЕКСЕМ 2.1: ", frequencyLexemes(subsample_2_1_lexemes), "ЧС ЛЕКСЕМ 2.2: ", frequencyLexemes(subsample_2_2_lexemes))
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# вирахування частот частин мови в межах підвибірок (але можна й у межах вибірки)
# для цього створено порожні словники окремо для кожної частини мови
# (ключ - назва частини мови, значення - абсолютна частота частини мови),
# далі знову пишемо цикл, який проходиться по кожному аргументу з аргументів,
# а тоді всередині цього циклу пишемо цикл, який проходиться по елементу аргументів,
# потім створюємо змінну language_variable, значенням якої є парсинг лише першого значення, яке визначив pymorphy2,
# тоді програма дивиться на назву частиномовного тегу в змінній language_variable
# і, залежно від назви тегу, додає до певного частотного словника за допомогою методу get()
# чому написано "language_variable[2]", так це тому, що результатом парсингу, як уже було сказано є список,
# де елементами є різна інформація про словоформу, а частиномовний тег є 3-ім елементом у цьому списку;
# індекс 2 написано, бо індекси, які приписуються елементам списку в Python, починають відлік не з 1, а з 0
# (тобто перший елемент має індекс 0, другий - 1 тощо)
# як видно з коду, функція повертає частотні словники, де також підписано, словники яких частин мови бачить користувач (-ка)
##########################################################################################################################################
##########################################################################################################################################
def frequencyPartsOfSpeech(*args):
    '''
    The function makes dicts for all the parts of speech where
    key is a word with some tag.POS (for example, "NOUN") and
    value is a quantity of this part of speech usage.
    '''
    frequency_nouns_dict = {}
    frequency_adjectives_dict = {}
    frequency_verbs_dict = {}
    frequency_gerunds_dict = {}
    frequency_numerals_dict = {}
    frequency_adverbs_dict = {}
    frequency_pronouns_dict = {}
    frequency_prepositions_dict = {}
    frequency_conjunctions_dict = {}
    frequency_particles_dict = {}
    frequency_interjections_dict = {}

    for arg in args:
        for i in arg:
            language_variable = morph.parse(i)[0]
            if language_variable.tag.POS == 'NOUN':
                frequency_nouns_dict[language_variable[2]] = frequency_nouns_dict.get(language_variable[2], 0) + 1
                sorted_in_descending_order_frequency_nouns_dict = dict(sorted(frequency_nouns_dict.items(), key=operator.itemgetter(1), reverse=True))
            elif language_variable.tag.POS == "ADJF":
                frequency_adjectives_dict[language_variable[2]] = frequency_adjectives_dict.get(language_variable[2], 0) + 1
                sorted_in_descending_order_frequency_adjectives_dict = dict(sorted(frequency_adjectives_dict.items(), key=operator.itemgetter(1), reverse=True))
            elif language_variable.tag.POS == "VERB":
                frequency_verbs_dict[language_variable[2]] = frequency_verbs_dict.get(language_variable[2], 0) + 1
                sorted_in_descending_order_frequency_verbs_dict = dict(sorted(frequency_verbs_dict.items(), key=operator.itemgetter(1), reverse=True))
            elif language_variable.tag.POS == "GRND":
                frequency_gerunds_dict[language_variable[2]] = frequency_gerunds_dict.get(language_variable[2], 0) + 1
                sorted_in_descending_order_frequency_gerunds_dict = dict(sorted(frequency_gerunds_dict.items(), key=operator.itemgetter(1), reverse=True))
            elif language_variable.tag.POS == "NUMR":
                frequency_numerals_dict[language_variable[2]] = frequency_numerals_dict.get(language_variable[2], 0) + 1
                sorted_in_descending_order_frequency_numerals_dict = dict(sorted(frequency_numerals_dict.items(), key=operator.itemgetter(1), reverse=True))
            elif language_variable.tag.POS == "ADVB":
                frequency_adverbs_dict[language_variable[2]] = frequency_adverbs_dict.get(language_variable[2], 0) + 1
                sorted_in_descending_order_frequency_adverbs_dict = dict(sorted(frequency_adverbs_dict.items(), key=operator.itemgetter(1), reverse=True))
            elif language_variable.tag.POS == "NPRO":
                frequency_pronouns_dict[language_variable[2]] = frequency_pronouns_dict.get(language_variable[2], 0) + 1
                sorted_in_descending_order_frequency_pronouns_dict = dict(sorted(frequency_pronouns_dict.items(), key=operator.itemgetter(1), reverse=True))
            elif language_variable.tag.POS == "PREP":
                frequency_prepositions_dict[language_variable[2]] = frequency_prepositions_dict.get(language_variable[2], 0) + 1
                sorted_in_descending_order_frequency_prepositions_dict = dict(sorted(frequency_prepositions_dict.items(), key=operator.itemgetter(1), reverse=True))
            elif language_variable.tag.POS == "CONJ":
                frequency_conjunctions_dict[language_variable[2]] = frequency_conjunctions_dict.get(language_variable[2], 0) + 1
                sorted_in_descending_order_frequency_conjunctions_dict = dict(sorted(frequency_conjunctions_dict.items(), key=operator.itemgetter(1), reverse=True))
            elif language_variable.tag.POS == "PRCL":
                frequency_particles_dict[language_variable[2]] = frequency_particles_dict.get(language_variable[2], 0) + 1
                sorted_in_descending_order_frequency_particles_dict = dict(sorted(frequency_particles_dict.items(), key=operator.itemgetter(1), reverse=True))
            elif language_variable.tag.POS == "INTJ":
                frequency_interjections_dict[language_variable[2]] = frequency_interjections_dict.get(language_variable[2], 0) + 1
                sorted_in_descending_order_frequency_interjections_dict = dict(sorted(frequency_interjections_dict.items(), key=operator.itemgetter(1), reverse=True))
                
    return  ['ІМЕННИКИ: ', sorted_in_descending_order_frequency_nouns_dict, \
            'ПРИКМЕТНИКИ: ', sorted_in_descending_order_frequency_adjectives_dict, \
            'ДІЄСЛОВА: ', sorted_in_descending_order_frequency_verbs_dict, \
            'ДІЄПРИСЛІВНИКИ: ', sorted_in_descending_order_frequency_gerunds_dict, \
            'ЧИСЛІВНИКИ КІЛЬКІСНІ: ', sorted_in_descending_order_frequency_numerals_dict, \
            'ПРИСЛІВНИКИ: ', sorted_in_descending_order_frequency_adverbs_dict, \
            'ЗАЙМЕННИКИ-ІМЕННИКИ: ', sorted_in_descending_order_frequency_pronouns_dict, \
            'ПРИЙМЕННИКИ: ', sorted_in_descending_order_frequency_prepositions_dict, \
            'СПОЛУЧНИКИ: ', sorted_in_descending_order_frequency_conjunctions_dict, \
            'ЧАСТКИ: ', sorted_in_descending_order_frequency_particles_dict, \
            'ВИГУКИ: ', sorted_in_descending_order_frequency_interjections_dict]

##########################################################################################################################################
# print("ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.1: ", frequencyPartsOfSpeech(subsample_1_1), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.2: ", frequencyPartsOfSpeech(subsample_1_2), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.3: ", frequencyPartsOfSpeech(subsample_1_3), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.4: ", frequencyPartsOfSpeech(subsample_1_4), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.5: ", frequencyPartsOfSpeech(subsample_1_5), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.6: ", frequencyPartsOfSpeech(subsample_1_6), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.7: ", frequencyPartsOfSpeech(subsample_1_7), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.8: ", frequencyPartsOfSpeech(subsample_1_8), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.9: ", frequencyPartsOfSpeech(subsample_1_9), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.10: ", frequencyPartsOfSpeech(subsample_1_10), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.11: ", frequencyPartsOfSpeech(subsample_1_11), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.12: ", frequencyPartsOfSpeech(subsample_1_12), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.13: ", frequencyPartsOfSpeech(subsample_1_13), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.14: ", frequencyPartsOfSpeech(subsample_1_14), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.15: ", frequencyPartsOfSpeech(subsample_1_15), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.16: ", frequencyPartsOfSpeech(subsample_1_16), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.17: ", frequencyPartsOfSpeech(subsample_1_17), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.18: ", frequencyPartsOfSpeech(subsample_1_18), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.19: ", frequencyPartsOfSpeech(subsample_1_19), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 1.20: ", frequencyPartsOfSpeech(subsample_1_20))
##########################################################################################################################################

##########################################################################################################################################
# print("ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.1: ", frequencyPartsOfSpeech(subsample_2_1), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.2: ", frequencyPartsOfSpeech(subsample_2_2), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.3: ", frequencyPartsOfSpeech(subsample_2_3), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.4: ", frequencyPartsOfSpeech(subsample_2_4), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.5: ", frequencyPartsOfSpeech(subsample_2_5), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.6: ", frequencyPartsOfSpeech(subsample_2_6), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.7: ", frequencyPartsOfSpeech(subsample_2_7), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.8: ", frequencyPartsOfSpeech(subsample_2_8), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.9: ", frequencyPartsOfSpeech(subsample_2_9), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.10: ", frequencyPartsOfSpeech(subsample_2_10), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.11: ", frequencyPartsOfSpeech(subsample_2_11), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.12: ", frequencyPartsOfSpeech(subsample_2_12), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.13: ", frequencyPartsOfSpeech(subsample_2_13), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.14: ", frequencyPartsOfSpeech(subsample_2_14), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.15: ", frequencyPartsOfSpeech(subsample_2_15), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.16: ", frequencyPartsOfSpeech(subsample_2_16), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.17: ", frequencyPartsOfSpeech(subsample_2_17), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.18: ", frequencyPartsOfSpeech(subsample_2_18), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.19: ", frequencyPartsOfSpeech(subsample_2_19), \
#     "ЧС ЧАСТИНИ МОВИ ПІДВИБІРКА 2.20: ", frequencyPartsOfSpeech(subsample_2_20))
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# вирахувано відносну різницю двох найчастотніших словоформ у вибірці
# функція робить усе те саме, що й функція frequencyWordUsage, але, окрім цього,
# ще створює змінні, значеннями яких є 2 найбільші абсолютні частоти
# (метод list() перетворює на список те, що написано в дужках після самої назви методу,
# у цій функції перетворює на список значення частотного словника);
# чому в тих же рядках написано [0] та [1], було пояснено, коли йшлося про ідексацію елементів списків у Python
# з нового: є рядок, який робить так, щоб при виклику функції значення відносної різниці і значок "%" було написано просто поряд, а не
# *цифра*, *"значок відсотка"*
# для цього до змінної relative_difference_of_two_most_frequent_words_1,
# значенням якої є відносна різниця двох найчастотніших словоформ,
# застосовано метод join() (приєднує елемент до даних типу str), у дужках якого є list comprehension
# (це коли у квадратних дужках пишеться код, який без квадратних дужок був би на кілька рядків,
# може застосовуватися до циклів, лямбда-функцій і т.д.);
# у цій функції list comprehension типу [*дія* for *елемент* in *певні рамки, на які поширюється дія*]),
# метод str() в *дії* перетворює те, що в дужках, на тип str, (а в дужках десятковий дріб (тип float),
# який тепер сприймається програмою як рядковий символ на рівні зі звичайним текстом, наприклад);
# str() застосовано до десяткового дробу типу float для того,
# щоб можна було з'єднувати методом join() цей дріб і значок відсотка типу str,
# а оскільки перед join() ще прописаний пробіл (' '), то десятковий дріб і значок відсотка не будуть написані разом
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

def relativeDifferenceOfTwoMostFrequentWords1(text_ready_to_work_as_a_word_list_1):
    '''
    The function makes a dict where
    key is a word from a sample and
    value is a quantity of this word form usage
    (in descending order by value)
    then calculates and returns a relative difference value
    of two most frequent words from a sample.
    '''
    frequency_word_usage_from_sample_dict = {}

    for word in text_ready_to_work_as_a_word_list_1:
        frequency_word_usage_from_sample_dict[word] = frequency_word_usage_from_sample_dict.get(word, 0) + 1
    sorted_in_descending_order_frequency_word_usage_from_sample_dict = dict(sorted(frequency_word_usage_from_sample_dict.items(), key=operator.itemgetter(1), reverse=True))

    first_value = list(sorted_in_descending_order_frequency_word_usage_from_sample_dict.values())[0]
    second_value = list(sorted_in_descending_order_frequency_word_usage_from_sample_dict.values())[1]

    relative_difference_of_two_most_frequent_words_1 = ((first_value - second_value)/first_value*100, "%")
    relative_difference_of_two_most_frequent_words_1 = ' '.join([str(element) for element in relative_difference_of_two_most_frequent_words_1])

    return (relative_difference_of_two_most_frequent_words_1)

##########################################################################################################################################
# print("ВІДНОСНА РІЗНИЦЯ ДЛЯ 2 НАЙБІЛЬШ ЧАСТОТНИХ СЛІВ 1: ", relativeDifferenceOfTwoMostFrequentWords1(text_ready_to_work_as_a_word_list_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

def relativeDifferenceOfTwoMostFrequentWords2(text_ready_to_work_as_a_word_list_2):
    '''
    The function makes a dict where
    key is a word from a sample and
    value is a quantity of this word form usage
    (in descending order by value)
    then calculates and returns a relative difference value
    of two most frequent words from a sample.
    '''
    frequency_word_usage_from_sample_dict = {}

    for word in text_ready_to_work_as_a_word_list_2:
        frequency_word_usage_from_sample_dict[word] = frequency_word_usage_from_sample_dict.get(word, 0) + 1
    sorted_in_descending_order_frequency_word_usage_from_sample_dict = dict(sorted(frequency_word_usage_from_sample_dict.items(), key=operator.itemgetter(1), reverse=True))

    first_value = list(sorted_in_descending_order_frequency_word_usage_from_sample_dict.values())[0]
    second_value = list(sorted_in_descending_order_frequency_word_usage_from_sample_dict.values())[1]

    relative_difference_of_two_most_frequent_words_2 = ((first_value - second_value)/first_value*100, "%")
    relative_difference_of_two_most_frequent_words_2 = ' '.join([str(element) for element in relative_difference_of_two_most_frequent_words_2])

    return (relative_difference_of_two_most_frequent_words_2)

##########################################################################################################################################
# print("ВІДНОСНА РІЗНИЦЯ ДЛЯ 2 НАЙБІЛЬШ ЧАСТОТНИХ СЛІВ 2: ", relativeDifferenceOfTwoMostFrequentWords2(text_ready_to_work_as_a_word_list_2))
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# вирахувано відносну різницю двох найменш частотних словоформ у вибірці
# 2 наступні функції працюють так само,
# як функції relativeDifferenceOfTwoMostFrequentWords1, relativeDifferenceOfTwoMostFrequentWords2
# єдина відмінність - значення частотного словника посортовано в порядку зростання
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

def relativeDifferenceOfTwoLeastFrequentWords1(text_ready_to_work_as_a_word_list_1):
    '''
    The function makes a dict where
    key is a word from a sample and
    value is a quantity of this word form usage
    (in ascending order by value)
    then calculates and returns a relative difference value
    of two least frequent words from a sample.
    '''
    frequency_word_usage_from_sample_dict = {}

    for word in text_ready_to_work_as_a_word_list_1:
        frequency_word_usage_from_sample_dict[word] = frequency_word_usage_from_sample_dict.get(word, 0) + 1
    sorted_in_ascending_order_frequency_word_usage_from_sample_dict = dict(sorted(frequency_word_usage_from_sample_dict.items(), key=operator.itemgetter(1)))

    first_value = list(sorted_in_ascending_order_frequency_word_usage_from_sample_dict.values())[0]
    second_value = list(sorted_in_ascending_order_frequency_word_usage_from_sample_dict.values())[1]

    relative_difference_of_two_least_frequent_words_1 = ((first_value - second_value)/first_value*100, "%")
    relative_difference_of_two_least_frequent_words_1 = ' '.join([str(element) for element in relative_difference_of_two_least_frequent_words_1])

    return (relative_difference_of_two_least_frequent_words_1)

##########################################################################################################################################
# print("ВІДНОСНА РІЗНИЦЯ ДЛЯ 2 НАЙМЕНШ ЧАСТОТНИХ СЛІВ 1: ", relativeDifferenceOfTwoLeastFrequentWords1(text_ready_to_work_as_a_word_list_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

def relativeDifferenceOfTwoLeastFrequentWords2(text_ready_to_work_as_a_word_list_2):
    '''
    The function makes a dict where
    key is a word from a sample and
    value is a quantity of this word form usage
    (in ascending order by value)
    then calculates and returns a relative difference value
    of two least frequent words from a sample.
    '''
    frequency_word_usage_from_sample_dict = {}

    for word in text_ready_to_work_as_a_word_list_2:
        frequency_word_usage_from_sample_dict[word] = frequency_word_usage_from_sample_dict.get(word, 0) + 1
    sorted_in_ascending_order_frequency_word_usage_from_sample_dict = dict(sorted(frequency_word_usage_from_sample_dict.items(), key=operator.itemgetter(1)))

    first_value = list(sorted_in_ascending_order_frequency_word_usage_from_sample_dict.values())[0]
    second_value = list(sorted_in_ascending_order_frequency_word_usage_from_sample_dict.values())[1]

    relative_difference_of_two_least_frequent_words_2 = ((first_value - second_value)/first_value*100, "%")
    relative_difference_of_two_least_frequent_words_2 = ' '.join([str(element) for element in relative_difference_of_two_least_frequent_words_2])

    return (relative_difference_of_two_least_frequent_words_2)

##########################################################################################################################################
# print("ВІДНОСНА РІЗНИЦЯ ДЛЯ 2 НАЙМЕНШ ЧАСТОТНИХ СЛІВ 2: ", relativeDifferenceOfTwoLeastFrequentWords2(text_ready_to_work_as_a_word_list_2))
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# вираховано відносну похибку двох найбільш частотних і найменш частотних словоформ у вибірках
# 2 наступні функції працюють так само,
# як функції relativeDifferenceOfTwoMostFrequentWords1, relativeDifferenceOfTwoMostFrequentWords2
# та relativeDifferenceOfTwoLeastFrequentWords1, relativeDifferenceOfTwoLeastFrequentWords2
# але додатково ще прописано формули для відносної похибки
# (наприклад, застосовано метод sqrt() з бібліотеки math, який вираховує квадратний корінь того,
# що написано в дужках після самої назви методу)
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

def relativeErrorOfTwoMostFrequentAndTwoLeastFrequentWords1(text_ready_to_work_as_a_word_list_1):
    '''
    The function makes a dict where
    key is a word from a sample and
    value is a quantity of this word form usage
    (in descending order by value)
    then calculates and returns a relative error value
    of two most frequent and two least frequent words from a sample.
    '''
    frequency_word_usage_from_sample_dict = {}

    for word in text_ready_to_work_as_a_word_list_1:
        frequency_word_usage_from_sample_dict[word] = frequency_word_usage_from_sample_dict.get(word, 0) + 1
    sorted_in_descending_order_frequency_word_usage_from_sample_dict = dict(sorted(frequency_word_usage_from_sample_dict.items(), key=operator.itemgetter(1), reverse=True))
    sorted_in_ascending_order_frequency_word_usage_from_sample_dict = dict(sorted(frequency_word_usage_from_sample_dict.items(), key=operator.itemgetter(1)))

    absolute_frequency_value_of_the_most_frequent_word_1_1 = list(sorted_in_descending_order_frequency_word_usage_from_sample_dict.values())[0]
    absolute_frequency_value_of_the_most_frequent_word_1_2 = list(sorted_in_descending_order_frequency_word_usage_from_sample_dict.values())[1]
    absolute_frequency_value_of_the_least_frequent_word_1_1 = list(sorted_in_ascending_order_frequency_word_usage_from_sample_dict.values())[0]
    absolute_frequency_value_of_the_least_frequent_word_1_2 = list(sorted_in_ascending_order_frequency_word_usage_from_sample_dict.values())[1]

    relative_error_of_the_most_frequent_word_1_1 = (1.96/math.sqrt(absolute_frequency_value_of_the_most_frequent_word_1_1*100), "%")
    relative_error_of_the_most_frequent_word_1_2 = (1.96/math.sqrt(absolute_frequency_value_of_the_most_frequent_word_1_2*100), "%")
    relative_error_of_the_least_frequent_word_1_1 = (1.96/math.sqrt(absolute_frequency_value_of_the_least_frequent_word_1_1*100), "%")
    relative_error_of_the_least_frequent_word_1_2 = (1.96/math.sqrt(absolute_frequency_value_of_the_least_frequent_word_1_2*100), "%")

    relative_error_of_the_most_frequent_word_1_1 = ' '.join([str(element) for element in relative_error_of_the_most_frequent_word_1_1])
    relative_error_of_the_most_frequent_word_1_2 = ' '.join([str(element) for element in relative_error_of_the_most_frequent_word_1_2])
    relative_error_of_the_least_frequent_word_1_1 = ' '.join([str(element) for element in relative_error_of_the_least_frequent_word_1_1])
    relative_error_of_the_least_frequent_word_1_2 = ' '.join([str(element) for element in relative_error_of_the_least_frequent_word_1_2])

    return ["ВІДНОСНА ПОХИБКА НАЙБІЛЬШ ЧАСТОТНОГО СЛОВА 1.1: ", relative_error_of_the_most_frequent_word_1_1, \
            "ВІДНОСНА ПОХИБКА НАЙБІЛЬШ ЧАСТОТНОГО СЛОВА 1.2: ", relative_error_of_the_most_frequent_word_1_2, \
            "ВІДНОСНА ПОХИБКА НАЙМЕНШ ЧАСТОТНОГО СЛОВА 1.1: ", relative_error_of_the_least_frequent_word_1_1, \
            "ВІДНОСНА ПОХИБКА НАЙМЕНШ ЧАСТОТНОГО СЛОВА 1.2: ", relative_error_of_the_least_frequent_word_1_2]

##########################################################################################################################################
# print(relativeErrorOfTwoMostFrequentAndTwoLeastFrequentWords1(text_ready_to_work_as_a_word_list_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

def relativeErrorOfTwoMostFrequentAndTwoLeastFrequentWords2(text_ready_to_work_as_a_word_list_2):
    '''
    The function makes a dict where
    key is a word from a sample and
    value is a quantity of this word form usage
    (in descending order by value)
    then calculates and returns a relative error value
    of two most frequent and two least frequent words from a sample.
    '''
    frequency_word_usage_from_sample_dict = {}

    for word in text_ready_to_work_as_a_word_list_2:
        frequency_word_usage_from_sample_dict[word] = frequency_word_usage_from_sample_dict.get(word, 0) + 1
    sorted_in_descending_order_frequency_word_usage_from_sample_dict = dict(sorted(frequency_word_usage_from_sample_dict.items(), key=operator.itemgetter(1), reverse=True))
    sorted_in_ascending_order_frequency_word_usage_from_sample_dict = dict(sorted(frequency_word_usage_from_sample_dict.items(), key=operator.itemgetter(1)))

    absolute_frequency_value_of_the_most_frequent_word_2_1 = list(sorted_in_descending_order_frequency_word_usage_from_sample_dict.values())[0]
    absolute_frequency_value_of_the_most_frequent_word_2_2 = list(sorted_in_descending_order_frequency_word_usage_from_sample_dict.values())[1]
    absolute_frequency_value_of_the_least_frequent_word_2_1 = list(sorted_in_ascending_order_frequency_word_usage_from_sample_dict.values())[0]
    absolute_frequency_value_of_the_least_frequent_word_2_2 = list(sorted_in_ascending_order_frequency_word_usage_from_sample_dict.values())[1]

    relative_error_of_the_most_frequent_word_2_1 = (1.96/math.sqrt(absolute_frequency_value_of_the_most_frequent_word_2_1*100), "%")
    relative_error_of_the_most_frequent_word_2_2 = (1.96/math.sqrt(absolute_frequency_value_of_the_most_frequent_word_2_2*100), "%")
    relative_error_of_the_least_frequent_word_2_1 = (1.96/math.sqrt(absolute_frequency_value_of_the_least_frequent_word_2_1*100), "%")
    relative_error_of_the_least_frequent_word_2_2 = (1.96/math.sqrt(absolute_frequency_value_of_the_least_frequent_word_2_2*100), "%")

    relative_error_of_the_most_frequent_word_2_1 = ' '.join([str(element) for element in relative_error_of_the_most_frequent_word_2_1])
    relative_error_of_the_most_frequent_word_2_2 = ' '.join([str(element) for element in relative_error_of_the_most_frequent_word_2_2])
    relative_error_of_the_least_frequent_word_2_1 = ' '.join([str(element) for element in relative_error_of_the_least_frequent_word_2_1])
    relative_error_of_the_least_frequent_word_2_2 = ' '.join([str(element) for element in relative_error_of_the_least_frequent_word_2_2])

    return ["ВІДНОСНА ПОХИБКА НАЙБІЛЬШ ЧАСТОТНОГО СЛОВА 2.1: ", relative_error_of_the_most_frequent_word_2_1, \
            "ВІДНОСНА ПОХИБКА НАЙБІЛЬШ ЧАСТОТНОГО СЛОВА 2.2: ", relative_error_of_the_most_frequent_word_2_2, \
            "ВІДНОСНА ПОХИБКА НАЙМЕНШ ЧАСТОТНОГО СЛОВА 2.1: ", relative_error_of_the_least_frequent_word_2_1, \
            "ВІДНОСНА ПОХИБКА НАЙМЕНШ ЧАСТОТНОГО СЛОВА 2.2: ", relative_error_of_the_least_frequent_word_2_2]

##########################################################################################################################################
# print(relativeErrorOfTwoMostFrequentAndTwoLeastFrequentWords2(text_ready_to_work_as_a_word_list_2))
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# створено 40 словників (ключі - назви частин мови, значення - абсолютна частота частин мови),
# де значення є 0, далі до кожного словника написано цикл, який проходиться по кожній лексемі із списку лексем,
# приписує змінній language_variable лише значення першої запропонованої pymorphy2 лексеми,
# потім є умова, яка дивиться на частиномовний тег, і залежно від тегу, додає 1
# до значення частини мови в словнику
# процедура повторюється 40 разів (бо підвибірок 40)
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

absolute_frequency_parts_of_speech_sample_1 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0, 
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in sample_1_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
            absolute_frequency_parts_of_speech_sample_1['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
            absolute_frequency_parts_of_speech_sample_1['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
            absolute_frequency_parts_of_speech_sample_1['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
            absolute_frequency_parts_of_speech_sample_1['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
            absolute_frequency_parts_of_speech_sample_1['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
            absolute_frequency_parts_of_speech_sample_1['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
            absolute_frequency_parts_of_speech_sample_1['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
            absolute_frequency_parts_of_speech_sample_1['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
            absolute_frequency_parts_of_speech_sample_1['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
            absolute_frequency_parts_of_speech_sample_1['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
            absolute_frequency_parts_of_speech_sample_1['INTJ'] += 1


absolute_frequency_parts_of_speech_subsample_1_1 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0, 
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_1_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
            absolute_frequency_parts_of_speech_subsample_1_1['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
            absolute_frequency_parts_of_speech_subsample_1_1['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
            absolute_frequency_parts_of_speech_subsample_1_1['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
            absolute_frequency_parts_of_speech_subsample_1_1['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
            absolute_frequency_parts_of_speech_subsample_1_1['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
            absolute_frequency_parts_of_speech_subsample_1_1['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
            absolute_frequency_parts_of_speech_subsample_1_1['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
            absolute_frequency_parts_of_speech_subsample_1_1['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
            absolute_frequency_parts_of_speech_subsample_1_1['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
            absolute_frequency_parts_of_speech_subsample_1_1['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
            absolute_frequency_parts_of_speech_subsample_1_1['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_2 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_2_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_2['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_2['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_2['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_2['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_2['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_2['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_2['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_2['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_2['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_2['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_2['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_3 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_3_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_3['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_3['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_3['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_3['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_3['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_3['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_3['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_3['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_3['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_3['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_3['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_4 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_4_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_4['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_4['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_4['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_4['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_4['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_4['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_4['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_4['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_4['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_4['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_4['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_5 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_5_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_5['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_5['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_5['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_5['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_5['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_5['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_5['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_5['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_5['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_5['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_5['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_6 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_6_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_6['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_6['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_6['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_6['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_6['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_6['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_6['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_6['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_6['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_6['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_6['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_7 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_7_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_7['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_7['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_7['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_7['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_7['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_7['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_7['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_7['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_7['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_7['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_7['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_8 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_8_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_8['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_8['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_8['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_8['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_8['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_8['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_8['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_8['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_8['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_8['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_8['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_9 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_9_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_9['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_9['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_9['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_9['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_9['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_9['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_9['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_9['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_9['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_9['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_9['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_10 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_10_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_10['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_10['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_10['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_10['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_10['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_10['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_10['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_10['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_10['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_10['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_10['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_11 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_11_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_11['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_11['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_11['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_11['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_11['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_11['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_11['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_11['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_11['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_11['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_11['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_12 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_12_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_12['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_12['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_12['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_12['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_12['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_12['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_12['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_12['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_12['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_12['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_12['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_13 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_13_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_13['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_13['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_13['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_13['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_13['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_13['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_13['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_13['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_13['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_13['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_13['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_14 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_14_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_14['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_14['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_14['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_14['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_14['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_14['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_14['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_14['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_14['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_14['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_14['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_15 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_15_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_15['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_15['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_15['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_15['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_15['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_15['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_15['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_15['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_15['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_15['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_15['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_16 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_16_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_16['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_16['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_16['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_16['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_16['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_16['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_16['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_16['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_16['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_16['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_16['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_17 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_17_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_17['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_17['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_17['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_17['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_17['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_17['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_17['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_17['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_17['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_17['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_17['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_18 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_18_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_18['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_18['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_18['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_18['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_18['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_18['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_18['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_18['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_18['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_18['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_18['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_19 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_19_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_19['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_19['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_19['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_19['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_19['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_19['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_19['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_19['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_19['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_19['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_19['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_1_20 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_1_20_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_1_20['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_1_20['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_1_20['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_1_20['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_1_20['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_1_20['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_1_20['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_1_20['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_1_20['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_1_20['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_1_20['INTJ'] += 1

##########################################################################################################################################
# print("АЧ ЧАСТИН МОВИ 1.1: ", absolute_frequency_parts_of_speech_subsample_1_1)
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

absolute_frequency_parts_of_speech_sample_2 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0, 
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in sample_2_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
            absolute_frequency_parts_of_speech_sample_2['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
            absolute_frequency_parts_of_speech_sample_2['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
            absolute_frequency_parts_of_speech_sample_2['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
            absolute_frequency_parts_of_speech_sample_2['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
            absolute_frequency_parts_of_speech_sample_2['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
            absolute_frequency_parts_of_speech_sample_2['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
            absolute_frequency_parts_of_speech_sample_2['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
            absolute_frequency_parts_of_speech_sample_2['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
            absolute_frequency_parts_of_speech_sample_2['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
            absolute_frequency_parts_of_speech_sample_2['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
            absolute_frequency_parts_of_speech_sample_2['INTJ'] += 1


absolute_frequency_parts_of_speech_subsample_2_1 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0, 
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_1_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
            absolute_frequency_parts_of_speech_subsample_2_1['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
            absolute_frequency_parts_of_speech_subsample_2_1['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
            absolute_frequency_parts_of_speech_subsample_2_1['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
            absolute_frequency_parts_of_speech_subsample_2_1['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
            absolute_frequency_parts_of_speech_subsample_2_1['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
            absolute_frequency_parts_of_speech_subsample_2_1['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
            absolute_frequency_parts_of_speech_subsample_2_1['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
            absolute_frequency_parts_of_speech_subsample_2_1['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
            absolute_frequency_parts_of_speech_subsample_2_1['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
            absolute_frequency_parts_of_speech_subsample_2_1['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
            absolute_frequency_parts_of_speech_subsample_2_1['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_2 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_2_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_2['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_2['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_2['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_2['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_2['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_2['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_2['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_2['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_2['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_2['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_2['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_3 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_3_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_3['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_3['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_3['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_3['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_3['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_3['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_3['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_3['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_3['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_3['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_3['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_4 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_4_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_4['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_4['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_4['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_4['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_4['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_4['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_4['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_4['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_4['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_4['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_4['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_5 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_5_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_5['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_5['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_5['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_5['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_5['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_5['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_5['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_5['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_5['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_5['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_5['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_6 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_6_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_6['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_6['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_6['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_6['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_6['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_6['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_6['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_6['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_6['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_6['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_6['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_7 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_7_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_7['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_7['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_7['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_7['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_7['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_7['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_7['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_7['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_7['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_7['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_7['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_8 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_8_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_8['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_8['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_8['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_8['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_8['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_8['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_8['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_8['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_8['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_8['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_8['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_9 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_9_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_9['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_9['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_9['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_9['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_9['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_9['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_9['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_9['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_9['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_9['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_9['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_10 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_10_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_10['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_10['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_10['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_10['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_10['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_10['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_10['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_10['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_10['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_10['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_10['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_11 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_11_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_11['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_11['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_11['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_11['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_11['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_11['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_11['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_11['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_11['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_11['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_11['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_12 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_12_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_12['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_12['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_12['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_12['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_12['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_12['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_12['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_12['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_12['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_12['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_12['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_13 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_13_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_13['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_13['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_13['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_13['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_13['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_13['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_13['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_13['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_13['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_13['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_13['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_14 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_14_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_14['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_14['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_14['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_14['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_14['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_14['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_14['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_14['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_14['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_14['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_14['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_15 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_15_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_15['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_15['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_15['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_15['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_15['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_15['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_15['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_15['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_15['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_15['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_15['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_16 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_16_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_16['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_16['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_16['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_16['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_16['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_16['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_16['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_16['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_16['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_16['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_16['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_17 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_17_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_17['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_17['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_17['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_17['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_17['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_17['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_17['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_17['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_17['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_17['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_17['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_18 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_18_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_18['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_18['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_18['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_18['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_18['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_18['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_18['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_18['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_18['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_18['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_18['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_19 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_19_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_19['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_19['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_19['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_19['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_19['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_19['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_19['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_19['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_19['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_19['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_19['INTJ'] += 1

absolute_frequency_parts_of_speech_subsample_2_20 = {'NOUN': 0, 'ADJF': 0, 'VERB': 0, 'GRND': 0,
                                                'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PREP': 0,
                                                'CONJ': 0, 'PRCL': 0, 'INTJ': 0}
for item in subsample_2_20_lexemes:
    language_variable = morph.parse(item)[0]
    if language_variable.tag.POS == 'NOUN':
        absolute_frequency_parts_of_speech_subsample_2_20['NOUN'] += 1
    elif language_variable.tag.POS == 'ADJF':
        absolute_frequency_parts_of_speech_subsample_2_20['ADJF'] += 1
    elif language_variable.tag.POS == 'VERB':
        absolute_frequency_parts_of_speech_subsample_2_20['VERB'] += 1
    elif language_variable.tag.POS == 'GRND':
        absolute_frequency_parts_of_speech_subsample_2_20['GRND'] += 1
    elif language_variable.tag.POS == 'NUMR':
        absolute_frequency_parts_of_speech_subsample_2_20['NUMR'] += 1
    elif language_variable.tag.POS == 'ADVB':
        absolute_frequency_parts_of_speech_subsample_2_20['ADVB'] += 1
    elif language_variable.tag.POS == 'NPRO':
        absolute_frequency_parts_of_speech_subsample_2_20['NPRO'] += 1
    elif language_variable.tag.POS == 'PREP':
        absolute_frequency_parts_of_speech_subsample_2_20['PREP'] += 1
    elif language_variable.tag.POS == 'CONJ':
        absolute_frequency_parts_of_speech_subsample_2_20['CONJ'] += 1
    elif language_variable.tag.POS == 'PRCL':
        absolute_frequency_parts_of_speech_subsample_2_20['PRCL'] += 1
    elif language_variable.tag.POS == 'INTJ':
        absolute_frequency_parts_of_speech_subsample_2_20['INTJ'] += 1

##########################################################################################################################################
# print("АЧ ЧАСТИН МОВИ 2.1: ", absolute_frequency_parts_of_speech_subsample_2_1)
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# вирахування середньої частоти частин мови
# для цього створено змінні (значення - сума всіх абсолютних частот певної частини мови),
# додати ці абсолютні частоти можна, якщо звернутися до її значення через назву ключа
# (наприклад, *назва словника*[*назва ключа*] дасть значення написаного у квадратних дужках ключа)
# потім змінні суми всіх абсолютних частот ділимо на кількість підвибірок у вибірці (на 20)
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

medium_frequency_parts_of_speech_list_of_dicts_1 = [absolute_frequency_parts_of_speech_subsample_1_1, absolute_frequency_parts_of_speech_subsample_1_2,
                                                absolute_frequency_parts_of_speech_subsample_1_3, absolute_frequency_parts_of_speech_subsample_1_4,
                                                absolute_frequency_parts_of_speech_subsample_1_5, absolute_frequency_parts_of_speech_subsample_1_6,
                                                absolute_frequency_parts_of_speech_subsample_1_7, absolute_frequency_parts_of_speech_subsample_1_8,
                                                absolute_frequency_parts_of_speech_subsample_1_9, absolute_frequency_parts_of_speech_subsample_1_10,
                                                absolute_frequency_parts_of_speech_subsample_1_11, absolute_frequency_parts_of_speech_subsample_1_12,
                                                absolute_frequency_parts_of_speech_subsample_1_13, absolute_frequency_parts_of_speech_subsample_1_14,
                                                absolute_frequency_parts_of_speech_subsample_1_15, absolute_frequency_parts_of_speech_subsample_1_16,
                                                absolute_frequency_parts_of_speech_subsample_1_17, absolute_frequency_parts_of_speech_subsample_1_18,
                                                absolute_frequency_parts_of_speech_subsample_1_19, absolute_frequency_parts_of_speech_subsample_1_20]
for item in medium_frequency_parts_of_speech_list_of_dicts_1:
    sum_of_noun_values = (absolute_frequency_parts_of_speech_subsample_1_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_2['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_4['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_6['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_8['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_10['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_12['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_14['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_16['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_18['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_20['NOUN'])
    sum_of_adjective_values = (absolute_frequency_parts_of_speech_subsample_1_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_2['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_4['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_6['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_8['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_10['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_12['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_14['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_16['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_18['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_20['NOUN'])
    sum_of_verb_values = (absolute_frequency_parts_of_speech_subsample_1_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_2['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_4['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_6['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_8['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_10['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_12['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_14['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_16['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_18['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_20['NOUN'])
    sum_of_gerund_values = (absolute_frequency_parts_of_speech_subsample_1_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_2['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_4['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_6['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_8['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_10['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_12['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_14['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_16['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_18['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_20['NOUN'])
    sum_of_numeral_values = (absolute_frequency_parts_of_speech_subsample_1_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_2['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_4['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_6['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_8['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_10['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_12['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_14['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_16['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_18['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_20['NOUN'])
    sum_of_adverb_values = (absolute_frequency_parts_of_speech_subsample_1_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_2['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_4['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_6['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_8['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_10['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_12['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_14['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_16['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_18['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_1_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_20['NOUN'])
    sum_of_nominative_pronoun_values = (absolute_frequency_parts_of_speech_subsample_1_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_2['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_1_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_4['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_1_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_6['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_1_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_8['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_1_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_10['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_1_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_12['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_1_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_14['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_1_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_16['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_1_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_18['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_1_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_20['NOUN'])
    sum_of_preposition_values = (absolute_frequency_parts_of_speech_subsample_1_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_2['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_4['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_6['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_8['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_10['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_12['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_14['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_16['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_18['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_20['NOUN'])
    sum_of_conjunction_values = (absolute_frequency_parts_of_speech_subsample_1_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_2['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_4['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_6['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_8['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_10['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_12['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_14['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_16['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_18['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_1_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_20['NOUN'])
    sum_of_particle_values = (absolute_frequency_parts_of_speech_subsample_1_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_2['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_4['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_6['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_8['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_10['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_12['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_14['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_16['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_18['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_20['NOUN'])
    sum_of_interjection_values = (absolute_frequency_parts_of_speech_subsample_1_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_2['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_4['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_6['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_8['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_10['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_12['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_14['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_16['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_18['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_1_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_1_20['NOUN'])
    medium_frequency_noun = sum_of_noun_values/20
    medium_frequency_adjective = sum_of_adjective_values/20
    medium_frequency_verb = sum_of_verb_values/20
    medium_frequency_gerund = sum_of_gerund_values/20
    medium_frequency_numeral = sum_of_numeral_values/20
    medium_frequency_adverb = sum_of_adverb_values/20
    medium_frequency_nominative_pronoun = sum_of_nominative_pronoun_values/20
    medium_frequency_preposition = sum_of_preposition_values/20
    medium_frequency_conjunction = sum_of_conjunction_values/20
    medium_frequency_particle = sum_of_particle_values/20
    medium_frequency_interjection = sum_of_interjection_values/20
# print("СЕРЕДНЯ ЧАСТОТА ІМЕННИКИ 1:", medium_frequency_noun, \
#     "СЕРЕДНЯ ЧАСТОТА ПРИКМЕТНИКИ 1:", medium_frequency_adjective, \
#     "СЕРЕДНЯ ЧАСТОТА ДІЄСЛОВА 1:", medium_frequency_verb, \
#     "СЕРЕДНЯ ЧАСТОТА ДІЄПРИСЛІВНИКИ 1:", medium_frequency_gerund, \
#     "СЕРЕДНЯ ЧАСТОТА ЧИСЛІВНИКИ 1:", medium_frequency_numeral, \
#     "СЕРЕДНЯ ЧАСТОТА ПРИСЛІВНИКИ 1:", medium_frequency_adverb, \
#     "СЕРЕДНЯ ЧАСТОТА ЗАЙМЕННИКИ-ІМЕННИКИ 1:", medium_frequency_nominative_pronoun, \
#     "СЕРЕДНЯ ЧАСТОТА ПРИЙМЕННИКИ 1:", medium_frequency_preposition, \
#     "СЕРЕДНЯ ЧАСТОТА СПОЛУЧНИКИ 1:", medium_frequency_conjunction, \
#     "СЕРЕДНЯ ЧАСТОТА ЧАСТКИ 1:", medium_frequency_particle, \
#     "СЕРЕДНЯ ЧАСТОТА ВИГУКИ 1:", medium_frequency_interjection)
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

medium_frequency_parts_of_speech_list_of_dicts_2 = [absolute_frequency_parts_of_speech_subsample_1_1, absolute_frequency_parts_of_speech_subsample_1_2,
                                                absolute_frequency_parts_of_speech_subsample_1_3, absolute_frequency_parts_of_speech_subsample_1_4,
                                                absolute_frequency_parts_of_speech_subsample_1_5, absolute_frequency_parts_of_speech_subsample_1_6,
                                                absolute_frequency_parts_of_speech_subsample_1_7, absolute_frequency_parts_of_speech_subsample_1_8,
                                                absolute_frequency_parts_of_speech_subsample_1_9, absolute_frequency_parts_of_speech_subsample_1_10,
                                                absolute_frequency_parts_of_speech_subsample_1_11, absolute_frequency_parts_of_speech_subsample_1_12,
                                                absolute_frequency_parts_of_speech_subsample_1_13, absolute_frequency_parts_of_speech_subsample_1_14,
                                                absolute_frequency_parts_of_speech_subsample_1_15, absolute_frequency_parts_of_speech_subsample_1_16,
                                                absolute_frequency_parts_of_speech_subsample_1_17, absolute_frequency_parts_of_speech_subsample_1_18,
                                                absolute_frequency_parts_of_speech_subsample_1_19, absolute_frequency_parts_of_speech_subsample_1_20]
for item in medium_frequency_parts_of_speech_list_of_dicts_2:
    sum_of_noun_values = (absolute_frequency_parts_of_speech_subsample_2_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_2['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_4['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_6['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_8['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_10['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_12['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_14['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_16['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_18['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_20['NOUN'])
    sum_of_adjective_values = (absolute_frequency_parts_of_speech_subsample_2_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_2['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_4['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_6['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_8['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_10['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_12['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_14['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_16['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_18['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_20['NOUN'])
    sum_of_verb_values = (absolute_frequency_parts_of_speech_subsample_2_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_2['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_4['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_6['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_8['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_10['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_12['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_14['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_16['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_18['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_20['NOUN'])
    sum_of_gerund_values = (absolute_frequency_parts_of_speech_subsample_2_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_2['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_4['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_6['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_8['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_10['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_12['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_14['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_16['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_18['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_20['NOUN'])
    sum_of_numeral_values = (absolute_frequency_parts_of_speech_subsample_2_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_2['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_4['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_6['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_8['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_10['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_12['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_14['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_16['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_18['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_20['NOUN'])
    sum_of_adverb_values = (absolute_frequency_parts_of_speech_subsample_2_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_2['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_4['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_6['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_8['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_10['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_12['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_14['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_16['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_18['NOUN'] +
                        absolute_frequency_parts_of_speech_subsample_2_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_20['NOUN'])
    sum_of_nominative_pronoun_values = (absolute_frequency_parts_of_speech_subsample_2_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_2['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_2_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_4['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_2_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_6['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_2_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_8['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_2_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_10['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_2_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_12['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_2_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_14['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_2_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_16['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_2_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_18['NOUN'] +
                                        absolute_frequency_parts_of_speech_subsample_2_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_20['NOUN'])
    sum_of_preposition_values = (absolute_frequency_parts_of_speech_subsample_2_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_2['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_4['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_6['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_8['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_10['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_12['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_14['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_16['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_18['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_20['NOUN'])
    sum_of_conjunction_values = (absolute_frequency_parts_of_speech_subsample_2_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_2['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_4['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_6['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_8['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_10['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_12['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_14['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_16['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_18['NOUN'] +
                                absolute_frequency_parts_of_speech_subsample_2_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_20['NOUN'])
    sum_of_particle_values = (absolute_frequency_parts_of_speech_subsample_2_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_2['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_4['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_6['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_8['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_10['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_12['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_14['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_16['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_18['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_20['NOUN'])
    sum_of_interjection_values = (absolute_frequency_parts_of_speech_subsample_2_1['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_2['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_3['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_4['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_5['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_6['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_7['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_8['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_9['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_10['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_11['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_12['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_13['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_14['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_15['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_16['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_17['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_18['NOUN'] +
                            absolute_frequency_parts_of_speech_subsample_2_19['NOUN'] + absolute_frequency_parts_of_speech_subsample_2_20['NOUN'])
    medium_frequency_noun = sum_of_noun_values/20
    medium_frequency_adjective = sum_of_adjective_values/20
    medium_frequency_verb = sum_of_verb_values/20
    medium_frequency_gerund = sum_of_gerund_values/20
    medium_frequency_numeral = sum_of_numeral_values/20
    medium_frequency_adverb = sum_of_adverb_values/20
    medium_frequency_nominative_pronoun = sum_of_nominative_pronoun_values/20
    medium_frequency_preposition = sum_of_preposition_values/20
    medium_frequency_conjunction = sum_of_conjunction_values/20
    medium_frequency_particle = sum_of_particle_values/20
    medium_frequency_interjection = sum_of_interjection_values/20
# print("СЕРЕДНЯ ЧАСТОТА ІМЕННИКИ 2:", medium_frequency_noun, \
#     "СЕРЕДНЯ ЧАСТОТА ПРИКМЕТНИКИ 2:", medium_frequency_adjective, \
#     "СЕРЕДНЯ ЧАСТОТА ДІЄСЛОВА 2:", medium_frequency_verb, \
#     "СЕРЕДНЯ ЧАСТОТА ДІЄПРИСЛІВНИКИ 2:", medium_frequency_gerund, \
#     "СЕРЕДНЯ ЧАСТОТА ЧИСЛІВНИКИ 2:", medium_frequency_numeral, \
#     "СЕРЕДНЯ ЧАСТОТА ПРИСЛІВНИКИ 2:", medium_frequency_adverb, \
#     "СЕРЕДНЯ ЧАСТОТА ЗАЙМЕННИКИ-ІМЕННИКИ 2:", medium_frequency_nominative_pronoun, \
#     "СЕРЕДНЯ ЧАСТОТА ПРИЙМЕННИКИ 2:", medium_frequency_preposition, \
#     "СЕРЕДНЯ ЧАСТОТА СПОЛУЧНИКИ 2:", medium_frequency_conjunction, \
#     "СЕРЕДНЯ ЧАСТОТА ЧАСТКИ 2:", medium_frequency_particle, \
#     "СЕРЕДНЯ ЧАСТОТА ВИГУКИ 2:", medium_frequency_interjection)
##########################################################################################################################################
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# створено порожні списки, куди буде додано варіянти абсолютних частот,
# здобутих із словників абсолютних частот частин мови,
# далі написано цикл, який проходиться по елементах словників абсолютних частот частин мови і
# за допомогою методу append() додає значення ключа до порожнього списку абсолютних частот
# як було сказано, дістати зі словника значення ключа можна, якщо звернутися до ключа, написавши його назву
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

variants_absolute_frequency_noun_1 = []
variants_absolute_frequency_adjective_1 = []
variants_absolute_frequency_verb_1 = []
variants_absolute_frequency_gerund_1 = []
variants_absolute_frequency_numeral_1 = []
variants_absolute_frequency_adverb_1 = []
variants_absolute_frequency_nominative_pronoun_1 = []
variants_absolute_frequency_preposition_1 = []
variants_absolute_frequency_conjunction_1 = []
variants_absolute_frequency_particle_1 = []
variants_absolute_frequency_interjection_1 = []
part_of_speech_dicts_1 = [absolute_frequency_parts_of_speech_subsample_1_1, absolute_frequency_parts_of_speech_subsample_1_2,
                        absolute_frequency_parts_of_speech_subsample_1_3, absolute_frequency_parts_of_speech_subsample_1_4,
                        absolute_frequency_parts_of_speech_subsample_1_5, absolute_frequency_parts_of_speech_subsample_1_6,
                        absolute_frequency_parts_of_speech_subsample_1_7, absolute_frequency_parts_of_speech_subsample_1_8,
                        absolute_frequency_parts_of_speech_subsample_1_9, absolute_frequency_parts_of_speech_subsample_1_10,
                        absolute_frequency_parts_of_speech_subsample_1_11, absolute_frequency_parts_of_speech_subsample_1_12,
                        absolute_frequency_parts_of_speech_subsample_1_13, absolute_frequency_parts_of_speech_subsample_1_14,
                        absolute_frequency_parts_of_speech_subsample_1_15, absolute_frequency_parts_of_speech_subsample_1_16,
                        absolute_frequency_parts_of_speech_subsample_1_17, absolute_frequency_parts_of_speech_subsample_1_18,
                        absolute_frequency_parts_of_speech_subsample_1_19, absolute_frequency_parts_of_speech_subsample_1_20]
for item in part_of_speech_dicts_1:
    variants_absolute_frequency_noun_1.append(item['NOUN'])
    variants_absolute_frequency_adjective_1.append(item['ADJF'])
    variants_absolute_frequency_verb_1.append(item['VERB'])
    variants_absolute_frequency_gerund_1.append(item['GRND'])
    variants_absolute_frequency_numeral_1.append(item['NUMR'])
    variants_absolute_frequency_adverb_1.append(item['ADVB'])
    variants_absolute_frequency_nominative_pronoun_1.append(item['NPRO'])
    variants_absolute_frequency_preposition_1.append(item['PREP'])
    variants_absolute_frequency_conjunction_1.append(item['CONJ'])
    variants_absolute_frequency_particle_1.append(item['PRCL'])
    variants_absolute_frequency_interjection_1.append(item['INTJ'])

############################################################### ВИБІРКА 2 ###############################################################

variants_absolute_frequency_noun_2 = []
variants_absolute_frequency_adjective_2 = []
variants_absolute_frequency_verb_2 = []
variants_absolute_frequency_gerund_2 = []
variants_absolute_frequency_numeral_2 = []
variants_absolute_frequency_adverb_2 = []
variants_absolute_frequency_nominative_pronoun_2 = []
variants_absolute_frequency_preposition_2 = []
variants_absolute_frequency_conjunction_2 = []
variants_absolute_frequency_particle_2 = []
variants_absolute_frequency_interjection_2 = []
part_of_speech_dicts_2 = [absolute_frequency_parts_of_speech_subsample_2_1, absolute_frequency_parts_of_speech_subsample_2_2,
                        absolute_frequency_parts_of_speech_subsample_2_3, absolute_frequency_parts_of_speech_subsample_2_4,
                        absolute_frequency_parts_of_speech_subsample_2_5, absolute_frequency_parts_of_speech_subsample_2_6,
                        absolute_frequency_parts_of_speech_subsample_2_7, absolute_frequency_parts_of_speech_subsample_2_8,
                        absolute_frequency_parts_of_speech_subsample_2_9, absolute_frequency_parts_of_speech_subsample_2_10,
                        absolute_frequency_parts_of_speech_subsample_2_11, absolute_frequency_parts_of_speech_subsample_2_12,
                        absolute_frequency_parts_of_speech_subsample_2_13, absolute_frequency_parts_of_speech_subsample_2_14,
                        absolute_frequency_parts_of_speech_subsample_2_15, absolute_frequency_parts_of_speech_subsample_2_16,
                        absolute_frequency_parts_of_speech_subsample_2_17, absolute_frequency_parts_of_speech_subsample_2_18,
                        absolute_frequency_parts_of_speech_subsample_2_19, absolute_frequency_parts_of_speech_subsample_2_20]
for item in part_of_speech_dicts_2:
    variants_absolute_frequency_noun_2.append(item['NOUN'])
    variants_absolute_frequency_adjective_2.append(item['ADJF'])
    variants_absolute_frequency_verb_2.append(item['VERB'])
    variants_absolute_frequency_gerund_2.append(item['GRND'])
    variants_absolute_frequency_numeral_2.append(item['NUMR'])
    variants_absolute_frequency_adverb_2.append(item['ADVB'])
    variants_absolute_frequency_nominative_pronoun_2.append(item['NPRO'])
    variants_absolute_frequency_preposition_2.append(item['PREP'])
    variants_absolute_frequency_conjunction_2.append(item['CONJ'])
    variants_absolute_frequency_particle_2.append(item['PRCL'])
    variants_absolute_frequency_interjection_2.append(item['INTJ'])

##########################################################################################################################################
##########################################################################################################################################
# до кожного списку варіянт абсолютних частот частин мови застосовано метод sort(),
# який сортує елементи списків у порядку зростання
# так буде зручніше потім працювати з цими варіянтами
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

variants_absolute_frequency_noun_1.sort()
variants_absolute_frequency_adjective_1.sort()
variants_absolute_frequency_verb_1.sort()
variants_absolute_frequency_gerund_1.sort()
variants_absolute_frequency_numeral_1.sort()
variants_absolute_frequency_adverb_1.sort()
variants_absolute_frequency_nominative_pronoun_1.sort()
variants_absolute_frequency_preposition_1.sort()
variants_absolute_frequency_conjunction_1.sort()
variants_absolute_frequency_particle_1.sort()
variants_absolute_frequency_interjection_1.sort()

############################################################### ВИБІРКА 2 ###############################################################

variants_absolute_frequency_noun_2.sort()
variants_absolute_frequency_adjective_2.sort()
variants_absolute_frequency_verb_2.sort()
variants_absolute_frequency_gerund_2.sort()
variants_absolute_frequency_numeral_2.sort()
variants_absolute_frequency_adverb_2.sort()
variants_absolute_frequency_nominative_pronoun_2.sort()
variants_absolute_frequency_preposition_2.sort()
variants_absolute_frequency_conjunction_2.sort()
variants_absolute_frequency_particle_2.sort()
variants_absolute_frequency_interjection_2.sort()

##########################################################################################################################################
##########################################################################################################################################
# створено словники методом dict() (ключ - варіянта, значення - кількість варіянт у вибірці)
# усередині dict() є метод zip(), який робить елементи списку варіянт ключами новоствореного словника,
# а також присвоює значення ключам
# виглядає це так: zip(*список, елементи якого будуть ключами*, *список, елементи якого будуть значеннями)
# але оскільки значенням буде кількість варіянт у вибірці, то потрібно порахувати кількість варіянт
# знову застосовуємо list comprehension типу [*дія* for *елемент* in *межі, у яких здійснюється дія*]
# у *дії* є метод count(), який рахує варіянти
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

grouped_data_noun_1 = dict(zip(variants_absolute_frequency_noun_1, [variants_absolute_frequency_noun_1.count(i) for i in variants_absolute_frequency_noun_1]))
grouped_data_adjective_1 = dict(zip(variants_absolute_frequency_adjective_1, [variants_absolute_frequency_adjective_1.count(i) for i in variants_absolute_frequency_adjective_1]))
grouped_data_verb_1 = dict(zip(variants_absolute_frequency_verb_1, [variants_absolute_frequency_verb_1.count(i) for i in variants_absolute_frequency_verb_1]))
grouped_data_gerund_1 = dict(zip(variants_absolute_frequency_gerund_1, [variants_absolute_frequency_gerund_1.count(i) for i in variants_absolute_frequency_gerund_1]))
grouped_data_numeral_1 = dict(zip(variants_absolute_frequency_numeral_1, [variants_absolute_frequency_numeral_1.count(i) for i in variants_absolute_frequency_numeral_1]))
grouped_data_adverb_1 = dict(zip(variants_absolute_frequency_adverb_1, [variants_absolute_frequency_adverb_1.count(i) for i in variants_absolute_frequency_adverb_1]))
grouped_data_nominative_pronoun_1 = dict(zip(variants_absolute_frequency_nominative_pronoun_1, [variants_absolute_frequency_nominative_pronoun_1.count(i) for i in variants_absolute_frequency_nominative_pronoun_1]))
grouped_data_preposition_1 = dict(zip(variants_absolute_frequency_preposition_1, [variants_absolute_frequency_preposition_1.count(i) for i in variants_absolute_frequency_preposition_1]))
grouped_data_conjunction_1 = dict(zip(variants_absolute_frequency_conjunction_1, [variants_absolute_frequency_conjunction_1.count(i) for i in variants_absolute_frequency_conjunction_1]))
grouped_data_particle_1 = dict(zip(variants_absolute_frequency_particle_1, [variants_absolute_frequency_particle_1.count(i) for i in variants_absolute_frequency_particle_1]))
grouped_data_interjection_1 = dict(zip(variants_absolute_frequency_interjection_1, [variants_absolute_frequency_interjection_1.count(i) for i in variants_absolute_frequency_interjection_1]))

# print("ВАРІЯЦІЙНИЙ РЯД ІМЕННИКИ 1: ", grouped_data_noun_1, \
#     "ВАРІЯЦІЙНИЙ РЯД ПРИКМЕТНИКИ 1: ", grouped_data_adjective_1, \
#     "ВАРІЯЦІЙНИЙ РЯД ДІЄСЛОВА 1: ", grouped_data_verb_1, \
#     "ВАРІЯЦІЙНИЙ РЯД ДІЄПРИСЛІВНИКИ 1: ", grouped_data_gerund_1, \
#     "ВАРІЯЦІЙНИЙ РЯД ЧИСЛІВНИКИ 1: ", grouped_data_numeral_1, \
#     "ВАРІЯЦІЙНИЙ РЯД ПРИСЛІВНИКИ 1: ", grouped_data_adverb_1, \
#     "ВАРІЯЦІЙНИЙ РЯД ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", grouped_data_nominative_pronoun_1, \
#     "ВАРІЯЦІЙНИЙ РЯД ПРИЙМЕННИКИ 1: ", grouped_data_preposition_1, \
#     "ВАРІЯЦІЙНИЙ РЯД СПОЛУЧНИКИ 1: ", grouped_data_conjunction_1, \
#     "ВАРІЯЦІЙНИЙ РЯД ЧАСТКИ 1: ", grouped_data_particle_1, \
#     "ВАРІЯЦІЙНИЙ РЯД ВИГУКИ 1: ", grouped_data_interjection_1)

############################################################### ВИБІРКА 2 ###############################################################

grouped_data_noun_2 = dict(zip(variants_absolute_frequency_noun_2, [variants_absolute_frequency_noun_2.count(i) for i in variants_absolute_frequency_noun_2]))
grouped_data_adjective_2 = dict(zip(variants_absolute_frequency_adjective_2, [variants_absolute_frequency_adjective_2.count(i) for i in variants_absolute_frequency_adjective_2]))
grouped_data_verb_2 = dict(zip(variants_absolute_frequency_verb_2, [variants_absolute_frequency_verb_2.count(i) for i in variants_absolute_frequency_verb_2]))
grouped_data_gerund_2 = dict(zip(variants_absolute_frequency_gerund_2, [variants_absolute_frequency_gerund_2.count(i) for i in variants_absolute_frequency_gerund_2]))
grouped_data_numeral_2 = dict(zip(variants_absolute_frequency_numeral_2, [variants_absolute_frequency_numeral_2.count(i) for i in variants_absolute_frequency_numeral_2]))
grouped_data_adverb_2 = dict(zip(variants_absolute_frequency_adverb_2, [variants_absolute_frequency_adverb_2.count(i) for i in variants_absolute_frequency_adverb_2]))
grouped_data_nominative_pronoun_2 = dict(zip(variants_absolute_frequency_nominative_pronoun_2, [variants_absolute_frequency_nominative_pronoun_2.count(i) for i in variants_absolute_frequency_nominative_pronoun_2]))
grouped_data_preposition_2 = dict(zip(variants_absolute_frequency_preposition_2, [variants_absolute_frequency_preposition_2.count(i) for i in variants_absolute_frequency_preposition_2]))
grouped_data_conjunction_2 = dict(zip(variants_absolute_frequency_conjunction_2, [variants_absolute_frequency_conjunction_2.count(i) for i in variants_absolute_frequency_conjunction_2]))
grouped_data_particle_2 = dict(zip(variants_absolute_frequency_particle_2, [variants_absolute_frequency_particle_2.count(i) for i in variants_absolute_frequency_particle_2]))
grouped_data_interjection_2 = dict(zip(variants_absolute_frequency_interjection_2, [variants_absolute_frequency_interjection_2.count(i) for i in variants_absolute_frequency_interjection_2]))

# print("ВАРІЯЦІЙНИЙ РЯД ІМЕННИКИ 2: ", grouped_data_noun_2, \
#     "ВАРІЯЦІЙНИЙ РЯД ПРИКМЕТНИКИ 2: ", grouped_data_adjective_2, \
#     "ВАРІЯЦІЙНИЙ РЯД ДІЄСЛОВА 2: ", grouped_data_verb_2, \
#     "ВАРІЯЦІЙНИЙ РЯД ДІЄПРИСЛІВНИКИ 2: ", grouped_data_gerund_2, \
#     "ВАРІЯЦІЙНИЙ РЯД ЧИСЛІВНИКИ 2: ", grouped_data_numeral_2, \
#     "ВАРІЯЦІЙНИЙ РЯД ПРИСЛІВНИКИ 2: ", grouped_data_adverb_2, \
#     "ВАРІЯЦІЙНИЙ РЯД ЗАЙМЕННИКИ-ІМЕННИКИ 2: ", grouped_data_nominative_pronoun_2, \
#     "ВАРІЯЦІЙНИЙ РЯД ПРИЙМЕННИКИ 2: ", grouped_data_preposition_2, \
#     "ВАРІЯЦІЙНИЙ РЯД СПОЛУЧНИКИ 2: ", grouped_data_conjunction_2, \
#     "ВАРІЯЦІЙНИЙ РЯД ЧАСТКИ 2: ", grouped_data_particle_2, \
#     "ВАРІЯЦІЙНИЙ РЯД ВИГУКИ 2: ", grouped_data_interjection_2)

##########################################################################################################################################
##########################################################################################################################################
# створення порожніх списків, де елементами будуть варіянти частин мови
# для цього для кожної частини мови написано цикл, який проходиться по ключах у словниках з варіяційним рядом
# (метод keys()) і додає ключі (варіянти) до новостворених списків
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

xi_noun_1 = []
xi_adjective_1 = []
xi_verb_1 = []
xi_gerund_1 = []
xi_numeral_1 = []
xi_adverb_1 = []
xi_nominative_pronoun_1 = []
xi_preposition_1 = []
xi_conjunction_1 = []
xi_particle_1 = []
xi_interjection_1 = []

for key in grouped_data_noun_1.keys():
    xi_noun_1.append(key)
for key in grouped_data_adjective_1.keys():
    xi_adjective_1.append(key)
for key in grouped_data_verb_1.keys():
    xi_verb_1.append(key)
for key in grouped_data_gerund_1.keys():
    xi_gerund_1.append(key)
for key in grouped_data_numeral_1.keys():
    xi_numeral_1.append(key)
for key in grouped_data_adverb_1.keys():
    xi_adverb_1.append(key)
for key in grouped_data_nominative_pronoun_1.keys():
    xi_nominative_pronoun_1.append(key)
for key in grouped_data_preposition_1.keys():
    xi_preposition_1.append(key)
for key in grouped_data_conjunction_1.keys():
    xi_conjunction_1.append(key)
for key in grouped_data_particle_1.keys():
    xi_particle_1.append(key)
for key in grouped_data_interjection_1.keys():
    xi_interjection_1.append(key)

##########################################################################################################################################
# print(sum(xi_noun_1))
# print(sum(xi_adjective_1))
# print(sum(xi_verb_1))
# print(sum(xi_gerund_1))
# print(sum(xi_numeral_1))
# print(sum(xi_adverb_1))
# print(sum(xi_nominative_pronoun_1))
# print(sum(xi_preposition_1))
# print(sum(xi_conjunction_1))
# print(sum(xi_particle_1))
# print(sum(xi_interjection_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

xi_noun_2 = []
xi_adjective_2 = []
xi_verb_2 = []
xi_gerund_2 = []
xi_numeral_2 = []
xi_adverb_2 = []
xi_nominative_pronoun_2 = []
xi_preposition_2 = []
xi_conjunction_2 = []
xi_particle_2 = []
xi_interjection_2 = []

for key in grouped_data_noun_2.keys():
    xi_noun_2.append(key)
for key in grouped_data_adjective_2.keys():
    xi_adjective_2.append(key)
for key in grouped_data_verb_2.keys():
    xi_verb_2.append(key)
for key in grouped_data_gerund_2.keys():
    xi_gerund_2.append(key)
for key in grouped_data_numeral_2.keys():
    xi_numeral_2.append(key)
for key in grouped_data_adverb_2.keys():
    xi_adverb_2.append(key)
for key in grouped_data_nominative_pronoun_2.keys():
    xi_nominative_pronoun_2.append(key)
for key in grouped_data_preposition_2.keys():
    xi_preposition_2.append(key)
for key in grouped_data_conjunction_2.keys():
    xi_conjunction_2.append(key)
for key in grouped_data_particle_2.keys():
    xi_particle_2.append(key)
for key in grouped_data_interjection_2.keys():
    xi_interjection_2.append(key)

##########################################################################################################################################
# print(sum(xi_noun_2))
# print(sum(xi_adjective_2))
# print(sum(xi_verb_2))
# print(sum(xi_gerund_2))
# print(sum(xi_numeral_2))
# print(sum(xi_adverb_2))
# print(sum(xi_nominative_pronoun_2))
# print(sum(xi_preposition_2))
# print(sum(xi_conjunction_2))
# print(sum(xi_particle_2))
# print(sum(xi_interjection_2))
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# створення порожніх списків, де елементами будуть кількості кожної варіянти певної частини мови
# тут відбувається те саме, що при створенні списків варіянт,
# але цикл звертається не до ключів (варіянт), а до значень (кількість варіянти)
# (метод values())
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

ni_noun_1 = []
ni_adjective_1 = []
ni_verb_1 = []
ni_gerund_1 = []
ni_numeral_1 = []
ni_adverb_1 = []
ni_nominative_pronoun_1 = []
ni_preposition_1 = []
ni_conjunction_1 = []
ni_particle_1 = []
ni_interjection_1 = []

for value in grouped_data_noun_1.values():
    ni_noun_1.append(value)
for value in grouped_data_adjective_1.values():
    ni_adjective_1.append(value)
for value in grouped_data_verb_1.values():
    ni_verb_1.append(value)
for value in grouped_data_gerund_1.values():
    ni_gerund_1.append(value)
for value in grouped_data_numeral_1.values():
    ni_numeral_1.append(value)
for value in grouped_data_adverb_1.values():
    ni_adverb_1.append(value)
for value in grouped_data_nominative_pronoun_1.values():
    ni_nominative_pronoun_1.append(value)
for value in grouped_data_preposition_1.values():
    ni_preposition_1.append(value)
for value in grouped_data_conjunction_1.values():
    ni_conjunction_1.append(value)
for value in grouped_data_particle_1.values():
    ni_particle_1.append(value)
for value in grouped_data_interjection_1.values():
    ni_interjection_1.append(value)

############################################################### ВИБІРКА 2 ###############################################################

ni_noun_2 = []
ni_adjective_2 = []
ni_verb_2 = []
ni_gerund_2 = []
ni_numeral_2 = []
ni_adverb_2 = []
ni_nominative_pronoun_2 = []
ni_preposition_2 = []
ni_conjunction_2 = []
ni_particle_2 = []
ni_interjection_2 = []

for value in grouped_data_noun_2.values():
    ni_noun_2.append(value)
for value in grouped_data_adjective_2.values():
    ni_adjective_2.append(value)
for value in grouped_data_verb_2.values():
    ni_verb_2.append(value)
for value in grouped_data_gerund_2.values():
    ni_gerund_2.append(value)
for value in grouped_data_numeral_2.values():
    ni_numeral_2.append(value)
for value in grouped_data_adverb_2.values():
    ni_adverb_2.append(value)
for value in grouped_data_nominative_pronoun_2.values():
    ni_nominative_pronoun_2.append(value)
for value in grouped_data_preposition_2.values():
    ni_preposition_2.append(value)
for value in grouped_data_conjunction_2.values():
    ni_conjunction_2.append(value)
for value in grouped_data_particle_2.values():
    ni_particle_2.append(value)
for value in grouped_data_interjection_2.values():
    ni_interjection_2.append(value)

##########################################################################################################################################
##########################################################################################################################################
# знаходження суми кількотей варіянт для кожної частини мови
# (утворення нових змінних (значення - сума кількостей варіянт)
# (метод sum() до кожного списку кількостей варіянт))
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

sum_ni_noun_1 = sum(ni_noun_1)
sum_ni_adjective_1 = sum(ni_adjective_1)
sum_ni_verb_1 = sum(ni_verb_1)
sum_ni_gerund_1 = sum(ni_gerund_1)
sum_ni_numeral_1 = sum(ni_numeral_1)
sum_ni_adverb_1 = sum(ni_adverb_1)
sum_ni_nominative_pronoun_1= sum(ni_nominative_pronoun_1)
sum_ni_preposition_1 = sum(ni_preposition_1)
sum_ni_conjunction_1 = sum(ni_conjunction_1)
sum_ni_particle_1 = sum(ni_particle_1)
sum_ni_interjection_1 = sum(ni_interjection_1)

##########################################################################################################################################
# print(sum_ni_noun_1)
# print(sum_ni_adjective_1)
# print(sum_ni_verb_1)
# print(sum_ni_gerund_1)
# print(sum_ni_numeral_1)
# print(sum_ni_adverb_1)
# print(sum_ni_nominative_pronoun_1)
# print(sum_ni_preposition_1)
# print(sum_ni_conjunction_1)
# print(sum_ni_particle_1)
# print(sum_ni_interjection_1)
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

sum_ni_noun_2 = sum(ni_noun_2)
sum_ni_adjective_2 = sum(ni_adjective_2)
sum_ni_verb_2 = sum(ni_verb_2)
sum_ni_gerund_2 = sum(ni_gerund_2)
sum_ni_numeral_2 = sum(ni_numeral_2)
sum_ni_adverb_2 = sum(ni_adverb_2)
sum_ni_nominative_pronoun_2= sum(ni_nominative_pronoun_2)
sum_ni_preposition_2 = sum(ni_preposition_2)
sum_ni_conjunction_2 = sum(ni_conjunction_2)
sum_ni_particle_2 = sum(ni_particle_2)
sum_ni_interjection_2 = sum(ni_interjection_2)

##########################################################################################################################################
# print(sum_ni_noun_2)
# print(sum_ni_adjective_2)
# print(sum_ni_verb_2)
# print(sum_ni_gerund_2)
# print(sum_ni_numeral_2)
# print(sum_ni_adverb_2)
# print(sum_ni_nominative_pronoun_2)
# print(sum_ni_preposition_2)
# print(sum_ni_conjunction_2)
# print(sum_ni_particle_2)
# print(sum_ni_interjection_2)
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# знаходження добутку варіянти на її кількість для кожної частини мови
# для цього створено змінні, значеннями яких є ці добутки
# знову застосовано list comprehension, але тут він уже працює не з одним списком, як раніше, а з двома
# (робота більш ніж з одним списком можлива завдяки знайомому методу zip())
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

product_xi_ni_noun_1 = [a * b for a, b in zip(xi_noun_1, ni_noun_1)]
product_xi_ni_adjective_1 = [a * b for a, b in zip(xi_adjective_1, ni_adjective_1)]
product_xi_ni_verb_1 = [a * b for a, b in zip(xi_verb_1, ni_verb_1)]
product_xi_ni_gerund_1 = [a * b for a, b in zip(xi_gerund_1, ni_gerund_1)]
product_xi_ni_numeral_1 = [a * b for a, b in zip(xi_numeral_1, ni_numeral_1)]
product_xi_ni_adverb_1 = [a * b for a, b in zip(xi_adverb_1, ni_adverb_1)]
product_xi_ni_nominative_pronoun_1 = [a * b for a, b in zip(xi_nominative_pronoun_1, ni_nominative_pronoun_1)]
product_xi_ni_preposition_1 = [a * b for a, b in zip(xi_preposition_1, ni_preposition_1)]
product_xi_ni_conjunction_1 = [a * b for a, b in zip(xi_conjunction_1, ni_conjunction_1)]
product_xi_ni_particle_1 = [a * b for a, b in zip(xi_particle_1, ni_particle_1)]
product_xi_ni_interjection_1 = [a * b for a, b in zip(xi_interjection_1, ni_interjection_1)]

############################################################### ВИБІРКА 2 ###############################################################

product_xi_ni_noun_2 = [a * b for a, b in zip(xi_noun_2, ni_noun_2)]
product_xi_ni_adjective_2 = [a * b for a, b in zip(xi_adjective_2, ni_adjective_2)]
product_xi_ni_verb_2 = [a * b for a, b in zip(xi_verb_2, ni_verb_2)]
product_xi_ni_gerund_2 = [a * b for a, b in zip(xi_gerund_2, ni_gerund_2)]
product_xi_ni_numeral_2 = [a * b for a, b in zip(xi_numeral_2, ni_numeral_2)]
product_xi_ni_adverb_2 = [a * b for a, b in zip(xi_adverb_2, ni_adverb_2)]
product_xi_ni_nominative_pronoun_2 = [a * b for a, b in zip(xi_nominative_pronoun_2, ni_nominative_pronoun_2)]
product_xi_ni_preposition_2 = [a * b for a, b in zip(xi_preposition_2, ni_preposition_2)]
product_xi_ni_conjunction_2 = [a * b for a, b in zip(xi_conjunction_2, ni_conjunction_2)]
product_xi_ni_particle_2 = [a * b for a, b in zip(xi_particle_2, ni_particle_2)]
product_xi_ni_interjection_2 = [a * b for a, b in zip(xi_interjection_2, ni_interjection_2)]

##########################################################################################################################################
#########################################################################################################################################
# знаходження суми добутків варіянт на їхні кількості для кожної частини мови
# для цього створено нові змінні, значеннями яких є ці суми
# (метод sum())
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

sum_product_xi_ni_noun_1 = sum(product_xi_ni_noun_1)
sum_product_xi_ni_adjective_1 = sum(product_xi_ni_adjective_1)
sum_product_xi_ni_verb_1 = sum(product_xi_ni_verb_1)
sum_product_xi_ni_gerund_1 = sum(product_xi_ni_gerund_1)
sum_product_xi_ni_numeral_1 = sum(product_xi_ni_numeral_1)
sum_product_xi_ni_adverb_1 = sum(product_xi_ni_adverb_1)
sum_product_xi_ni_nomintaive_pronoun_1 = sum(product_xi_ni_nominative_pronoun_1)
sum_product_xi_ni_preposition_1 = sum(product_xi_ni_preposition_1)
sum_product_xi_ni_conjunction_1 = sum(product_xi_ni_conjunction_1)
sum_product_xi_ni_particle_1 = sum(product_xi_ni_particle_1)
sum_product_xi_ni_interjection_1 = sum(product_xi_ni_interjection_1)

############################################################### ВИБІРКА 2 ###############################################################

sum_product_xi_ni_noun_2 = sum(product_xi_ni_noun_2)
sum_product_xi_ni_adjective_2 = sum(product_xi_ni_adjective_2)
sum_product_xi_ni_verb_2 = sum(product_xi_ni_verb_2)
sum_product_xi_ni_gerund_2 = sum(product_xi_ni_gerund_2)
sum_product_xi_ni_numeral_2 = sum(product_xi_ni_numeral_2)
sum_product_xi_ni_adverb_2 = sum(product_xi_ni_adverb_2)
sum_product_xi_ni_nomintaive_pronoun_2 = sum(product_xi_ni_nominative_pronoun_2)
sum_product_xi_ni_preposition_2 = sum(product_xi_ni_preposition_2)
sum_product_xi_ni_conjunction_2 = sum(product_xi_ni_conjunction_2)
sum_product_xi_ni_particle_2 = sum(product_xi_ni_particle_2)
sum_product_xi_ni_interjection_2 = sum(product_xi_ni_interjection_2)

##########################################################################################################################################
##########################################################################################################################################
# знаходження середньої відносної частоти для кожної частини мови 
# для цього створено змінні, значеннями яких є суми добутків варіянтів на їхні кількості, поділені на суми кількостей варіянт
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

medium_x_noun_1 = sum_product_xi_ni_noun_1/sum_ni_noun_1
medium_x_adjective_1 = sum_product_xi_ni_adjective_1/sum_ni_adjective_1
medium_x_verb_1 = sum_product_xi_ni_verb_1/sum_ni_verb_1
medium_x_gerund_1 = sum_product_xi_ni_gerund_1/sum_ni_gerund_1
medium_x_numeral_1 = sum_product_xi_ni_numeral_1/sum_ni_numeral_1
medium_x_adverb_1 = sum_product_xi_ni_adverb_1/sum_ni_adverb_1
medium_x_nominative_pronoun_1 = sum_product_xi_ni_nomintaive_pronoun_1/sum_ni_nominative_pronoun_1
medium_x_preposition_1 = sum_product_xi_ni_preposition_1/sum_ni_preposition_1
medium_x_conjunction_1 = sum_product_xi_ni_conjunction_1/sum_ni_conjunction_1
medium_x_particle_1 = sum_product_xi_ni_particle_1/sum_ni_particle_1
medium_x_interjection_1 = sum_product_xi_ni_interjection_1/sum_ni_interjection_1

##########################################################################################################################################
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ІМЕННИКИ 1: ", medium_x_noun_1)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ПРИКМЕТНИКИ 1: ", medium_x_adjective_1)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ДІЄСЛОВА 1: ", medium_x_verb_1)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ДІЄПРИСЛІВНИКИ 1: ", medium_x_gerund_1)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ЧИСЛІВНИКИ 1: ", medium_x_numeral_1)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ПРИСЛІВНИКИ 1: ", medium_x_adverb_1)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", medium_x_nominative_pronoun_1)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ПРИЙМЕННИКИ 1: ", medium_x_preposition_1)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА СПОЛУЧНИКИ 1: ", medium_x_conjunction_1)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ЧАСТКИ 1: ", medium_x_particle_1)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ВИГУКИ 1: ", medium_x_interjection_1)
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

medium_x_noun_2 = sum_product_xi_ni_noun_2/sum_ni_noun_2
medium_x_adjective_2 = sum_product_xi_ni_adjective_2/sum_ni_adjective_2
medium_x_verb_2 = sum_product_xi_ni_verb_2/sum_ni_verb_2
medium_x_gerund_2 = sum_product_xi_ni_gerund_2/sum_ni_gerund_2
medium_x_numeral_2 = sum_product_xi_ni_numeral_2/sum_ni_numeral_2
medium_x_adverb_2 = sum_product_xi_ni_adverb_2/sum_ni_adverb_2
medium_x_nominative_pronoun_2 = sum_product_xi_ni_nomintaive_pronoun_2/sum_ni_nominative_pronoun_2
medium_x_preposition_2 = sum_product_xi_ni_preposition_2/sum_ni_preposition_2
medium_x_conjunction_2 = sum_product_xi_ni_conjunction_2/sum_ni_conjunction_2
medium_x_particle_2 = sum_product_xi_ni_particle_2/sum_ni_particle_2
medium_x_interjection_2 = sum_product_xi_ni_interjection_2/sum_ni_interjection_2

##########################################################################################################################################
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ІМЕННИКИ 2: ", medium_x_noun_2)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ПРИКМЕТНИКИ 2: ", medium_x_adjective_2)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ДІЄСЛОВА 2: ", medium_x_verb_2)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ДІЄПРИСЛІВНИКИ 2: ", medium_x_gerund_2)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ЧИСЛІВНИКИ 2: ", medium_x_numeral_2)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ПРИСЛІВНИКИ 2: ", medium_x_adverb_2)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ЗАЙМЕННИКИ-ІМЕННИКИ 2: ", medium_x_nominative_pronoun_2)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ПРИЙМЕННИКИ 2: ", medium_x_preposition_2)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА СПОЛУЧНИКИ 2: ", medium_x_conjunction_2)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ЧАСТКИ 2: ", medium_x_particle_2)
# print("СЕРЕДНЯ ВІДНОСНА ЧАСТОТА ВИГУКИ 2: ", medium_x_interjection_2)
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# знаходження середнього квадратичного відхилення для кожної частини мови
# для цього створено змінні, значеннями яких є середні квадратичні відхилення
# бачимо знайомі методи: sqrt() з бібліотеки math, list comprehension, zip() 
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

standard_deviation_noun_1 = math.sqrt(sum([((el1 - medium_x_noun_1)**2)*el2 for el1, el2 in zip(xi_noun_1, ni_noun_1)])/sum_ni_noun_1)
standard_deviation_adjective_1 = math.sqrt(sum([((el1 - medium_x_adjective_1)**2)*el2 for el1, el2 in zip(xi_adjective_1, ni_adjective_1)])/sum_ni_adjective_1)
standard_deviation_verb_1 = math.sqrt(sum([((el1 - medium_x_verb_1)**2)*el2 for el1, el2 in zip(xi_verb_1, ni_verb_1)])/sum_ni_verb_1)
standard_deviation_gerund_1 = math.sqrt(sum([((el1 - medium_x_gerund_1)**2)*el2 for el1, el2 in zip(xi_gerund_1, ni_gerund_1)])/sum_ni_gerund_1)
standard_deviation_numeral_1 = math.sqrt(sum([((el1 - medium_x_numeral_1)**2)*el2 for el1, el2 in zip(xi_numeral_1, ni_numeral_1)])/sum_ni_numeral_1)
standard_deviation_adverb_1 = math.sqrt(sum([((el1 - medium_x_adverb_1)**2)*el2 for el1, el2 in zip(xi_adverb_1, ni_adverb_1)])/sum_ni_adverb_1)
standard_deviation_nominative_pronoun_1 = math.sqrt(sum([((el1 - medium_x_nominative_pronoun_1)**2)*el2 for el1, el2 in zip(xi_nominative_pronoun_1, ni_nominative_pronoun_1)])/sum_ni_nominative_pronoun_1)
standard_deviation_preposition_1 = math.sqrt(sum([((el1 - medium_x_preposition_1)**2)*el2 for el1, el2 in zip(xi_preposition_1, ni_preposition_1)])/sum_ni_preposition_1)
standard_deviation_conjunction_1 = math.sqrt(sum([((el1 - medium_x_conjunction_1)**2)*el2 for el1, el2 in zip(xi_conjunction_1, ni_conjunction_1)])/sum_ni_conjunction_1)
standard_deviation_particle_1 = math.sqrt(sum([((el1 - medium_x_particle_1)**2)*el2 for el1, el2 in zip(xi_particle_1, ni_particle_1)])/sum_ni_particle_1)
standard_deviation_interjection_1 = math.sqrt(sum([((el1 - medium_x_interjection_1)**2)*el2 for el1, el2 in zip(xi_interjection_1, ni_interjection_1)])/sum_ni_interjection_1)

##########################################################################################################################################
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ІМЕННИКИ 1: ", standard_deviation_noun_1)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ПРИКМЕТНИКИ 1: ", standard_deviation_adjective_1)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ДІЄСЛОВА 1: ", standard_deviation_verb_1)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ДІЄПРИСЛІВНИКИ 1: ", standard_deviation_gerund_1)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ЧИСЛІВНИКИ 1: ", standard_deviation_numeral_1)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ПРИСЛІВНИКИ 1: ", standard_deviation_adverb_1)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", standard_deviation_nominative_pronoun_1)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ПРИЙМЕННИКИ 1: ", standard_deviation_preposition_1)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ СПОЛУЧНИКИ 1: ", standard_deviation_conjunction_1)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ЧАСТКИ 1: ", standard_deviation_particle_1)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ВИГУКИ 1: ", standard_deviation_interjection_1)
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

standard_deviation_noun_2 = math.sqrt(sum([((el2 - medium_x_noun_2)**2)*el2 for el2, el2 in zip(xi_noun_2, ni_noun_2)])/sum_ni_noun_2)
standard_deviation_adjective_2 = math.sqrt(sum([((el2 - medium_x_adjective_2)**2)*el2 for el2, el2 in zip(xi_adjective_2, ni_adjective_2)])/sum_ni_adjective_2)
standard_deviation_verb_2 = math.sqrt(sum([((el2 - medium_x_verb_2)**2)*el2 for el2, el2 in zip(xi_verb_2, ni_verb_2)])/sum_ni_verb_2)
standard_deviation_gerund_2 = math.sqrt(sum([((el2 - medium_x_gerund_2)**2)*el2 for el2, el2 in zip(xi_gerund_2, ni_gerund_2)])/sum_ni_gerund_2)
standard_deviation_numeral_2 = math.sqrt(sum([((el2 - medium_x_numeral_2)**2)*el2 for el2, el2 in zip(xi_numeral_2, ni_numeral_2)])/sum_ni_numeral_2)
standard_deviation_adverb_2 = math.sqrt(sum([((el2 - medium_x_adverb_2)**2)*el2 for el2, el2 in zip(xi_adverb_2, ni_adverb_2)])/sum_ni_adverb_2)
standard_deviation_nominative_pronoun_2 = math.sqrt(sum([((el2 - medium_x_nominative_pronoun_2)**2)*el2 for el2, el2 in zip(xi_nominative_pronoun_2, ni_nominative_pronoun_2)])/sum_ni_nominative_pronoun_2)
standard_deviation_preposition_2 = math.sqrt(sum([((el2 - medium_x_preposition_2)**2)*el2 for el2, el2 in zip(xi_preposition_2, ni_preposition_2)])/sum_ni_preposition_2)
standard_deviation_conjunction_2 = math.sqrt(sum([((el2 - medium_x_conjunction_2)**2)*el2 for el2, el2 in zip(xi_conjunction_2, ni_conjunction_2)])/sum_ni_conjunction_2)
standard_deviation_particle_2 = math.sqrt(sum([((el2 - medium_x_particle_2)**2)*el2 for el2, el2 in zip(xi_particle_2, ni_particle_2)])/sum_ni_particle_2)
standard_deviation_interjection_2 = math.sqrt(sum([((el2 - medium_x_interjection_2)**2)*el2 for el2, el2 in zip(xi_interjection_2, ni_interjection_2)])/sum_ni_interjection_2)

##########################################################################################################################################
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ІМЕННИКИ 2: ", standard_deviation_noun_2)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ПРИКМЕТНИКИ 2: ", standard_deviation_adjective_2)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ДІЄСЛОВА 2: ", standard_deviation_verb_2)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ДІЄПРИСЛІВНИКИ 2: ", standard_deviation_gerund_2)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ЧИСЛІВНИКИ 2: ", tandard_deviation_numeral_2)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ПРИСЛІВНИКИ 2: ", standard_deviation_adverb_2)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ЗАЙМЕННИКИ-ІМЕННИКИ 2: ", standard_deviation_nominative_pronoun_2)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ПРИЙМЕННИКИ 2: ", standard_deviation_preposition_2)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ СПОЛУЧНИКИ 2: ", standard_deviation_conjunction_2)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ЧАСТКИ 2: ", standard_deviation_particle_2)
# print("СЕРЕДНЄ КВАДРАТИЧНЕ ВІДХИЛЕННЯ ВИГУКИ 2: ", standard_deviation_interjection_2)
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# знаходження міри коливаня середньої частоти для кожної частини мови
# для цього створено змінні, значеннями яких є міри коливання середньої частоти
# у формулах бачимо поділ середніх квадратичних відхилень на квадратний корінь
# (метод sqrt() з бібліотеки math) сум кількостей варіянт 
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

standard_error_noun_1 = standard_deviation_noun_1/math.sqrt(sum_ni_noun_1)
standard_error_adjective_1 = standard_deviation_adjective_1/math.sqrt(sum_ni_adjective_1)
standard_error_verb_1 = standard_deviation_verb_1/math.sqrt(sum_ni_verb_1)
standard_error_gerund_1 = standard_deviation_gerund_1/math.sqrt(sum_ni_gerund_1)
standard_error_numeral_1 = standard_deviation_numeral_1/math.sqrt(sum_ni_numeral_1)
standard_error_adverb_1 = standard_deviation_adverb_1/math.sqrt(sum_ni_adverb_1)
standard_error_nominative_pronoun_1 = standard_deviation_nominative_pronoun_1/math.sqrt(sum_ni_nominative_pronoun_1)
standard_error_preposition_1 = standard_deviation_preposition_1/math.sqrt(sum_ni_preposition_1)
standard_error_conjunction_1 = standard_deviation_conjunction_1/math.sqrt(sum_ni_conjunction_1)
standard_error_particle_1 = standard_deviation_particle_1/math.sqrt(sum_ni_particle_1)
standard_error_interjection_1 = standard_deviation_interjection_1/math.sqrt(sum_ni_interjection_1)

##########################################################################################################################################
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ІМЕННИКИ 1: ", standard_error_noun_1)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ПРИКМЕТНИКИ 1: ", standard_error_adjective_1)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ДІЄСЛОВА 1: ", standard_error_verb_1)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ДІЄПРИСЛІВНИКИ 1: ", standard_error_gerund_1)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ЧИСЛІВНИКИ 1: ", standard_error_numeral_1)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ПРИСЛІВНИКИ 1: ", standard_error_adverb_1)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", standard_error_nominative_pronoun_1)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ПРИЙМЕННИКИ 1: ", standard_error_preposition_1)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ СПОЛУЧНИКИ 1: ", standard_error_conjunction_1)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ЧАСТКИ 1: ", standard_error_particle_1)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ВИГУКИ 1: ", standard_error_interjection_1)
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

standard_error_noun_2 = standard_deviation_noun_2/math.sqrt(sum_ni_noun_2)
standard_error_adjective_2 = standard_deviation_adjective_2/math.sqrt(sum_ni_adjective_2)
standard_error_verb_2 = standard_deviation_verb_2/math.sqrt(sum_ni_verb_2)
standard_error_gerund_2 = standard_deviation_gerund_2/math.sqrt(sum_ni_gerund_2)
standard_error_numeral_2 = standard_deviation_numeral_2/math.sqrt(sum_ni_numeral_2)
standard_error_adverb_2 = standard_deviation_adverb_2/math.sqrt(sum_ni_adverb_2)
standard_error_nominative_pronoun_2 = standard_deviation_nominative_pronoun_2/math.sqrt(sum_ni_nominative_pronoun_2)
standard_error_preposition_2 = standard_deviation_preposition_2/math.sqrt(sum_ni_preposition_2)
standard_error_conjunction_2 = standard_deviation_conjunction_2/math.sqrt(sum_ni_conjunction_2)
standard_error_particle_2 = standard_deviation_particle_2/math.sqrt(sum_ni_particle_2)
standard_error_interjection_2 = standard_deviation_interjection_2/math.sqrt(sum_ni_interjection_2)

##########################################################################################################################################
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ІМЕННИКИ 2: ", standard_error_noun_2)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ПРИКМЕТНИКИ 2: ", standard_error_adjective_2)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ДІЄСЛОВА 2: ", standard_error_verb_2)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ДІЄПРИСЛІВНИКИ 2: ", standard_error_gerund_2)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ЧИСЛІВНИКИ 2: ", standard_error_numeral_2)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ПРИСЛІВНИКИ 2: ", standard_error_adverb_2)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ЗАЙМЕННИКИ-ІМЕННИКИ 2: ", standard_error_nominative_pronoun_2)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ПРИЙМЕННИКИ 2: ", standard_error_preposition_2)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ СПОЛУЧНИКИ 2: ", standard_error_conjunction_2)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ЧАСТКИ 2: ", standard_error_particle_2)
# print("МІРА КОЛИВАННЯ СЕРЕДНЬОЇ ЧАСТОТИ ВИГУКИ 2: ", standard_error_interjection_2)
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# знаходження коєфіцієнтів варіяції для кожної частини мови
# для цього створено змінні, значеннями яких є ці коєфіцієнти 
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

coefficient_of_variation_noun_1 = standard_deviation_noun_1/medium_x_noun_1
coefficient_of_variation_adjective_1 = standard_deviation_adjective_1/medium_x_adjective_1
coefficient_of_variation_verb_1 = standard_deviation_verb_1/medium_x_verb_1
coefficient_of_variation_gerund_1 = standard_deviation_gerund_1/medium_x_gerund_1
coefficient_of_variation_numeral_1 = standard_deviation_numeral_1/medium_x_numeral_1
coefficient_of_variation_adverb_1 = standard_deviation_adverb_1/medium_x_adverb_1
coefficient_of_variation_nominative_pronoun_1 = standard_deviation_nominative_pronoun_1/medium_x_nominative_pronoun_1
coefficient_of_variation_preposition_1 = standard_deviation_preposition_1/medium_x_preposition_1
coefficient_of_variation_conjunction_1 = standard_deviation_conjunction_1/medium_x_conjunction_1
coefficient_of_variation_particle_1 = standard_deviation_particle_1/medium_x_particle_1
coefficient_of_variation_interjection_1 = standard_deviation_interjection_1/medium_x_interjection_1

##########################################################################################################################################
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ІМЕННИКИ 1: ", coefficient_of_variation_noun_1)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ПРИКМЕТНИКИ 1: ", coefficient_of_variation_adjective_1)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ДІЄСЛОВА 1: ", coefficient_of_variation_verb_1)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ДІЄПРИСЛІВНИКИ 1: ", coefficient_of_variation_gerund_1)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ЧИСЛІВНИКИ 1: ", coefficient_of_variation_numeral_1)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ПРИСЛІВНИКИ 1: ", coefficient_of_variation_adverb_1)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", coefficient_of_variation_nominative_pronoun_1)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ПРИЙМЕННИКИ 1: ", coefficient_of_variation_preposition_1)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ СПОЛУЧНИКИ 1: ", coefficient_of_variation_conjunction_1)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ЧАСТКИ 1: ", coefficient_of_variation_particle_1)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ВИГУКИ 1: ", coefficient_of_variation_interjection_1)
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

coefficient_of_variation_noun_2 = standard_deviation_noun_2/medium_x_noun_2
coefficient_of_variation_adjective_2 = standard_deviation_adjective_2/medium_x_adjective_2
coefficient_of_variation_verb_2 = standard_deviation_verb_2/medium_x_verb_2
coefficient_of_variation_gerund_2 = standard_deviation_gerund_2/medium_x_gerund_2
coefficient_of_variation_numeral_2 = standard_deviation_numeral_2/medium_x_numeral_2
coefficient_of_variation_adverb_2 = standard_deviation_adverb_2/medium_x_adverb_2
coefficient_of_variation_nominative_pronoun_2 = standard_deviation_nominative_pronoun_2/medium_x_nominative_pronoun_2
coefficient_of_variation_preposition_2 = standard_deviation_preposition_2/medium_x_preposition_2
coefficient_of_variation_conjunction_2 = standard_deviation_conjunction_2/medium_x_conjunction_2
coefficient_of_variation_particle_2 = standard_deviation_particle_2/medium_x_particle_2
coefficient_of_variation_interjection_2 = standard_deviation_interjection_2/medium_x_interjection_2

##########################################################################################################################################
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ІМЕННИКИ 2: ", coefficient_of_variation_noun_2)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ПРИКМЕТНИКИ 2: ", coefficient_of_variation_adjective_2)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ДІЄСЛОВА 2: ", coefficient_of_variation_verb_2)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ДІЄПРИСЛІВНИКИ 2: ", coefficient_of_variation_gerund_2)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ЧИСЛІВНИКИ 2: ", coefficient_of_variation_numeral_2)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ПРИСЛІВНИКИ 2: ", coefficient_of_variation_adverb_2)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ЗАЙМЕННИКИ-ІМЕННИКИ 2: ", coefficient_of_variation_nominative_pronoun_2)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ПРИЙМЕННИКИ 2: ", coefficient_of_variation_preposition_2)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ СПОЛУЧНИКИ 2: ", coefficient_of_variation_conjunction_2)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ЧАСТКИ 2: ", coefficient_of_variation_particle_2)
# print("КОЄФІЦІЄНТ ВАРІЯЦІЇ ВИГУКИ 2: ", coefficient_of_variation_interjection_2)
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# знаходження коєфіцієнтів стабільности для кожної частини мови
# тут відбувається те саме, що й для знаходження коєфіцієнтів варіяції
# (тільки формула інша) 
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

coefficient_of_stability_noun_1 = standard_deviation_noun_1/medium_x_noun_1*math.sqrt(sum_ni_noun_1-1)
coefficient_of_stability_adjective_1 = standard_deviation_adjective_1/medium_x_adjective_1*math.sqrt(sum_ni_adjective_1-1)
coefficient_of_stability_verb_1 = standard_deviation_verb_1/medium_x_verb_1*math.sqrt(sum_ni_verb_1-1)
coefficient_of_stability_gerund_1 = standard_deviation_gerund_1/medium_x_gerund_1*math.sqrt(sum_ni_gerund_1-1)
coefficient_of_stability_numeral_1 = standard_deviation_numeral_1/medium_x_numeral_1*math.sqrt(sum_ni_numeral_1-1)
coefficient_of_stability_adverb_1 = standard_deviation_adverb_1/medium_x_adverb_1*math.sqrt(sum_ni_adverb_1-1)
coefficient_of_stability_nominative_pronoun_1 = standard_deviation_nominative_pronoun_1/medium_x_nominative_pronoun_1*math.sqrt(sum_ni_nominative_pronoun_1-1)
coefficient_of_stability_preposition_1 = standard_deviation_preposition_1/medium_x_preposition_1*math.sqrt(sum_ni_preposition_1-1)
coefficient_of_stability_conjunction_1 = standard_deviation_conjunction_1/medium_x_conjunction_1*math.sqrt(sum_ni_conjunction_1-1)
coefficient_of_stability_particle_1 = standard_deviation_particle_1/medium_x_particle_1*math.sqrt(sum_ni_particle_1-1)
coefficient_of_stability_interjection_1 = standard_deviation_interjection_1/medium_x_interjection_1*math.sqrt(sum_ni_interjection_1-1)

##########################################################################################################################################
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ІМЕННИКИ 1: ", coefficient_of_stability_noun_1)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ПРИКМЕТНИКИ 1: ", coefficient_of_stability_adjective_1)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ДІЄСЛОВА 1: ", coefficient_of_stability_verb_1)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ДІЄПРИСЛІВНИКИ 1: ", coefficient_of_stability_gerund_1)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ЧИСЛІВНИКИ 1: ", coefficient_of_stability_numeral_1)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ПРИСЛІВНИКИ 1: ", coefficient_of_stability_adverb_1)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", coefficient_of_stability_nominative_pronoun_1)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ПРИЙМЕННИКИ 1: ", coefficient_of_stability_preposition_1)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ СПОЛУЧНИКИ 1: ", coefficient_of_stability_conjunction_1)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ЧАСТКИ 1: ", coefficient_of_stability_particle_1)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ВИГУКИ 1: ", coefficient_of_stability_interjection_1)
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

coefficient_of_stability_noun_2 = standard_deviation_noun_2/medium_x_noun_2*math.sqrt(sum_ni_noun_2-2)
coefficient_of_stability_adjective_2 = standard_deviation_adjective_2/medium_x_adjective_2*math.sqrt(sum_ni_adjective_2-2)
coefficient_of_stability_verb_2 = standard_deviation_verb_2/medium_x_verb_2*math.sqrt(sum_ni_verb_2-2)
coefficient_of_stability_gerund_2 = standard_deviation_gerund_2/medium_x_gerund_2*math.sqrt(sum_ni_gerund_2-2)
coefficient_of_stability_numeral_2 = standard_deviation_numeral_2/medium_x_numeral_2*math.sqrt(sum_ni_numeral_2-2)
coefficient_of_stability_adverb_2 = standard_deviation_adverb_2/medium_x_adverb_2*math.sqrt(sum_ni_adverb_2-2)
coefficient_of_stability_nominative_pronoun_2 = standard_deviation_nominative_pronoun_2/medium_x_nominative_pronoun_2*math.sqrt(sum_ni_nominative_pronoun_2-2)
coefficient_of_stability_preposition_2 = standard_deviation_preposition_2/medium_x_preposition_2*math.sqrt(sum_ni_preposition_2-2)
coefficient_of_stability_conjunction_2 = standard_deviation_conjunction_2/medium_x_conjunction_2*math.sqrt(sum_ni_conjunction_2-2)
coefficient_of_stability_particle_2 = standard_deviation_particle_2/medium_x_particle_2*math.sqrt(sum_ni_particle_2-2)
coefficient_of_stability_interjection_2 = standard_deviation_interjection_2/medium_x_interjection_2*math.sqrt(sum_ni_interjection_2-2)

##########################################################################################################################################
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ІМЕННИКИ 2: ", coefficient_of_stability_noun_2)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ПРИКМЕТНИКИ 2: ", coefficient_of_stability_adjective_2)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ДІЄСЛОВА 2: ", coefficient_of_stability_verb_2)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ДІЄПРИСЛІВНИКИ 2: ", coefficient_of_stability_gerund_2)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ЧИСЛІВНИКИ 2: ", coefficient_of_stability_numeral_2)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ПРИСЛІВНИКИ 2: ", coefficient_of_stability_adverb_2)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ЗАЙМЕННИКИ-ІМЕННИКИ 2: ", coefficient_of_stability_nominative_pronoun_2)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ПРИЙМЕННИКИ 2: ", coefficient_of_stability_preposition_2)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ СПОЛУЧНИКИ 2: ", coefficient_of_stability_conjunction_2)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ЧАСТКИ 2: ", coefficient_of_stability_particle_2)
# print("КОЄФІЦІЄНТ СТАБІЛЬНОСТИ ВИГУКИ 2: ", coefficient_of_stability_interjection_2)
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# вирахування величини інтервалу для іменника
# у квадратних дужках бачимо індекс -1 тому, що індексація елементів списку можлива не лише за допомогою описаного раніше способу
# (коли відлік починається з 0, елемент з індексом 0 є першим, елемент з індексом 1 є другим тощо),
# а й за допомогою мінусових індексів
# мінусові індекси починають відлік з -1 з кінця списку,
# тобто елемент з індексом -1 є першим з кінця, елемент з індексом -2 є другим з кінця тощо
# (на цьому моменті я починаю розуміти, що необов'язково було писати складний рядок для того,
# щоб відсортувати значення частотного словника у порядку зростання, а можна було просто застосувати
# метод list() до values() словника і в кінці написати індекси -1 i -2 у квадратних дужках для того,
# щоб дістати 2 найменш частотні словоформи)
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

h_interval_value_noun_1 = (xi_noun_1[-1]-xi_noun_1[0])/5

############################################################### ВИБІРКА 2 ###############################################################

h_interval_value_noun_2 = (xi_noun_2[-2]-xi_noun_2[0])/5

##########################################################################################################################################
##########################################################################################################################################
# створення порожнього списку інтервалів іменника, елементами якого будуть списки, елементами яких будуть значення меж інтервалів
# потрібно окремо створити порожні списки, елементами яких будуть значення меж інтервалів
# кількість цих порожніх списків залежить від того, на яке непарне число було поділено різницю найбільшої та найменшої варіянт
# (якщо на 5, буде 5 інтервалів, отже, треба створити 5 порожніх списків, якщо на 7, то 7 тощо)
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

intervals_noun_1 = []

############################################################### ВИБІРКА 2 ###############################################################

intervals_noun_2 = []

##########################################################################################################################################
##########################################################################################################################################
# до порожнього списку з межами першого інтервалу додаємо значення найменшої варіянти (перша межа)
# (метод append()), 
# далі загадуємо нову змінну, значенням якої є значення найменшої варіянти плюс величина інтервалу,
# потім до списку з межами першого інтервалу додаємо значення змінної (друга межа)
# (метод append()), 
# і нарешті додаємо список, де елементами є значення меж інтервалу, до порожнього списку інтервалів
# (метод append()),
# те саме пророблюємо з ще 4-ма інтервалами
# (до другої межі останнього інтервалу додаємо величину інтервалу, і так поки не буде 5 інтервалів)
# таким чином, здобуваємо список списків
# !!!УВАГА!!! описана в цьому блоці логіка відбувається з усіма частинами мови
# !!!УВАГА!!! при додаванні списку до списку потрібно враховувати, що метод append() дозволяє зберегти список у списку,
# тоді як метод extend() об'єднує ці 2 списки
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

interval_1_noun_1 = []
interval_1_noun_1.append(xi_noun_1[0])
boundary_interval_1_noun_1 = xi_noun_1[0] + h_interval_value_noun_1
interval_1_noun_1.append(boundary_interval_1_noun_1)
intervals_noun_1.append(interval_1_noun_1)

interval_2_noun_1 = []
interval_2_noun_1.append(boundary_interval_1_noun_1)
boundary_interval_2_noun_1 = boundary_interval_1_noun_1 + h_interval_value_noun_1
interval_2_noun_1.append(boundary_interval_2_noun_1)
intervals_noun_1.append(interval_2_noun_1)

interval_3_noun_1 = []
interval_3_noun_1.append(boundary_interval_2_noun_1)
boundary_interval_3_noun_1 = boundary_interval_2_noun_1 + h_interval_value_noun_1
interval_3_noun_1.append(boundary_interval_3_noun_1)
intervals_noun_1.append(interval_3_noun_1)

interval_4_noun_1 = []
interval_4_noun_1.append(boundary_interval_3_noun_1)
boundary_interval_4_noun_1 = boundary_interval_3_noun_1 + h_interval_value_noun_1
interval_4_noun_1.append(boundary_interval_4_noun_1)
intervals_noun_1.append(interval_4_noun_1)

interval_5_noun_1 = []
interval_5_noun_1.append(boundary_interval_4_noun_1)
boundary_interval_5_noun_1 = boundary_interval_4_noun_1 + h_interval_value_noun_1
interval_5_noun_1.append(boundary_interval_5_noun_1)
intervals_noun_1.append(interval_5_noun_1)

##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ІМЕННИКИ 1: ", intervals_noun_1)
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

interval_1_noun_2 = []
interval_1_noun_2.append(xi_noun_2[0])
boundary_interval_1_noun_2 = xi_noun_2[0] + h_interval_value_noun_2
interval_1_noun_2.append(boundary_interval_1_noun_2)
intervals_noun_2.append(interval_1_noun_2)

interval_2_noun_2 = []
interval_2_noun_2.append(boundary_interval_1_noun_2)
boundary_interval_2_noun_2 = boundary_interval_1_noun_2 + h_interval_value_noun_2
interval_2_noun_2.append(boundary_interval_2_noun_2)
intervals_noun_2.append(interval_2_noun_2)

interval_3_noun_2 = []
interval_3_noun_2.append(boundary_interval_2_noun_2)
boundary_interval_3_noun_2 = boundary_interval_2_noun_2 + h_interval_value_noun_2
interval_3_noun_2.append(boundary_interval_3_noun_2)
intervals_noun_2.append(interval_3_noun_2)

interval_4_noun_2 = []
interval_4_noun_2.append(boundary_interval_3_noun_2)
boundary_interval_4_noun_2 = boundary_interval_3_noun_2 + h_interval_value_noun_2
interval_4_noun_2.append(boundary_interval_4_noun_2)
intervals_noun_2.append(interval_4_noun_2)

interval_5_noun_2 = []
interval_5_noun_2.append(boundary_interval_4_noun_2)
boundary_interval_5_noun_2 = boundary_interval_4_noun_2 + h_interval_value_noun_2
interval_5_noun_2.append(boundary_interval_5_noun_2)
intervals_noun_2.append(interval_5_noun_2)

##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ІМЕННИКИ 2: ", intervals_noun_2)
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# знаходимо кількість абсолютних частот (АЧ) у межах кожного інтервалу
# для цього створюємо порожні списки, куди будемо додавати АЧ,
# пишемо цикл, який проходиться по списку АЧ,
# з умовою, яка перевіряє, чи АЧ більша від першої межі інтервалу й менша від другої межі,
# і тільки за виконання цих умов додає АЧ в новостворений список
# (метод append())
# після цього за допомогою методу append() додаємо довжину списків АЧ у межах інтервалів (метод len())
# і результатом буде список з 5-ма цифрами, де кожна цифра показує кількість АЧ у межах інтервалу
# !!!УВАГА!!! оскільки при утворенні інтервалів можливі випадки, коли друга межа останнього інтервалу менша від найбільшої АЧ
# і програма не додає цю АЧ в інтервал, то не завжди сума кількостей АЧ буде 20
# (тобто працюємо з 20-ма підвибірками в межах однієї вибірки, у кожній з цих підвибірок є певна кількість якоїсь частини мови,
# АЧ має бути 20, але при знаходженні кількостей АЧ у межах інтервалів
# не всі АЧ можуть увійти в останній інтервал, от і виходить, що сума кількостей АЧ
# не завжди дорівнює кількості підвибірок)
# як користувач (-ка) дізнається про те, у яких частинах мови відбуваються такі нюанси, можна буде побачити трохи згодом
# !!!УВАГА!!! описана в цьому блоці логіка відбувається з усіма частинами мови
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

ni_in_intervals_noun_1 = []
absolute_frequency_values_in_interval_1_noun_1 = []
absolute_frequency_values_in_interval_2_noun_1 = []
absolute_frequency_values_in_interval_3_noun_1 = []
absolute_frequency_values_in_interval_4_noun_1 = []
absolute_frequency_values_in_interval_5_noun_1 = []
for i in xi_noun_1:
    if i < interval_1_noun_1[-1]:
        absolute_frequency_values_in_interval_1_noun_1.append(i)
    elif i > interval_2_noun_1[0] and i < interval_2_noun_1[-1]:
        absolute_frequency_values_in_interval_2_noun_1.append(i)
    elif i > interval_3_noun_1[0] and i < interval_3_noun_1[-1]:
        absolute_frequency_values_in_interval_3_noun_1.append(i)
    elif i > interval_4_noun_1[0] and i < interval_4_noun_1[-1]:
        absolute_frequency_values_in_interval_4_noun_1.append(i)
    elif i > interval_5_noun_1[0]:
        absolute_frequency_values_in_interval_5_noun_1.append(i)
ni_in_intervals_noun_1.append(len(absolute_frequency_values_in_interval_1_noun_1))
ni_in_intervals_noun_1.append(len(absolute_frequency_values_in_interval_2_noun_1))
ni_in_intervals_noun_1.append(len(absolute_frequency_values_in_interval_3_noun_1))
ni_in_intervals_noun_1.append(len(absolute_frequency_values_in_interval_4_noun_1))
ni_in_intervals_noun_1.append(len(absolute_frequency_values_in_interval_5_noun_1))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ІМЕННИКИ 1: ",ni_in_intervals_noun_1)  
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

ni_in_intervals_noun_2 = []
absolute_frequency_values_in_interval_1_noun_2 = []
absolute_frequency_values_in_interval_2_noun_2 = []
absolute_frequency_values_in_interval_3_noun_2 = []
absolute_frequency_values_in_interval_4_noun_2 = []
absolute_frequency_values_in_interval_5_noun_2 = []
for i in xi_noun_2:
    if i < interval_1_noun_2[-1]:
        absolute_frequency_values_in_interval_1_noun_2.append(i)
    elif i > interval_2_noun_2[0] and i < interval_2_noun_2[-1]:
        absolute_frequency_values_in_interval_2_noun_2.append(i)
    elif i > interval_3_noun_2[0] and i < interval_3_noun_2[-1]:
        absolute_frequency_values_in_interval_3_noun_2.append(i)
    elif i > interval_4_noun_2[0] and i < interval_4_noun_2[-1]:
        absolute_frequency_values_in_interval_4_noun_2.append(i)
    elif i > interval_5_noun_2[0]:
        absolute_frequency_values_in_interval_5_noun_2.append(i)
ni_in_intervals_noun_2.append(len(absolute_frequency_values_in_interval_1_noun_2))
ni_in_intervals_noun_2.append(len(absolute_frequency_values_in_interval_2_noun_2))
ni_in_intervals_noun_2.append(len(absolute_frequency_values_in_interval_3_noun_2))
ni_in_intervals_noun_2.append(len(absolute_frequency_values_in_interval_4_noun_2))
ni_in_intervals_noun_2.append(len(absolute_frequency_values_in_interval_5_noun_2))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ІМЕННИКИ 2: ",ni_in_intervals_noun_2)
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# вираховуємо середини інтервалів
# для цього створюємо список, елементами якого є списки, елементами якого є середини інтервалів
# (можна було, звісно, просто створити список із серединами інтервалів, але, на мою думку,
# зручніше дивитися на список списків, бо відразу видно, що це не просто список чисел, а значення,
# які існують відокремлено одне від одного; це так, просто для візуального сприйняття
# (могло ж бути не 5 інтервалів, а 11, 15 тощо)),
# далі пишемо цикл, який проходиться по списку абсолютних частот у межах інтервалу,
# створює змінну, значенням якої є сума першого й останнього елемента цього списку
# (знову бачимо різну індексацію),
# поділена на 2
# потім, уже за межами циклу, додаємо знайдену середину інтервалу до порожнього списку,
# створеного спеціяльно для цієї середини,
# і цей список із серединою інтервалу додаємо до списку середин інтервалів
# !!!УВАГА!!! описана в цьому блоці логіка відбувається з усіма інтервалами й усіма частинами мови
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

mediums_intervals_noun_1 = []

medium_1_intervals_noun_1 = []
for item in interval_1_noun_1:
    middlepoint_1_noun_1 = (interval_1_noun_1[0] + interval_1_noun_1[-1]) / 2
medium_1_intervals_noun_1.append(middlepoint_1_noun_1)
mediums_intervals_noun_1.append(medium_1_intervals_noun_1)

medium_2_intervals_noun_1 = []
for item in interval_2_noun_1:
    middlepoint_2_noun_1 = (interval_2_noun_1[0] + interval_2_noun_1[-1]) / 2
medium_2_intervals_noun_1.append(middlepoint_2_noun_1)
mediums_intervals_noun_1.append(medium_2_intervals_noun_1)

medium_3_intervals_noun_1 = []
for item in interval_3_noun_1:
    middlepoint_3_noun_1 = (interval_3_noun_1[0] + interval_3_noun_1[-1]) / 2
medium_3_intervals_noun_1.append(middlepoint_3_noun_1)
mediums_intervals_noun_1.append(medium_3_intervals_noun_1)

medium_4_intervals_noun_1 = []
for item in interval_4_noun_1:
    middlepoint_4_noun_1 = (interval_4_noun_1[0] + interval_4_noun_1[-1]) / 2
medium_4_intervals_noun_1.append(middlepoint_4_noun_1)
mediums_intervals_noun_1.append(medium_4_intervals_noun_1)

medium_5_intervals_noun_1 = []
for item in interval_5_noun_1:
    middlepoint_5_noun_1 = (interval_5_noun_1[0] + interval_5_noun_1[-1]) / 2
medium_5_intervals_noun_1.append(middlepoint_5_noun_1)
mediums_intervals_noun_1.append(medium_5_intervals_noun_1)

##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ІМЕННИКИ 1: ", mediums_intervals_noun_1)
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

mediums_intervals_noun_2 = []

medium_1_intervals_noun_2 = []
for item in interval_1_noun_2:
    middlepoint_1_noun_2 = (interval_1_noun_2[0] + interval_1_noun_2[-1]) / 2
medium_1_intervals_noun_2.append(middlepoint_1_noun_2)
mediums_intervals_noun_2.append(medium_1_intervals_noun_2)

medium_2_intervals_noun_2 = []
for item in interval_2_noun_2:
    middlepoint_2_noun_2 = (interval_2_noun_2[0] + interval_2_noun_2[-1]) / 2
medium_2_intervals_noun_2.append(middlepoint_2_noun_2)
mediums_intervals_noun_2.append(medium_2_intervals_noun_2)

medium_3_intervals_noun_2 = []
for item in interval_3_noun_2:
    middlepoint_3_noun_2 = (interval_3_noun_2[0] + interval_3_noun_2[-1]) / 2
medium_3_intervals_noun_2.append(middlepoint_3_noun_2)
mediums_intervals_noun_2.append(medium_3_intervals_noun_2)

medium_4_intervals_noun_2 = []
for item in interval_4_noun_2:
    middlepoint_4_noun_2 = (interval_4_noun_2[0] + interval_4_noun_2[-1]) / 2
medium_4_intervals_noun_2.append(middlepoint_4_noun_2)
mediums_intervals_noun_2.append(medium_4_intervals_noun_2)

medium_5_intervals_noun_2 = []
for item in interval_5_noun_2:
    middlepoint_5_noun_2 = (interval_5_noun_2[0] + interval_5_noun_2[-1]) / 2
medium_5_intervals_noun_2.append(middlepoint_5_noun_2)
mediums_intervals_noun_2.append(medium_5_intervals_noun_2)

##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ІМЕННИКИ 2: ", mediums_intervals_noun_2)
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# знаходимо середнє квадратичне відхилення для інтервального ряду
# для цього створємо змінні, значеннями яких є різниці середин інтервалів та середніх частот,
# піднесені до квадрата й помножені на кількості абсолютних частот у межах інтервалів
# далі ці змінні потрібно додати (створюємо змінну, де значенням є сума попередніх змінних),
# а потім створити змінну, значенням якої є середнє квадратичне відхилення для інтервального ряду
# (здобуваємо квадратний корінь за допомогою методу sqrt() (бібліотека math)
# з частки суми значень змінних, створених у цьому блоці
# (де різниця середин інтервалів та середніх частот,
# піднесені до квадрата й помножені на кількості абсолютних частот у межах інтервалів)
# та суми кількостей абсолютних частот у межах інтервалів (метод sum()))
# !!!УВАГА!!! описана в цьому блоці логіка відбувається з усіма частинами мови
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

xi_minus_medium_x_power_two_multiply_ni_1_noun_1 = (medium_1_intervals_noun_1[0] - medium_x_noun_1)**2*ni_in_intervals_noun_1[0]
xi_minus_medium_x_power_two_multiply_ni_2_noun_1 = (medium_2_intervals_noun_1[0] - medium_x_noun_1)**2*ni_in_intervals_noun_1[1]
xi_minus_medium_x_power_two_multiply_ni_3_noun_1 = (medium_3_intervals_noun_1[0] - medium_x_noun_1)**2*ni_in_intervals_noun_1[2]
xi_minus_medium_x_power_two_multiply_ni_4_noun_1 = (medium_4_intervals_noun_1[0] - medium_x_noun_1)**2*ni_in_intervals_noun_1[3]
xi_minus_medium_x_power_two_multiply_ni_5_noun_1 = (medium_5_intervals_noun_1[0] - medium_x_noun_1)**2*ni_in_intervals_noun_1[4]
sum_xi_minus_medium_x_power_two_multiply_ni_noun_1 = (xi_minus_medium_x_power_two_multiply_ni_1_noun_1
                                                    + xi_minus_medium_x_power_two_multiply_ni_2_noun_1
                                                    + xi_minus_medium_x_power_two_multiply_ni_3_noun_1
                                                    + xi_minus_medium_x_power_two_multiply_ni_4_noun_1
                                                    + xi_minus_medium_x_power_two_multiply_ni_5_noun_1)
standard_deviation_for_intervals_noun_1 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_noun_1/sum(ni_in_intervals_noun_1))

##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_noun_1)
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

xi_minus_medium_x_power_two_multiply_ni_2_noun_2 = (medium_2_intervals_noun_2[0] - medium_x_noun_2)**2*ni_in_intervals_noun_2[0]
xi_minus_medium_x_power_two_multiply_ni_2_noun_2 = (medium_2_intervals_noun_2[0] - medium_x_noun_2)**2*ni_in_intervals_noun_2[2]
xi_minus_medium_x_power_two_multiply_ni_3_noun_2 = (medium_3_intervals_noun_2[0] - medium_x_noun_2)**2*ni_in_intervals_noun_2[2]
xi_minus_medium_x_power_two_multiply_ni_4_noun_2 = (medium_4_intervals_noun_2[0] - medium_x_noun_2)**2*ni_in_intervals_noun_2[3]
xi_minus_medium_x_power_two_multiply_ni_5_noun_2 = (medium_5_intervals_noun_2[0] - medium_x_noun_2)**2*ni_in_intervals_noun_2[4]
sum_xi_minus_medium_x_power_two_multiply_ni_noun_2 = (xi_minus_medium_x_power_two_multiply_ni_2_noun_2
                                                    + xi_minus_medium_x_power_two_multiply_ni_2_noun_2
                                                    + xi_minus_medium_x_power_two_multiply_ni_3_noun_2
                                                    + xi_minus_medium_x_power_two_multiply_ni_4_noun_2
                                                    + xi_minus_medium_x_power_two_multiply_ni_5_noun_2)
standard_deviation_for_intervals_noun_2 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_noun_2/sum(ni_in_intervals_noun_2))

##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_noun_2)
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# знаходимо кількість абсолютних частот у смугах коливання 68% та 95%
# для цього створюємо порожній список для меж смуги коливання 68%
# та порожній список для меж смуги коливання 95%,
# загадуємо 2 нові змінні, значеннями яких є межі смуги коливання, вирахувані за формулами
# "середня частота - середнє квадратичне відхилення для інтервального ряду" (нижня межа) та
# "середня частота + середнє квадратичне відхилення для інтервального ряду" (верхня межа)
# (для смуги коливання 95% також загадуємо 2 нові змінні,
# але значення саме цих 2 змінних вираховуємо за формулами
# "середня частота - 2 * середнє квадратичне відхилення для інтервального ряду" (нижня межа) та
# "середня частота + 2 * середнє квадратичне відхилення для інтервального ряду" (верхня межа)),
# потім за допомогою знайомого методу append() додаємо ці 2 змінні до новоствореного списку
# (так само зі смугою коливання 95%)
# після цього створємо 2 порожні списки, куди будемо додавати абсолютні частоти в межах смуг коливання
# (один список для смуги коливання 68%, другий - для смуги коливання 95%)
# пишемо 2 цикли, які проходиться по всім абсолютним частотам певної частини мови, і,
# якщо абсолютна частота більша або дорівнює нижній межі смуги коливання та менша або дорівнює верхній межі смуги коливання,
# додає абсолютну частоту в новостворений список (метод append())
# !!!УВАГА!!! описана в цьому блоці логіка відбувається з усіма частинами мови
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

boundaries_for_absolute_frequencies_distribution_68_per_cent_noun_1 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_noun_1 = medium_x_noun_1 - standard_deviation_for_intervals_noun_1
boundary_2_for_absolute_frequencies_distribution_68_per_cent_noun_1 = medium_x_noun_1 + standard_deviation_for_intervals_noun_1
boundaries_for_absolute_frequencies_distribution_68_per_cent_noun_1.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_noun_1)
boundaries_for_absolute_frequencies_distribution_68_per_cent_noun_1.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_noun_1)
absolute_frequencies_distribution_68_per_cent_noun_1 = []
for i in xi_noun_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_noun_1 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_noun_1:
        absolute_frequencies_distribution_68_per_cent_noun_1.append(i)
# print(absolute_frequencies_distribution_68_per_cent_noun_1)

##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ІМЕННИКИ 1: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_noun_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ІМЕННИКИ 1: ", len(absolute_frequencies_distribution_68_per_cent_noun_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

boundaries_for_absolute_frequencies_distribution_68_per_cent_noun_2 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_noun_2 = medium_x_noun_2 - standard_deviation_for_intervals_noun_2
boundary_2_for_absolute_frequencies_distribution_68_per_cent_noun_2 = medium_x_noun_2 + standard_deviation_for_intervals_noun_2
boundaries_for_absolute_frequencies_distribution_68_per_cent_noun_2.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_noun_2)
boundaries_for_absolute_frequencies_distribution_68_per_cent_noun_2.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_noun_2)
absolute_frequencies_distribution_68_per_cent_noun_2 = []
for i in xi_noun_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_noun_2 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_noun_2:
        absolute_frequencies_distribution_68_per_cent_noun_2.append(i)

##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ІМЕННИКИ 2: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_noun_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ІМЕННИКИ 2: ", len(absolute_frequencies_distribution_68_per_cent_noun_2))
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

boundaries_for_absolute_frequencies_distribution_95_per_cent_noun_1 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_noun_1 = medium_x_noun_1 - 2*standard_deviation_for_intervals_noun_1
boundary_2_for_absolute_frequencies_distribution_95_per_cent_noun_1 = medium_x_noun_1 + 2*standard_deviation_for_intervals_noun_1
boundaries_for_absolute_frequencies_distribution_95_per_cent_noun_1.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_noun_1)
boundaries_for_absolute_frequencies_distribution_95_per_cent_noun_1.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_noun_1)
absolute_frequencies_distribution_95_per_cent_noun_1 = []
for i in xi_noun_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_noun_1 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_noun_1:
        absolute_frequencies_distribution_95_per_cent_noun_1.append(i)

##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ІМЕННИКИ 1: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_noun_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ІМЕННИКИ 1: ", len(absolute_frequencies_distribution_95_per_cent_noun_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

boundaries_for_absolute_frequencies_distribution_95_per_cent_noun_2 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_noun_2 = medium_x_noun_2 - 2*standard_deviation_for_intervals_noun_2
boundary_2_for_absolute_frequencies_distribution_95_per_cent_noun_2 = medium_x_noun_2 + 2*standard_deviation_for_intervals_noun_2
boundaries_for_absolute_frequencies_distribution_95_per_cent_noun_2.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_noun_2)
boundaries_for_absolute_frequencies_distribution_95_per_cent_noun_2.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_noun_2)
absolute_frequencies_distribution_95_per_cent_noun_2 = []
for i in xi_noun_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_noun_2 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_noun_2:
        absolute_frequencies_distribution_95_per_cent_noun_2.append(i)

##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ІМЕННИКИ 2: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_noun_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ІМЕННИКИ 2: ", len(absolute_frequencies_distribution_95_per_cent_noun_2))
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

h_interval_value_adjective_1 = (xi_adjective_1[-1]-xi_adjective_1[0])/5

intervals_adjective_1 = []

interval_1_adjective_1 = []
interval_1_adjective_1.append(xi_adjective_1[0])
boundary_interval_1_adjective_1 = xi_adjective_1[0] + h_interval_value_adjective_1
interval_1_adjective_1.append(boundary_interval_1_adjective_1)
intervals_adjective_1.append(interval_1_adjective_1)

interval_2_adjective_1 = []
interval_2_adjective_1.append(boundary_interval_1_adjective_1)
boundary_interval_2_adjective_1 = boundary_interval_1_adjective_1 + h_interval_value_adjective_1
interval_2_adjective_1.append(boundary_interval_2_adjective_1)
intervals_adjective_1.append(interval_2_adjective_1)

interval_3_adjective_1 = []
interval_3_adjective_1.append(boundary_interval_2_adjective_1)
boundary_interval_3_adjective_1 = boundary_interval_2_adjective_1 + h_interval_value_adjective_1
interval_3_adjective_1.append(boundary_interval_3_adjective_1)
intervals_adjective_1.append(interval_3_adjective_1)

interval_4_adjective_1 = []
interval_4_adjective_1.append(boundary_interval_3_adjective_1)
boundary_interval_4_adjective_1 = boundary_interval_3_adjective_1 + h_interval_value_adjective_1
interval_4_adjective_1.append(boundary_interval_4_adjective_1)
intervals_adjective_1.append(interval_4_adjective_1)

interval_5_adjective_1 = []
interval_5_adjective_1.append(boundary_interval_4_adjective_1)
boundary_interval_5_adjective_1 = boundary_interval_4_adjective_1 + h_interval_value_adjective_1
interval_5_adjective_1.append(boundary_interval_5_adjective_1)
intervals_adjective_1.append(interval_5_adjective_1)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ПРИКМЕТНИКИ 1: ", intervals_adjective_1)
##########################################################################################################################################

ni_in_intervals_adjective_1 = []
absolute_frequency_values_in_interval_1_adjective_1 = []
absolute_frequency_values_in_interval_2_adjective_1 = []
absolute_frequency_values_in_interval_3_adjective_1 = []
absolute_frequency_values_in_interval_4_adjective_1 = []
absolute_frequency_values_in_interval_5_adjective_1 = []
for i in xi_adjective_1:
    if i < interval_1_adjective_1[-1]:
        absolute_frequency_values_in_interval_1_adjective_1.append(i)
    elif i > interval_2_adjective_1[0] and i < interval_2_adjective_1[-1]:
        absolute_frequency_values_in_interval_2_adjective_1.append(i)
    elif i > interval_3_adjective_1[0] and i < interval_3_adjective_1[-1]:
        absolute_frequency_values_in_interval_3_adjective_1.append(i)
    elif i > interval_4_adjective_1[0] and i < interval_4_adjective_1[-1]:
        absolute_frequency_values_in_interval_4_adjective_1.append(i)
    elif i > interval_5_adjective_1[0]:
        absolute_frequency_values_in_interval_5_adjective_1.append(i)
ni_in_intervals_adjective_1.append(len(absolute_frequency_values_in_interval_1_adjective_1))
ni_in_intervals_adjective_1.append(len(absolute_frequency_values_in_interval_2_adjective_1))
ni_in_intervals_adjective_1.append(len(absolute_frequency_values_in_interval_3_adjective_1))
ni_in_intervals_adjective_1.append(len(absolute_frequency_values_in_interval_4_adjective_1))
ni_in_intervals_adjective_1.append(len(absolute_frequency_values_in_interval_5_adjective_1))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ПРИКМЕТНИКИ 1: ",ni_in_intervals_adjective_1)
##########################################################################################################################################

mediums_intervals_adjective_1 = []

medium_1_intervals_adjective_1 = []
for item in interval_1_adjective_1:
    middlepoint_1_adjective_1 = (interval_1_adjective_1[0] + interval_1_adjective_1[-1]) / 2
medium_1_intervals_adjective_1.append(middlepoint_1_adjective_1)
mediums_intervals_adjective_1.append(medium_1_intervals_adjective_1)

medium_2_intervals_adjective_1 = []
for item in interval_2_adjective_1:
    middlepoint_2_adjective_1 = (interval_2_adjective_1[0] + interval_2_adjective_1[-1]) / 2
medium_2_intervals_adjective_1.append(middlepoint_2_adjective_1)
mediums_intervals_adjective_1.append(medium_2_intervals_adjective_1)

medium_3_intervals_adjective_1 = []
for item in interval_3_adjective_1:
    middlepoint_3_adjective_1 = (interval_3_adjective_1[0] + interval_3_adjective_1[-1]) / 2
medium_3_intervals_adjective_1.append(middlepoint_3_adjective_1)
mediums_intervals_adjective_1.append(medium_3_intervals_adjective_1)

medium_4_intervals_adjective_1 = []
for item in interval_4_adjective_1:
    middlepoint_4_adjective_1 = (interval_4_adjective_1[0] + interval_4_adjective_1[-1]) / 2
medium_4_intervals_adjective_1.append(middlepoint_4_adjective_1)
mediums_intervals_adjective_1.append(medium_4_intervals_adjective_1)

medium_5_intervals_adjective_1 = []
for item in interval_5_adjective_1:
    middlepoint_5_adjective_1 = (interval_5_adjective_1[0] + interval_5_adjective_1[-1]) / 2
medium_5_intervals_adjective_1.append(middlepoint_5_adjective_1)
mediums_intervals_adjective_1.append(medium_5_intervals_adjective_1)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ПРИКМЕТНИКИ 1: ", mediums_intervals_adjective_1)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_1_adjective_1 = (medium_1_intervals_adjective_1[0] - medium_x_adjective_1)**2*ni_in_intervals_adjective_1[0]
xi_minus_medium_x_power_two_multiply_ni_2_adjective_1 = (medium_2_intervals_adjective_1[0] - medium_x_adjective_1)**2*ni_in_intervals_adjective_1[1]
xi_minus_medium_x_power_two_multiply_ni_3_adjective_1 = (medium_3_intervals_adjective_1[0] - medium_x_adjective_1)**2*ni_in_intervals_adjective_1[2]
xi_minus_medium_x_power_two_multiply_ni_4_adjective_1 = (medium_4_intervals_adjective_1[0] - medium_x_adjective_1)**2*ni_in_intervals_adjective_1[3]
xi_minus_medium_x_power_two_multiply_ni_5_adjective_1 = (medium_5_intervals_adjective_1[0] - medium_x_adjective_1)**2*ni_in_intervals_adjective_1[4]
sum_xi_minus_medium_x_power_two_multiply_ni_adjective_1 = (xi_minus_medium_x_power_two_multiply_ni_1_adjective_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_2_adjective_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_3_adjective_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_4_adjective_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_5_adjective_1)
standard_deviation_for_intervals_adjective_1 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_adjective_1/sum(ni_in_intervals_adjective_1))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_adjective_1)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_adjective_1 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_adjective_1 = medium_x_adjective_1 - standard_deviation_for_intervals_adjective_1
boundary_2_for_absolute_frequencies_distribution_68_per_cent_adjective_1 = medium_x_adjective_1 + standard_deviation_for_intervals_adjective_1
boundaries_for_absolute_frequencies_distribution_68_per_cent_adjective_1.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_adjective_1)
boundaries_for_absolute_frequencies_distribution_68_per_cent_adjective_1.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_adjective_1)
absolute_frequencies_distribution_68_per_cent_adjective_1 = []
for i in xi_adjective_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_adjective_1 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_adjective_1:
        absolute_frequencies_distribution_68_per_cent_adjective_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ПРИКМЕТНИКИ 1: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_adjective_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ПРИКМЕТНИКИ 1: ", len(absolute_frequencies_distribution_68_per_cent_adjective_1))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_adjective_1 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_adjective_1 = medium_x_adjective_1 - 2*standard_deviation_for_intervals_adjective_1
boundary_2_for_absolute_frequencies_distribution_95_per_cent_adjective_1 = medium_x_adjective_1 + 2*standard_deviation_for_intervals_adjective_1
boundaries_for_absolute_frequencies_distribution_95_per_cent_adjective_1.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_adjective_1)
boundaries_for_absolute_frequencies_distribution_95_per_cent_adjective_1.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_adjective_1)
absolute_frequencies_distribution_95_per_cent_adjective_1 = []
for i in xi_adjective_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_adjective_1 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_adjective_1:
        absolute_frequencies_distribution_95_per_cent_adjective_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ПРИКМЕТНИКИ 1: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_adjective_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ПРИКМЕТНИКИ 1: ", len(absolute_frequencies_distribution_95_per_cent_adjective_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

h_interval_value_adjective_2 = (xi_adjective_2[-2]-xi_adjective_2[0])/5

intervals_adjective_2 = []

interval_1_adjective_2 = []
interval_1_adjective_2.append(xi_adjective_2[0])
boundary_interval_1_adjective_2 = xi_adjective_2[0] + h_interval_value_adjective_2
interval_1_adjective_2.append(boundary_interval_1_adjective_2)
intervals_adjective_2.append(interval_1_adjective_2)

interval_2_adjective_2 = []
interval_2_adjective_2.append(boundary_interval_1_adjective_2)
boundary_interval_2_adjective_2 = boundary_interval_1_adjective_2 + h_interval_value_adjective_2
interval_2_adjective_2.append(boundary_interval_2_adjective_2)
intervals_adjective_2.append(interval_2_adjective_2)

interval_3_adjective_2 = []
interval_3_adjective_2.append(boundary_interval_2_adjective_2)
boundary_interval_3_adjective_2 = boundary_interval_2_adjective_2 + h_interval_value_adjective_2
interval_3_adjective_2.append(boundary_interval_3_adjective_2)
intervals_adjective_2.append(interval_3_adjective_2)

interval_4_adjective_2 = []
interval_4_adjective_2.append(boundary_interval_3_adjective_2)
boundary_interval_4_adjective_2 = boundary_interval_3_adjective_2 + h_interval_value_adjective_2
interval_4_adjective_2.append(boundary_interval_4_adjective_2)
intervals_adjective_2.append(interval_4_adjective_2)

interval_5_adjective_2 = []
interval_5_adjective_2.append(boundary_interval_4_adjective_2)
boundary_interval_5_adjective_2 = boundary_interval_4_adjective_2 + h_interval_value_adjective_2
interval_5_adjective_2.append(boundary_interval_5_adjective_2)
intervals_adjective_2.append(interval_5_adjective_2)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ПРИКМЕТНИКИ 2: ", intervals_adjective_2)
##########################################################################################################################################

ni_in_intervals_adjective_2 = []
absolute_frequency_values_in_interval_1_adjective_2 = []
absolute_frequency_values_in_interval_2_adjective_2 = []
absolute_frequency_values_in_interval_3_adjective_2 = []
absolute_frequency_values_in_interval_4_adjective_2 = []
absolute_frequency_values_in_interval_5_adjective_2 = []
for i in xi_adjective_2:
    if i < interval_1_adjective_2[-1]:
        absolute_frequency_values_in_interval_1_adjective_2.append(i)
    elif i > interval_2_adjective_2[0] and i < interval_2_adjective_2[-1]:
        absolute_frequency_values_in_interval_2_adjective_2.append(i)
    elif i > interval_3_adjective_2[0] and i < interval_3_adjective_2[-1]:
        absolute_frequency_values_in_interval_3_adjective_2.append(i)
    elif i > interval_4_adjective_2[0] and i < interval_4_adjective_2[-1]:
        absolute_frequency_values_in_interval_4_adjective_2.append(i)
    elif i > interval_5_adjective_2[0]:
        absolute_frequency_values_in_interval_5_adjective_2.append(i)
ni_in_intervals_adjective_2.append(len(absolute_frequency_values_in_interval_1_adjective_2))
ni_in_intervals_adjective_2.append(len(absolute_frequency_values_in_interval_2_adjective_2))
ni_in_intervals_adjective_2.append(len(absolute_frequency_values_in_interval_3_adjective_2))
ni_in_intervals_adjective_2.append(len(absolute_frequency_values_in_interval_4_adjective_2))
ni_in_intervals_adjective_2.append(len(absolute_frequency_values_in_interval_5_adjective_2))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ПРИКМЕТНИКИ 2: ",ni_in_intervals_adjective_2)
##########################################################################################################################################

mediums_intervals_adjective_2 = []

medium_1_intervals_adjective_2 = []
for item in interval_1_adjective_2:
    middlepoint_1_adjective_2 = (interval_1_adjective_2[0] + interval_1_adjective_2[-1]) / 2
medium_1_intervals_adjective_2.append(middlepoint_1_adjective_2)
mediums_intervals_adjective_2.append(medium_1_intervals_adjective_2)

medium_2_intervals_adjective_2 = []
for item in interval_2_adjective_2:
    middlepoint_2_adjective_2 = (interval_2_adjective_2[0] + interval_2_adjective_2[-1]) / 2
medium_2_intervals_adjective_2.append(middlepoint_2_adjective_2)
mediums_intervals_adjective_2.append(medium_2_intervals_adjective_2)

medium_3_intervals_adjective_2 = []
for item in interval_3_adjective_2:
    middlepoint_3_adjective_2 = (interval_3_adjective_2[0] + interval_3_adjective_2[-1]) / 2
medium_3_intervals_adjective_2.append(middlepoint_3_adjective_2)
mediums_intervals_adjective_2.append(medium_3_intervals_adjective_2)

medium_4_intervals_adjective_2 = []
for item in interval_4_adjective_2:
    middlepoint_4_adjective_2 = (interval_4_adjective_2[0] + interval_4_adjective_2[-1]) / 2
medium_4_intervals_adjective_2.append(middlepoint_4_adjective_2)
mediums_intervals_adjective_2.append(medium_4_intervals_adjective_2)

medium_5_intervals_adjective_2 = []
for item in interval_5_adjective_2:
    middlepoint_5_adjective_2 = (interval_5_adjective_2[0] + interval_5_adjective_2[-1]) / 2
medium_5_intervals_adjective_2.append(middlepoint_5_adjective_2)
mediums_intervals_adjective_2.append(medium_5_intervals_adjective_2)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ПРИКМЕТНИКИ 2: ", mediums_intervals_adjective_2)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_2_adjective_2 = (medium_2_intervals_adjective_2[0] - medium_x_adjective_2)**2*ni_in_intervals_adjective_2[0]
xi_minus_medium_x_power_two_multiply_ni_2_adjective_2 = (medium_2_intervals_adjective_2[0] - medium_x_adjective_2)**2*ni_in_intervals_adjective_2[2]
xi_minus_medium_x_power_two_multiply_ni_3_adjective_2 = (medium_3_intervals_adjective_2[0] - medium_x_adjective_2)**2*ni_in_intervals_adjective_2[2]
xi_minus_medium_x_power_two_multiply_ni_4_adjective_2 = (medium_4_intervals_adjective_2[0] - medium_x_adjective_2)**2*ni_in_intervals_adjective_2[3]
xi_minus_medium_x_power_two_multiply_ni_5_adjective_2 = (medium_5_intervals_adjective_2[0] - medium_x_adjective_2)**2*ni_in_intervals_adjective_2[4]
sum_xi_minus_medium_x_power_two_multiply_ni_adjective_2 = (xi_minus_medium_x_power_two_multiply_ni_2_adjective_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_2_adjective_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_3_adjective_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_4_adjective_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_5_adjective_2)
standard_deviation_for_intervals_adjective_2 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_adjective_2/sum(ni_in_intervals_adjective_2))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_adjective_2)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_adjective_2 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_adjective_2 = medium_x_adjective_2 - standard_deviation_for_intervals_adjective_2
boundary_2_for_absolute_frequencies_distribution_68_per_cent_adjective_2 = medium_x_adjective_2 + standard_deviation_for_intervals_adjective_2
boundaries_for_absolute_frequencies_distribution_68_per_cent_adjective_2.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_adjective_2)
boundaries_for_absolute_frequencies_distribution_68_per_cent_adjective_2.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_adjective_2)
absolute_frequencies_distribution_68_per_cent_adjective_2 = []
for i in xi_adjective_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_adjective_2 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_adjective_2:
        absolute_frequencies_distribution_68_per_cent_adjective_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ПРИКМЕТНИКИ 2: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_adjective_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ПРИКМЕТНИКИ 2: ", len(absolute_frequencies_distribution_68_per_cent_adjective_2))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_adjective_2 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_adjective_2 = medium_x_adjective_2 - 2*standard_deviation_for_intervals_adjective_2
boundary_2_for_absolute_frequencies_distribution_95_per_cent_adjective_2 = medium_x_adjective_2 + 2*standard_deviation_for_intervals_adjective_2
boundaries_for_absolute_frequencies_distribution_95_per_cent_adjective_2.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_adjective_2)
boundaries_for_absolute_frequencies_distribution_95_per_cent_adjective_2.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_adjective_2)
absolute_frequencies_distribution_95_per_cent_adjective_2 = []
for i in xi_adjective_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_adjective_2 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_adjective_2:
        absolute_frequencies_distribution_95_per_cent_adjective_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ПРИКМЕТНИКИ 2: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_adjective_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ПРИКМЕТНИКИ 2: ", len(absolute_frequencies_distribution_95_per_cent_adjective_2))
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

h_interval_value_verb_1 = (xi_verb_1[-1]-xi_verb_1[0])/5

intervals_verb_1 = []

interval_1_verb_1 = []
interval_1_verb_1.append(xi_verb_1[0])
boundary_interval_1_verb_1 = xi_verb_1[0] + h_interval_value_verb_1
interval_1_verb_1.append(boundary_interval_1_verb_1)
intervals_verb_1.append(interval_1_verb_1)

interval_2_verb_1 = []
interval_2_verb_1.append(boundary_interval_1_verb_1)
boundary_interval_2_verb_1 = boundary_interval_1_verb_1 + h_interval_value_verb_1
interval_2_verb_1.append(boundary_interval_2_verb_1)
intervals_verb_1.append(interval_2_verb_1)

interval_3_verb_1 = []
interval_3_verb_1.append(boundary_interval_2_verb_1)
boundary_interval_3_verb_1 = boundary_interval_2_verb_1 + h_interval_value_verb_1
interval_3_verb_1.append(boundary_interval_3_verb_1)
intervals_verb_1.append(interval_3_verb_1)

interval_4_verb_1 = []
interval_4_verb_1.append(boundary_interval_3_verb_1)
boundary_interval_4_verb_1 = boundary_interval_3_verb_1 + h_interval_value_verb_1
interval_4_verb_1.append(boundary_interval_4_verb_1)
intervals_verb_1.append(interval_4_verb_1)

interval_5_verb_1 = []
interval_5_verb_1.append(boundary_interval_4_verb_1)
boundary_interval_5_verb_1 = boundary_interval_4_verb_1 + h_interval_value_verb_1
interval_5_verb_1.append(boundary_interval_5_verb_1)
intervals_verb_1.append(interval_5_verb_1)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ДІЄСЛОВА 1: ", intervals_verb_1)
##########################################################################################################################################

ni_in_intervals_verb_1 = []
absolute_frequency_values_in_interval_1_verb_1 = []
absolute_frequency_values_in_interval_2_verb_1 = []
absolute_frequency_values_in_interval_3_verb_1 = []
absolute_frequency_values_in_interval_4_verb_1 = []
absolute_frequency_values_in_interval_5_verb_1 = []
for i in xi_verb_1:
    if i < interval_1_verb_1[-1]:
        absolute_frequency_values_in_interval_1_verb_1.append(i)
    elif i > interval_2_verb_1[0] and i < interval_2_verb_1[-1]:
        absolute_frequency_values_in_interval_2_verb_1.append(i)
    elif i > interval_2_verb_1[0] and i < interval_3_verb_1[-1]:
        absolute_frequency_values_in_interval_3_verb_1.append(i)
    elif i > interval_4_verb_1[0] and i < interval_4_verb_1[-1]:
        absolute_frequency_values_in_interval_4_verb_1.append(i)
    elif i > interval_5_verb_1[0]:
        absolute_frequency_values_in_interval_5_verb_1.append(i)
ni_in_intervals_verb_1.append(len(absolute_frequency_values_in_interval_1_verb_1))
ni_in_intervals_verb_1.append(len(absolute_frequency_values_in_interval_2_verb_1))
ni_in_intervals_verb_1.append(len(absolute_frequency_values_in_interval_3_verb_1))
ni_in_intervals_verb_1.append(len(absolute_frequency_values_in_interval_4_verb_1))
ni_in_intervals_verb_1.append(len(absolute_frequency_values_in_interval_5_verb_1))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ДІЄСЛОВА 1: ",ni_in_intervals_verb_1)
##########################################################################################################################################

mediums_intervals_verb_1 = []

medium_1_intervals_verb_1 = []
for item in interval_1_verb_1:
    middlepoint_1_verb_1 = (interval_1_verb_1[0] + interval_1_verb_1[-1]) / 2
medium_1_intervals_verb_1.append(middlepoint_1_verb_1)
mediums_intervals_verb_1.append(medium_1_intervals_verb_1)

medium_2_intervals_verb_1 = []
for item in interval_2_verb_1:
    middlepoint_2_verb_1 = (interval_2_verb_1[0] + interval_2_verb_1[-1]) / 2
medium_2_intervals_verb_1.append(middlepoint_2_verb_1)
mediums_intervals_verb_1.append(medium_2_intervals_verb_1)

medium_3_intervals_verb_1 = []
for item in interval_3_verb_1:
    middlepoint_3_verb_1 = (interval_3_verb_1[0] + interval_3_verb_1[-1]) / 2
medium_3_intervals_verb_1.append(middlepoint_3_verb_1)
mediums_intervals_verb_1.append(medium_3_intervals_verb_1)

medium_4_intervals_verb_1 = []
for item in interval_4_verb_1:
    middlepoint_4_verb_1 = (interval_4_verb_1[0] + interval_4_verb_1[-1]) / 2
medium_4_intervals_verb_1.append(middlepoint_4_verb_1)
mediums_intervals_verb_1.append(medium_4_intervals_verb_1)

medium_5_intervals_verb_1 = []
for item in interval_5_verb_1:
    middlepoint_5_verb_1 = (interval_5_verb_1[0] + interval_5_verb_1[-1]) / 2
medium_5_intervals_verb_1.append(middlepoint_5_verb_1)
mediums_intervals_verb_1.append(medium_5_intervals_verb_1)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ДІЄСЛОВА 1: ", mediums_intervals_verb_1)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_1_verb_1 = (medium_1_intervals_verb_1[0] - medium_x_verb_1)**2*ni_in_intervals_verb_1[0]
xi_minus_medium_x_power_two_multiply_ni_2_verb_1 = (medium_2_intervals_verb_1[0] - medium_x_verb_1)**2*ni_in_intervals_verb_1[1]
xi_minus_medium_x_power_two_multiply_ni_3_verb_1 = (medium_3_intervals_verb_1[0] - medium_x_verb_1)**2*ni_in_intervals_verb_1[2]
xi_minus_medium_x_power_two_multiply_ni_4_verb_1 = (medium_4_intervals_verb_1[0] - medium_x_verb_1)**2*ni_in_intervals_verb_1[3]
xi_minus_medium_x_power_two_multiply_ni_5_verb_1 = (medium_5_intervals_verb_1[0] - medium_x_verb_1)**2*ni_in_intervals_verb_1[4]
sum_xi_minus_medium_x_power_two_multiply_ni_verb_1 = (xi_minus_medium_x_power_two_multiply_ni_1_verb_1
                                                    + xi_minus_medium_x_power_two_multiply_ni_2_verb_1
                                                    + xi_minus_medium_x_power_two_multiply_ni_3_verb_1
                                                    + xi_minus_medium_x_power_two_multiply_ni_4_verb_1
                                                    + xi_minus_medium_x_power_two_multiply_ni_5_verb_1)
standard_deviation_for_intervals_verb_1 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_verb_1/sum(ni_in_intervals_verb_1))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_verb_1)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_verb_1 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_verb_1 = medium_x_verb_1 - standard_deviation_for_intervals_verb_1
boundary_2_for_absolute_frequencies_distribution_68_per_cent_verb_1 = medium_x_verb_1 + standard_deviation_for_intervals_verb_1
boundaries_for_absolute_frequencies_distribution_68_per_cent_verb_1.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_verb_1)
boundaries_for_absolute_frequencies_distribution_68_per_cent_verb_1.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_verb_1)
absolute_frequencies_distribution_68_per_cent_verb_1 = []
for i in xi_verb_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_verb_1 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_verb_1:
        absolute_frequencies_distribution_68_per_cent_verb_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ДІЄСЛОВА 1: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_verb_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ДІЄСЛОВА 1: ", len(absolute_frequencies_distribution_68_per_cent_verb_1))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_verb_1 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_verb_1 = medium_x_verb_1 - 2*standard_deviation_for_intervals_verb_1
boundary_2_for_absolute_frequencies_distribution_95_per_cent_verb_1 = medium_x_verb_1 + 2*standard_deviation_for_intervals_verb_1
boundaries_for_absolute_frequencies_distribution_95_per_cent_verb_1.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_verb_1)
boundaries_for_absolute_frequencies_distribution_95_per_cent_verb_1.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_verb_1)
absolute_frequencies_distribution_95_per_cent_verb_1 = []
for i in xi_verb_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_verb_1 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_verb_1:
        absolute_frequencies_distribution_95_per_cent_verb_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ДІЄСЛОВА 1: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_verb_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ДІЄСЛОВА 1: ", len(absolute_frequencies_distribution_95_per_cent_verb_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

h_interval_value_verb_2 = (xi_verb_2[-2]-xi_verb_2[0])/5

intervals_verb_2 = []

interval_1_verb_2 = []
interval_1_verb_2.append(xi_verb_2[0])
boundary_interval_1_verb_2 = xi_verb_2[0] + h_interval_value_verb_2
interval_1_verb_2.append(boundary_interval_1_verb_2)
intervals_verb_2.append(interval_1_verb_2)

interval_2_verb_2 = []
interval_2_verb_2.append(boundary_interval_1_verb_2)
boundary_interval_2_verb_2 = boundary_interval_1_verb_2 + h_interval_value_verb_2
interval_2_verb_2.append(boundary_interval_2_verb_2)
intervals_verb_2.append(interval_2_verb_2)

interval_3_verb_2 = []
interval_3_verb_2.append(boundary_interval_2_verb_2)
boundary_interval_3_verb_2 = boundary_interval_2_verb_2 + h_interval_value_verb_2
interval_3_verb_2.append(boundary_interval_3_verb_2)
intervals_verb_2.append(interval_3_verb_2)

interval_4_verb_2 = []
interval_4_verb_2.append(boundary_interval_3_verb_2)
boundary_interval_4_verb_2 = boundary_interval_3_verb_2 + h_interval_value_verb_2
interval_4_verb_2.append(boundary_interval_4_verb_2)
intervals_verb_2.append(interval_4_verb_2)

interval_5_verb_2 = []
interval_5_verb_2.append(boundary_interval_4_verb_2)
boundary_interval_5_verb_2 = boundary_interval_4_verb_2 + h_interval_value_verb_2
interval_5_verb_2.append(boundary_interval_5_verb_2)
intervals_verb_2.append(interval_5_verb_2)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ДІЄСЛОВА 2: ", intervals_verb_2)
##########################################################################################################################################

ni_in_intervals_verb_2 = []
absolute_frequency_values_in_interval_1_verb_2 = []
absolute_frequency_values_in_interval_2_verb_2 = []
absolute_frequency_values_in_interval_3_verb_2 = []
absolute_frequency_values_in_interval_4_verb_2 = []
absolute_frequency_values_in_interval_5_verb_2 = []
for i in xi_verb_2:
    if i < interval_1_verb_2[-1]:
        absolute_frequency_values_in_interval_1_verb_2.append(i)
    elif i > interval_2_verb_2[0] and i < interval_2_verb_2[-1]:
        absolute_frequency_values_in_interval_2_verb_2.append(i)
    elif i > interval_3_verb_2[0] and i < interval_3_verb_2[-1]:
        absolute_frequency_values_in_interval_3_verb_2.append(i)
    elif i > interval_4_verb_2[0] and i < interval_4_verb_2[-1]:
        absolute_frequency_values_in_interval_4_verb_2.append(i)
    elif i > interval_5_verb_2[0]:
        absolute_frequency_values_in_interval_5_verb_2.append(i)
ni_in_intervals_verb_2.append(len(absolute_frequency_values_in_interval_1_verb_2))
ni_in_intervals_verb_2.append(len(absolute_frequency_values_in_interval_2_verb_2))
ni_in_intervals_verb_2.append(len(absolute_frequency_values_in_interval_3_verb_2))
ni_in_intervals_verb_2.append(len(absolute_frequency_values_in_interval_4_verb_2))
ni_in_intervals_verb_2.append(len(absolute_frequency_values_in_interval_5_verb_2))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ДІЄСЛОВА 2: ", ni_in_intervals_verb_2)
##########################################################################################################################################

mediums_intervals_verb_2 = []

medium_1_intervals_verb_2 = []
for item in interval_1_verb_2:
    middlepoint_1_verb_2 = (interval_1_verb_2[0] + interval_1_verb_2[-1]) / 2
medium_1_intervals_verb_2.append(middlepoint_1_verb_2)
mediums_intervals_verb_2.append(medium_1_intervals_verb_2)

medium_2_intervals_verb_2 = []
for item in interval_2_verb_2:
    middlepoint_2_verb_2 = (interval_2_verb_2[0] + interval_2_verb_2[-1]) / 2
medium_2_intervals_verb_2.append(middlepoint_2_verb_2)
mediums_intervals_verb_2.append(medium_2_intervals_verb_2)

medium_3_intervals_verb_2 = []
for item in interval_3_verb_2:
    middlepoint_3_verb_2 = (interval_3_verb_2[0] + interval_3_verb_2[-1]) / 2
medium_3_intervals_verb_2.append(middlepoint_3_verb_2)
mediums_intervals_verb_2.append(medium_3_intervals_verb_2)

medium_4_intervals_verb_2 = []
for item in interval_4_verb_2:
    middlepoint_4_verb_2 = (interval_4_verb_2[0] + interval_4_verb_2[-1]) / 2
medium_4_intervals_verb_2.append(middlepoint_4_verb_2)
mediums_intervals_verb_2.append(medium_4_intervals_verb_2)

medium_5_intervals_verb_2 = []
for item in interval_5_verb_2:
    middlepoint_5_verb_2 = (interval_5_verb_2[0] + interval_5_verb_2[-1]) / 2
medium_5_intervals_verb_2.append(middlepoint_5_verb_2)
mediums_intervals_verb_2.append(medium_5_intervals_verb_2)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ДІЄСЛОВА 2: ", mediums_intervals_verb_2)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_2_verb_2 = (medium_2_intervals_verb_2[0] - medium_x_verb_2)**2*ni_in_intervals_verb_2[0]
xi_minus_medium_x_power_two_multiply_ni_2_verb_2 = (medium_2_intervals_verb_2[0] - medium_x_verb_2)**2*ni_in_intervals_verb_2[2]
xi_minus_medium_x_power_two_multiply_ni_3_verb_2 = (medium_3_intervals_verb_2[0] - medium_x_verb_2)**2*ni_in_intervals_verb_2[2]
xi_minus_medium_x_power_two_multiply_ni_4_verb_2 = (medium_4_intervals_verb_2[0] - medium_x_verb_2)**2*ni_in_intervals_verb_2[3]
xi_minus_medium_x_power_two_multiply_ni_5_verb_2 = (medium_5_intervals_verb_2[0] - medium_x_verb_2)**2*ni_in_intervals_verb_2[4]
sum_xi_minus_medium_x_power_two_multiply_ni_verb_2 = (xi_minus_medium_x_power_two_multiply_ni_2_verb_2
                                                    + xi_minus_medium_x_power_two_multiply_ni_2_verb_2
                                                    + xi_minus_medium_x_power_two_multiply_ni_3_verb_2
                                                    + xi_minus_medium_x_power_two_multiply_ni_4_verb_2
                                                    + xi_minus_medium_x_power_two_multiply_ni_5_verb_2)
standard_deviation_for_intervals_verb_2 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_verb_2/sum(ni_in_intervals_verb_2))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_verb_2)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_verb_2 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_verb_2 = medium_x_verb_2 - standard_deviation_for_intervals_verb_2
boundary_2_for_absolute_frequencies_distribution_68_per_cent_verb_2 = medium_x_verb_2 + standard_deviation_for_intervals_verb_2
boundaries_for_absolute_frequencies_distribution_68_per_cent_verb_2.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_verb_2)
boundaries_for_absolute_frequencies_distribution_68_per_cent_verb_2.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_verb_2)
absolute_frequencies_distribution_68_per_cent_verb_2 = []
for i in xi_verb_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_verb_2 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_verb_2:
        absolute_frequencies_distribution_68_per_cent_verb_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ДІЄСЛОВА 2: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_verb_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ДІЄСЛОВА 2: ", len(absolute_frequencies_distribution_68_per_cent_verb_2))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_verb_2 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_verb_2 = medium_x_verb_2 - 2*standard_deviation_for_intervals_verb_2
boundary_2_for_absolute_frequencies_distribution_95_per_cent_verb_2 = medium_x_verb_2 + 2*standard_deviation_for_intervals_verb_2
boundaries_for_absolute_frequencies_distribution_95_per_cent_verb_2.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_verb_2)
boundaries_for_absolute_frequencies_distribution_95_per_cent_verb_2.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_verb_2)
absolute_frequencies_distribution_95_per_cent_verb_2 = []
for i in xi_verb_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_verb_2 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_verb_2:
        absolute_frequencies_distribution_95_per_cent_verb_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ДІЄСЛОВА 2: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_verb_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ДІЄСЛОВА 2: ", len(absolute_frequencies_distribution_95_per_cent_verb_2))
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

h_interval_value_gerund_1 = (xi_gerund_1[-1]-xi_gerund_1[0])/5

intervals_gerund_1 = []

interval_1_gerund_1 = []
interval_1_gerund_1.append(xi_gerund_1[0])
boundary_interval_1_gerund_1 = xi_gerund_1[0] + h_interval_value_gerund_1
interval_1_gerund_1.append(boundary_interval_1_gerund_1)
intervals_gerund_1.append(interval_1_gerund_1)

interval_2_gerund_1 = []
interval_2_gerund_1.append(boundary_interval_1_gerund_1)
boundary_interval_2_gerund_1 = boundary_interval_1_gerund_1 + h_interval_value_gerund_1
interval_2_gerund_1.append(boundary_interval_2_gerund_1)
intervals_gerund_1.append(interval_2_gerund_1)

interval_3_gerund_1 = []
interval_3_gerund_1.append(boundary_interval_2_gerund_1)
boundary_interval_3_gerund_1 = boundary_interval_2_gerund_1 + h_interval_value_gerund_1
interval_3_gerund_1.append(boundary_interval_3_gerund_1)
intervals_gerund_1.append(interval_3_gerund_1)

interval_4_gerund_1 = []
interval_4_gerund_1.append(boundary_interval_3_gerund_1)
boundary_interval_4_gerund_1 = boundary_interval_3_gerund_1 + h_interval_value_gerund_1
interval_4_gerund_1.append(boundary_interval_4_gerund_1)
intervals_gerund_1.append(interval_4_gerund_1)

interval_5_gerund_1 = []
interval_5_gerund_1.append(boundary_interval_4_gerund_1)
boundary_interval_5_gerund_1 = boundary_interval_4_gerund_1 + h_interval_value_gerund_1
interval_5_gerund_1.append(boundary_interval_5_gerund_1)
intervals_gerund_1.append(interval_5_gerund_1)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ДІЄПРИСЛІВНИКИ 1: ", intervals_gerund_1)
##########################################################################################################################################

ni_in_intervals_gerund_1 = []
absolute_frequency_values_in_interval_1_gerund_1 = []
absolute_frequency_values_in_interval_2_gerund_1 = []
absolute_frequency_values_in_interval_3_gerund_1 = []
absolute_frequency_values_in_interval_4_gerund_1 = []
absolute_frequency_values_in_interval_5_gerund_1 = []
for i in xi_gerund_1:
    if i < interval_1_gerund_1[-1]:
        absolute_frequency_values_in_interval_1_gerund_1.append(i)
    elif i > interval_2_gerund_1[0] and i < interval_2_gerund_1[-1]:
        absolute_frequency_values_in_interval_2_gerund_1.append(i)
    elif i > interval_3_gerund_1[0] and i < interval_3_gerund_1[-1]:
        absolute_frequency_values_in_interval_3_gerund_1.append(i)
    elif i > interval_4_gerund_1[0] and i < interval_4_gerund_1[-1]:
        absolute_frequency_values_in_interval_4_gerund_1.append(i)
    elif i > interval_5_gerund_1[0]:
        absolute_frequency_values_in_interval_5_gerund_1.append(i)
ni_in_intervals_gerund_1.append(len(absolute_frequency_values_in_interval_1_gerund_1))
ni_in_intervals_gerund_1.append(len(absolute_frequency_values_in_interval_2_gerund_1))
ni_in_intervals_gerund_1.append(len(absolute_frequency_values_in_interval_3_gerund_1))
ni_in_intervals_gerund_1.append(len(absolute_frequency_values_in_interval_4_gerund_1))
ni_in_intervals_gerund_1.append(len(absolute_frequency_values_in_interval_5_gerund_1))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ДІЄСПРИСЛІВНИКИ 1: ", ni_in_intervals_gerund_1)
##########################################################################################################################################

mediums_intervals_gerund_1 = []

medium_1_intervals_gerund_1 = []
for item in interval_1_gerund_1:
    middlepoint_1_gerund_1 = (interval_1_gerund_1[0] + interval_1_gerund_1[-1]) / 2
medium_1_intervals_gerund_1.append(middlepoint_1_gerund_1)
mediums_intervals_gerund_1.append(medium_1_intervals_gerund_1)

medium_2_intervals_gerund_1 = []
for item in interval_2_gerund_1:
    middlepoint_2_gerund_1 = (interval_2_gerund_1[0] + interval_2_gerund_1[-1]) / 2
medium_2_intervals_gerund_1.append(middlepoint_2_gerund_1)
mediums_intervals_gerund_1.append(medium_2_intervals_gerund_1)

medium_3_intervals_gerund_1 = []
for item in interval_3_gerund_1:
    middlepoint_3_gerund_1 = (interval_3_gerund_1[0] + interval_3_gerund_1[-1]) / 2
medium_3_intervals_gerund_1.append(middlepoint_3_gerund_1)
mediums_intervals_gerund_1.append(medium_3_intervals_gerund_1)

medium_4_intervals_gerund_1 = []
for item in interval_4_gerund_1:
    middlepoint_4_gerund_1 = (interval_4_gerund_1[0] + interval_4_gerund_1[-1]) / 2
medium_4_intervals_gerund_1.append(middlepoint_4_gerund_1)
mediums_intervals_gerund_1.append(medium_4_intervals_gerund_1)

medium_5_intervals_gerund_1 = []
for item in interval_5_gerund_1:
    middlepoint_5_gerund_1 = (interval_5_gerund_1[0] + interval_5_gerund_1[-1]) / 2
medium_5_intervals_gerund_1.append(middlepoint_5_gerund_1)
mediums_intervals_gerund_1.append(medium_5_intervals_gerund_1)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ДІЄПРИСЛІВНИКИ 1: ", mediums_intervals_gerund_1)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_1_gerund_1 = (medium_1_intervals_gerund_1[0] - medium_x_gerund_1)**2*ni_in_intervals_gerund_1[0]
xi_minus_medium_x_power_two_multiply_ni_2_gerund_1 = (medium_2_intervals_gerund_1[0] - medium_x_gerund_1)**2*ni_in_intervals_gerund_1[1]
xi_minus_medium_x_power_two_multiply_ni_3_gerund_1 = (medium_3_intervals_gerund_1[0] - medium_x_gerund_1)**2*ni_in_intervals_gerund_1[2]
xi_minus_medium_x_power_two_multiply_ni_4_gerund_1 = (medium_4_intervals_gerund_1[0] - medium_x_gerund_1)**2*ni_in_intervals_gerund_1[3]
xi_minus_medium_x_power_two_multiply_ni_5_gerund_1 = (medium_5_intervals_gerund_1[0] - medium_x_gerund_1)**2*ni_in_intervals_gerund_1[4]
sum_xi_minus_medium_x_power_two_multiply_ni_gerund_1 = (xi_minus_medium_x_power_two_multiply_ni_1_gerund_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_2_gerund_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_3_gerund_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_4_gerund_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_5_gerund_1)
standard_deviation_for_intervals_gerund_1 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_gerund_1/sum(ni_in_intervals_gerund_1))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_gerund_1)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_gerund_1 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_gerund_1 = medium_x_gerund_1 - standard_deviation_for_intervals_gerund_1
boundary_2_for_absolute_frequencies_distribution_68_per_cent_gerund_1 = medium_x_gerund_1 + standard_deviation_for_intervals_gerund_1
boundaries_for_absolute_frequencies_distribution_68_per_cent_gerund_1.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_gerund_1)
boundaries_for_absolute_frequencies_distribution_68_per_cent_gerund_1.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_gerund_1)
absolute_frequencies_distribution_68_per_cent_gerund_1 = []
for i in xi_gerund_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_gerund_1 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_gerund_1:
        absolute_frequencies_distribution_68_per_cent_gerund_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ДІЄПРИСЛІВНИКИ 1: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_gerund_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ДІЄПРИСЛІВНИКИ 1: ", len(absolute_frequencies_distribution_68_per_cent_gerund_1))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_gerund_1 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_gerund_1 = medium_x_gerund_1 - 2*standard_deviation_for_intervals_gerund_1
boundary_2_for_absolute_frequencies_distribution_95_per_cent_gerund_1 = medium_x_gerund_1 + 2*standard_deviation_for_intervals_gerund_1
boundaries_for_absolute_frequencies_distribution_95_per_cent_gerund_1.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_gerund_1)
boundaries_for_absolute_frequencies_distribution_95_per_cent_gerund_1.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_gerund_1)
absolute_frequencies_distribution_95_per_cent_gerund_1 = []
for i in xi_gerund_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_gerund_1 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_gerund_1:
        absolute_frequencies_distribution_95_per_cent_gerund_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ДІЄПРИСЛІВНИКИ 1: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_gerund_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ДІЄПРИСЛІВНИКИ 1: ", len(absolute_frequencies_distribution_95_per_cent_gerund_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

h_interval_value_gerund_2 = (xi_gerund_2[-2]-xi_gerund_2[0])/5

intervals_gerund_2 = []

interval_1_gerund_2 = []
interval_1_gerund_2.append(xi_gerund_2[0])
boundary_interval_1_gerund_2 = xi_gerund_2[0] + h_interval_value_gerund_2
interval_1_gerund_2.append(boundary_interval_1_gerund_2)
intervals_gerund_2.append(interval_1_gerund_2)

interval_2_gerund_2 = []
interval_2_gerund_2.append(boundary_interval_1_gerund_2)
boundary_interval_2_gerund_2 = boundary_interval_1_gerund_2 + h_interval_value_gerund_2
interval_2_gerund_2.append(boundary_interval_2_gerund_2)
intervals_gerund_2.append(interval_2_gerund_2)

interval_3_gerund_2 = []
interval_3_gerund_2.append(boundary_interval_2_gerund_2)
boundary_interval_3_gerund_2 = boundary_interval_2_gerund_2 + h_interval_value_gerund_2
interval_3_gerund_2.append(boundary_interval_3_gerund_2)
intervals_gerund_2.append(interval_3_gerund_2)

interval_4_gerund_2 = []
interval_4_gerund_2.append(boundary_interval_3_gerund_2)
boundary_interval_4_gerund_2 = boundary_interval_3_gerund_2 + h_interval_value_gerund_2
interval_4_gerund_2.append(boundary_interval_4_gerund_2)
intervals_gerund_2.append(interval_4_gerund_2)

interval_5_gerund_2 = []
interval_5_gerund_2.append(boundary_interval_4_gerund_2)
boundary_interval_5_gerund_2 = boundary_interval_4_gerund_2 + h_interval_value_gerund_2
interval_5_gerund_2.append(boundary_interval_5_gerund_2)
intervals_gerund_2.append(interval_5_gerund_2)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ДІЄПРИСЛІВНИКИ 2: ", intervals_gerund_2)
##########################################################################################################################################

ni_in_intervals_gerund_2 = []
absolute_frequency_values_in_interval_1_gerund_2 = []
absolute_frequency_values_in_interval_2_gerund_2 = []
absolute_frequency_values_in_interval_3_gerund_2 = []
absolute_frequency_values_in_interval_4_gerund_2 = []
absolute_frequency_values_in_interval_5_gerund_2 = []
for i in xi_gerund_2:
    if i < interval_1_gerund_2[-1]:
        absolute_frequency_values_in_interval_1_gerund_2.append(i)
    elif i > interval_2_gerund_2[0] and i < interval_2_gerund_2[-1]:
        absolute_frequency_values_in_interval_2_gerund_2.append(i)
    elif i > interval_3_gerund_2[0] and i < interval_3_gerund_2[-1]:
        absolute_frequency_values_in_interval_3_gerund_2.append(i)
    elif i > interval_4_gerund_2[0] and i < interval_4_gerund_2[-1]:
        absolute_frequency_values_in_interval_4_gerund_2.append(i)
    elif i > interval_5_gerund_2[0]:
        absolute_frequency_values_in_interval_5_gerund_2.append(i)
ni_in_intervals_gerund_2.append(len(absolute_frequency_values_in_interval_1_gerund_2))
ni_in_intervals_gerund_2.append(len(absolute_frequency_values_in_interval_2_gerund_2))
ni_in_intervals_gerund_2.append(len(absolute_frequency_values_in_interval_3_gerund_2))
ni_in_intervals_gerund_2.append(len(absolute_frequency_values_in_interval_4_gerund_2))
ni_in_intervals_gerund_2.append(len(absolute_frequency_values_in_interval_5_gerund_2))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ДІЄСПРИСЛІВНИКИ 2: ", ni_in_intervals_gerund_2)
##########################################################################################################################################

mediums_intervals_gerund_2 = []

medium_1_intervals_gerund_2 = []
for item in interval_1_gerund_2:
    middlepoint_1_gerund_2 = (interval_1_gerund_2[0] + interval_1_gerund_2[-1]) / 2
medium_1_intervals_gerund_2.append(middlepoint_1_gerund_2)
mediums_intervals_gerund_2.append(medium_1_intervals_gerund_2)

medium_2_intervals_gerund_2 = []
for item in interval_2_gerund_2:
    middlepoint_2_gerund_2 = (interval_2_gerund_2[0] + interval_2_gerund_2[-1]) / 2
medium_2_intervals_gerund_2.append(middlepoint_2_gerund_2)
mediums_intervals_gerund_2.append(medium_2_intervals_gerund_2)

medium_3_intervals_gerund_2 = []
for item in interval_3_gerund_2:
    middlepoint_3_gerund_2 = (interval_3_gerund_2[0] + interval_3_gerund_2[-1]) / 2
medium_3_intervals_gerund_2.append(middlepoint_3_gerund_2)
mediums_intervals_gerund_2.append(medium_3_intervals_gerund_2)

medium_4_intervals_gerund_2 = []
for item in interval_4_gerund_2:
    middlepoint_4_gerund_2 = (interval_4_gerund_2[0] + interval_4_gerund_2[-1]) / 2
medium_4_intervals_gerund_2.append(middlepoint_4_gerund_2)
mediums_intervals_gerund_2.append(medium_4_intervals_gerund_2)

medium_5_intervals_gerund_2 = []
for item in interval_5_gerund_2:
    middlepoint_5_gerund_2 = (interval_5_gerund_2[0] + interval_5_gerund_2[-1]) / 2
medium_5_intervals_gerund_2.append(middlepoint_5_gerund_2)
mediums_intervals_gerund_2.append(medium_5_intervals_gerund_2)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ДІЄПРИСЛІВНИКИ 2: ", mediums_intervals_gerund_2)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_2_gerund_2 = (medium_2_intervals_gerund_2[0] - medium_x_gerund_2)**2*ni_in_intervals_gerund_2[0]
xi_minus_medium_x_power_two_multiply_ni_2_gerund_2 = (medium_2_intervals_gerund_2[0] - medium_x_gerund_2)**2*ni_in_intervals_gerund_2[2]
xi_minus_medium_x_power_two_multiply_ni_3_gerund_2 = (medium_3_intervals_gerund_2[0] - medium_x_gerund_2)**2*ni_in_intervals_gerund_2[2]
xi_minus_medium_x_power_two_multiply_ni_4_gerund_2 = (medium_4_intervals_gerund_2[0] - medium_x_gerund_2)**2*ni_in_intervals_gerund_2[3]
xi_minus_medium_x_power_two_multiply_ni_5_gerund_2 = (medium_5_intervals_gerund_2[0] - medium_x_gerund_2)**2*ni_in_intervals_gerund_2[4]
sum_xi_minus_medium_x_power_two_multiply_ni_gerund_2 = (xi_minus_medium_x_power_two_multiply_ni_2_gerund_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_2_gerund_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_3_gerund_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_4_gerund_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_5_gerund_2)
standard_deviation_for_intervals_gerund_2 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_gerund_2/sum(ni_in_intervals_gerund_2))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_gerund_2)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_gerund_2 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_gerund_2 = medium_x_gerund_2 - standard_deviation_for_intervals_gerund_2
boundary_2_for_absolute_frequencies_distribution_68_per_cent_gerund_2 = medium_x_gerund_2 + standard_deviation_for_intervals_gerund_2
boundaries_for_absolute_frequencies_distribution_68_per_cent_gerund_2.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_gerund_2)
boundaries_for_absolute_frequencies_distribution_68_per_cent_gerund_2.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_gerund_2)
absolute_frequencies_distribution_68_per_cent_gerund_2 = []
for i in xi_gerund_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_gerund_2 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_gerund_2:
        absolute_frequencies_distribution_68_per_cent_gerund_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ДІЄПРИСЛІВНИКИ 2: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_gerund_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ДІЄПРИСЛІВНИКИ 2: ", len(absolute_frequencies_distribution_68_per_cent_gerund_2))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_gerund_2 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_gerund_2 = medium_x_gerund_2 - 2*standard_deviation_for_intervals_gerund_2
boundary_2_for_absolute_frequencies_distribution_95_per_cent_gerund_2 = medium_x_gerund_2 + 2*standard_deviation_for_intervals_gerund_2
boundaries_for_absolute_frequencies_distribution_95_per_cent_gerund_2.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_gerund_2)
boundaries_for_absolute_frequencies_distribution_95_per_cent_gerund_2.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_gerund_2)
absolute_frequencies_distribution_95_per_cent_gerund_2 = []
for i in xi_gerund_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_gerund_2 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_gerund_2:
        absolute_frequencies_distribution_95_per_cent_gerund_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ДІЄПРИСЛІВНИКИ 2: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_gerund_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ДІЄПРИСЛІВНИКИ 2: ", len(absolute_frequencies_distribution_95_per_cent_gerund_2))
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

h_interval_value_numeral_1 = (xi_numeral_1[-1]-xi_numeral_1[0])/5

intervals_numeral_1 = []

interval_1_numeral_1 = []
interval_1_numeral_1.append(xi_numeral_1[0])
boundary_interval_1_numeral_1 = xi_numeral_1[0] + h_interval_value_numeral_1
interval_1_numeral_1.append(boundary_interval_1_numeral_1)
intervals_numeral_1.append(interval_1_numeral_1)

interval_2_numeral_1 = []
interval_2_numeral_1.append(boundary_interval_1_numeral_1)
boundary_interval_2_numeral_1 = boundary_interval_1_numeral_1 + h_interval_value_numeral_1
interval_2_numeral_1.append(boundary_interval_2_numeral_1)
intervals_numeral_1.append(interval_2_numeral_1)

interval_3_numeral_1 = []
interval_3_numeral_1.append(boundary_interval_2_numeral_1)
boundary_interval_3_numeral_1 = boundary_interval_2_numeral_1 + h_interval_value_numeral_1
interval_3_numeral_1.append(boundary_interval_3_numeral_1)
intervals_numeral_1.append(interval_3_numeral_1)

interval_4_numeral_1 = []
interval_4_numeral_1.append(boundary_interval_3_numeral_1)
boundary_interval_4_numeral_1 = boundary_interval_3_numeral_1 + h_interval_value_numeral_1
interval_4_numeral_1.append(boundary_interval_4_numeral_1)
intervals_numeral_1.append(interval_4_numeral_1)

interval_5_numeral_1 = []
interval_5_numeral_1.append(boundary_interval_4_numeral_1)
boundary_interval_5_numeral_1 = boundary_interval_4_numeral_1 + h_interval_value_numeral_1
interval_5_numeral_1.append(boundary_interval_5_numeral_1)
intervals_numeral_1.append(interval_5_numeral_1)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ЧИСЛІВНИКИ 1: ", intervals_numeral_1)
##########################################################################################################################################

ni_in_intervals_numeral_1 = []
absolute_frequency_values_in_interval_1_numeral_1 = []
absolute_frequency_values_in_interval_2_numeral_1 = []
absolute_frequency_values_in_interval_3_numeral_1 = []
absolute_frequency_values_in_interval_4_numeral_1 = []
absolute_frequency_values_in_interval_5_numeral_1 = []
for i in xi_numeral_1:
    if i < interval_1_numeral_1[-1]:
        absolute_frequency_values_in_interval_1_numeral_1.append(i)
    elif i > interval_2_numeral_1[0] and i < interval_2_numeral_1[-1]:
        absolute_frequency_values_in_interval_2_numeral_1.append(i)
    elif i > interval_3_numeral_1[0] and i < interval_3_numeral_1[-1]:
        absolute_frequency_values_in_interval_3_numeral_1.append(i)
    elif i > interval_4_numeral_1[0] and i < interval_4_numeral_1[-1]:
        absolute_frequency_values_in_interval_4_numeral_1.append(i)
    elif i > interval_5_numeral_1[0]:
        absolute_frequency_values_in_interval_5_numeral_1.append(i)
ni_in_intervals_numeral_1.append(len(absolute_frequency_values_in_interval_1_numeral_1))
ni_in_intervals_numeral_1.append(len(absolute_frequency_values_in_interval_2_numeral_1))
ni_in_intervals_numeral_1.append(len(absolute_frequency_values_in_interval_3_numeral_1))
ni_in_intervals_numeral_1.append(len(absolute_frequency_values_in_interval_4_numeral_1))
ni_in_intervals_numeral_1.append(len(absolute_frequency_values_in_interval_5_numeral_1))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ЧИСЛІВНИКИ 1: ", ni_in_intervals_numeral_1)
##########################################################################################################################################

mediums_intervals_numeral_1 = []

medium_1_intervals_numeral_1 = []
for item in interval_1_numeral_1:
    middlepoint_1_numeral_1 = (interval_1_numeral_1[0] + interval_1_numeral_1[-1]) / 2
medium_1_intervals_numeral_1.append(middlepoint_1_numeral_1)
mediums_intervals_numeral_1.append(medium_1_intervals_numeral_1)

medium_2_intervals_numeral_1 = []
for item in interval_2_numeral_1:
    middlepoint_2_numeral_1 = (interval_2_numeral_1[0] + interval_2_numeral_1[-1]) / 2
medium_2_intervals_numeral_1.append(middlepoint_2_numeral_1)
mediums_intervals_numeral_1.append(medium_2_intervals_numeral_1)

medium_3_intervals_numeral_1 = []
for item in interval_3_numeral_1:
    middlepoint_3_numeral_1 = (interval_3_numeral_1[0] + interval_3_numeral_1[-1]) / 2
medium_3_intervals_numeral_1.append(middlepoint_3_numeral_1)
mediums_intervals_numeral_1.append(medium_3_intervals_numeral_1)

medium_4_intervals_numeral_1 = []
for item in interval_4_numeral_1:
    middlepoint_4_numeral_1 = (interval_4_numeral_1[0] + interval_4_numeral_1[-1]) / 2
medium_4_intervals_numeral_1.append(middlepoint_4_numeral_1)
mediums_intervals_numeral_1.append(medium_4_intervals_numeral_1)

medium_5_intervals_numeral_1 = []
for item in interval_5_numeral_1:
    middlepoint_5_numeral_1 = (interval_5_numeral_1[0] + interval_5_numeral_1[-1]) / 2
medium_5_intervals_numeral_1.append(middlepoint_5_numeral_1)
mediums_intervals_numeral_1.append(medium_5_intervals_numeral_1)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ЧИСЛІВНИКИ 1: ", mediums_intervals_numeral_1)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_1_numeral_1 = (medium_1_intervals_numeral_1[0] - medium_x_numeral_1)**2*ni_in_intervals_numeral_1[0]
xi_minus_medium_x_power_two_multiply_ni_2_numeral_1 = (medium_2_intervals_numeral_1[0] - medium_x_numeral_1)**2*ni_in_intervals_numeral_1[1]
xi_minus_medium_x_power_two_multiply_ni_3_numeral_1 = (medium_3_intervals_numeral_1[0] - medium_x_numeral_1)**2*ni_in_intervals_numeral_1[2]
xi_minus_medium_x_power_two_multiply_ni_4_numeral_1 = (medium_4_intervals_numeral_1[0] - medium_x_numeral_1)**2*ni_in_intervals_numeral_1[3]
xi_minus_medium_x_power_two_multiply_ni_5_numeral_1 = (medium_5_intervals_numeral_1[0] - medium_x_numeral_1)**2*ni_in_intervals_numeral_1[4]
sum_xi_minus_medium_x_power_two_multiply_ni_numeral_1 = (xi_minus_medium_x_power_two_multiply_ni_1_numeral_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_2_numeral_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_3_numeral_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_4_numeral_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_5_numeral_1)
standard_deviation_for_intervals_numeral_1 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_numeral_1/sum(ni_in_intervals_numeral_1))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_numeral_1)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_numeral_1 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_numeral_1 = medium_x_numeral_1 - standard_deviation_for_intervals_numeral_1
boundary_2_for_absolute_frequencies_distribution_68_per_cent_numeral_1 = medium_x_numeral_1 + standard_deviation_for_intervals_numeral_1
boundaries_for_absolute_frequencies_distribution_68_per_cent_numeral_1.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_numeral_1)
boundaries_for_absolute_frequencies_distribution_68_per_cent_numeral_1.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_numeral_1)
absolute_frequencies_distribution_68_per_cent_numeral_1 = []
for i in xi_numeral_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_numeral_1 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_numeral_1:
        absolute_frequencies_distribution_68_per_cent_numeral_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ЧИСЛІВНИКИ 1: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_numeral_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ЧИСЛІВНИКИ 1: ", len(absolute_frequencies_distribution_68_per_cent_numeral_1))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_numeral_1 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_numeral_1 = medium_x_numeral_1 - 2*standard_deviation_for_intervals_numeral_1
boundary_2_for_absolute_frequencies_distribution_95_per_cent_numeral_1 = medium_x_numeral_1 + 2*standard_deviation_for_intervals_numeral_1
boundaries_for_absolute_frequencies_distribution_95_per_cent_numeral_1.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_numeral_1)
boundaries_for_absolute_frequencies_distribution_95_per_cent_numeral_1.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_numeral_1)
absolute_frequencies_distribution_95_per_cent_numeral_1 = []
for i in xi_numeral_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_numeral_1 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_numeral_1:
        absolute_frequencies_distribution_95_per_cent_numeral_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ЧИСЛІВНИКИ 1: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_numeral_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ЧИСЛІВНИКИ 1: ", len(absolute_frequencies_distribution_95_per_cent_numeral_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

h_interval_value_numeral_2 = (xi_numeral_2[-2]-xi_numeral_2[0])/5

intervals_numeral_2 = []

interval_1_numeral_2 = []
interval_1_numeral_2.append(xi_numeral_2[0])
boundary_interval_1_numeral_2 = xi_numeral_2[0] + h_interval_value_numeral_2
interval_1_numeral_2.append(boundary_interval_1_numeral_2)
intervals_numeral_2.append(interval_1_numeral_2)

interval_2_numeral_2 = []
interval_2_numeral_2.append(boundary_interval_1_numeral_2)
boundary_interval_2_numeral_2 = boundary_interval_1_numeral_2 + h_interval_value_numeral_2
interval_2_numeral_2.append(boundary_interval_2_numeral_2)
intervals_numeral_2.append(interval_2_numeral_2)

interval_3_numeral_2 = []
interval_3_numeral_2.append(boundary_interval_2_numeral_2)
boundary_interval_3_numeral_2 = boundary_interval_2_numeral_2 + h_interval_value_numeral_2
interval_3_numeral_2.append(boundary_interval_3_numeral_2)
intervals_numeral_2.append(interval_3_numeral_2)

interval_4_numeral_2 = []
interval_4_numeral_2.append(boundary_interval_3_numeral_2)
boundary_interval_4_numeral_2 = boundary_interval_3_numeral_2 + h_interval_value_numeral_2
interval_4_numeral_2.append(boundary_interval_4_numeral_2)
intervals_numeral_2.append(interval_4_numeral_2)

interval_5_numeral_2 = []
interval_5_numeral_2.append(boundary_interval_4_numeral_2)
boundary_interval_5_numeral_2 = boundary_interval_4_numeral_2 + h_interval_value_numeral_2
interval_5_numeral_2.append(boundary_interval_5_numeral_2)
intervals_numeral_2.append(interval_5_numeral_2)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ЧИСЛІВНИКИ 2: ", intervals_numeral_2)
##########################################################################################################################################

ni_in_intervals_numeral_2 = []
absolute_frequency_values_in_interval_1_numeral_2 = []
absolute_frequency_values_in_interval_2_numeral_2 = []
absolute_frequency_values_in_interval_3_numeral_2 = []
absolute_frequency_values_in_interval_4_numeral_2 = []
absolute_frequency_values_in_interval_5_numeral_2 = []
for i in xi_numeral_2:
    if i < interval_1_numeral_2[-1]:
        absolute_frequency_values_in_interval_1_numeral_2.append(i)
    elif i > interval_2_numeral_2[0] and i < interval_2_numeral_2[-1]:
        absolute_frequency_values_in_interval_2_numeral_2.append(i)
    elif i > interval_3_numeral_2[0] and i < interval_3_numeral_2[-1]:
        absolute_frequency_values_in_interval_3_numeral_2.append(i)
    elif i > interval_4_numeral_2[0] and i < interval_4_numeral_2[-1]:
        absolute_frequency_values_in_interval_4_numeral_2.append(i)
    elif i > interval_5_numeral_2[0]:
        absolute_frequency_values_in_interval_5_numeral_2.append(i)
ni_in_intervals_numeral_2.append(len(absolute_frequency_values_in_interval_1_numeral_2))
ni_in_intervals_numeral_2.append(len(absolute_frequency_values_in_interval_2_numeral_2))
ni_in_intervals_numeral_2.append(len(absolute_frequency_values_in_interval_3_numeral_2))
ni_in_intervals_numeral_2.append(len(absolute_frequency_values_in_interval_4_numeral_2))
ni_in_intervals_numeral_2.append(len(absolute_frequency_values_in_interval_5_numeral_2))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ЧИСЛІВНИКИ 2: ", ni_in_intervals_numeral_2)
##########################################################################################################################################

mediums_intervals_numeral_2 = []

medium_1_intervals_numeral_2 = []
for item in interval_1_numeral_2:
    middlepoint_1_numeral_2 = (interval_1_numeral_2[0] + interval_1_numeral_2[-1]) / 2
medium_1_intervals_numeral_2.append(middlepoint_1_numeral_2)
mediums_intervals_numeral_2.append(medium_1_intervals_numeral_2)

medium_2_intervals_numeral_2 = []
for item in interval_2_numeral_2:
    middlepoint_2_numeral_2 = (interval_2_numeral_2[0] + interval_2_numeral_2[-1]) / 2
medium_2_intervals_numeral_2.append(middlepoint_2_numeral_2)
mediums_intervals_numeral_2.append(medium_2_intervals_numeral_2)

medium_3_intervals_numeral_2 = []
for item in interval_3_numeral_2:
    middlepoint_3_numeral_2 = (interval_3_numeral_2[0] + interval_3_numeral_2[-1]) / 2
medium_3_intervals_numeral_2.append(middlepoint_3_numeral_2)
mediums_intervals_numeral_2.append(medium_3_intervals_numeral_2)

medium_4_intervals_numeral_2 = []
for item in interval_4_numeral_2:
    middlepoint_4_numeral_2 = (interval_4_numeral_2[0] + interval_4_numeral_2[-1]) / 2
medium_4_intervals_numeral_2.append(middlepoint_4_numeral_2)
mediums_intervals_numeral_2.append(medium_4_intervals_numeral_2)

medium_5_intervals_numeral_2 = []
for item in interval_5_numeral_2:
    middlepoint_5_numeral_2 = (interval_5_numeral_2[0] + interval_5_numeral_2[-1]) / 2
medium_5_intervals_numeral_2.append(middlepoint_5_numeral_2)
mediums_intervals_numeral_2.append(medium_5_intervals_numeral_2)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ЧИСЛІВНИКИ 2: ", mediums_intervals_numeral_2)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_2_numeral_2 = (medium_2_intervals_numeral_2[0] - medium_x_numeral_2)**2*ni_in_intervals_numeral_2[0]
xi_minus_medium_x_power_two_multiply_ni_2_numeral_2 = (medium_2_intervals_numeral_2[0] - medium_x_numeral_2)**2*ni_in_intervals_numeral_2[2]
xi_minus_medium_x_power_two_multiply_ni_3_numeral_2 = (medium_3_intervals_numeral_2[0] - medium_x_numeral_2)**2*ni_in_intervals_numeral_2[2]
xi_minus_medium_x_power_two_multiply_ni_4_numeral_2 = (medium_4_intervals_numeral_2[0] - medium_x_numeral_2)**2*ni_in_intervals_numeral_2[3]
xi_minus_medium_x_power_two_multiply_ni_5_numeral_2 = (medium_5_intervals_numeral_2[0] - medium_x_numeral_2)**2*ni_in_intervals_numeral_2[4]
sum_xi_minus_medium_x_power_two_multiply_ni_numeral_2 = (xi_minus_medium_x_power_two_multiply_ni_2_numeral_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_2_numeral_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_3_numeral_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_4_numeral_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_5_numeral_2)
standard_deviation_for_intervals_numeral_2 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_numeral_2/sum(ni_in_intervals_numeral_2))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_numeral_2)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_numeral_2 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_numeral_2 = medium_x_numeral_2 - standard_deviation_for_intervals_numeral_2
boundary_2_for_absolute_frequencies_distribution_68_per_cent_numeral_2 = medium_x_numeral_2 + standard_deviation_for_intervals_numeral_2
boundaries_for_absolute_frequencies_distribution_68_per_cent_numeral_2.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_numeral_2)
boundaries_for_absolute_frequencies_distribution_68_per_cent_numeral_2.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_numeral_2)
absolute_frequencies_distribution_68_per_cent_numeral_2 = []
for i in xi_numeral_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_numeral_2 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_numeral_2:
        absolute_frequencies_distribution_68_per_cent_numeral_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ЧИСЛІВНИКИ 2: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_numeral_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ЧИСЛІВНИКИ 2: ", len(absolute_frequencies_distribution_68_per_cent_numeral_2))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_numeral_2 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_numeral_2 = medium_x_numeral_2 - 2*standard_deviation_for_intervals_numeral_2
boundary_2_for_absolute_frequencies_distribution_95_per_cent_numeral_2 = medium_x_numeral_2 + 2*standard_deviation_for_intervals_numeral_2
boundaries_for_absolute_frequencies_distribution_95_per_cent_numeral_2.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_numeral_2)
boundaries_for_absolute_frequencies_distribution_95_per_cent_numeral_2.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_numeral_2)
absolute_frequencies_distribution_95_per_cent_numeral_2 = []
for i in xi_numeral_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_numeral_2 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_numeral_2:
        absolute_frequencies_distribution_95_per_cent_numeral_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ЧИСЛІВНИКИ 2: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_numeral_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ЧИСЛІВНИКИ 2: ", len(absolute_frequencies_distribution_95_per_cent_numeral_2))
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

h_interval_value_adverb_1 = (xi_adverb_1[-1]-xi_adverb_1[0])/5

intervals_adverb_1 = []

interval_1_adverb_1 = []
interval_1_adverb_1.append(xi_adverb_1[0])
boundary_interval_1_adverb_1 = xi_adverb_1[0] + h_interval_value_adverb_1
interval_1_adverb_1.append(boundary_interval_1_adverb_1)
intervals_adverb_1.append(interval_1_adverb_1)

interval_2_adverb_1 = []
interval_2_adverb_1.append(boundary_interval_1_adverb_1)
boundary_interval_2_adverb_1 = boundary_interval_1_adverb_1 + h_interval_value_adverb_1
interval_2_adverb_1.append(boundary_interval_2_adverb_1)
intervals_adverb_1.append(interval_2_adverb_1)

interval_3_adverb_1 = []
interval_3_adverb_1.append(boundary_interval_2_adverb_1)
boundary_interval_3_adverb_1 = boundary_interval_2_adverb_1 + h_interval_value_adverb_1
interval_3_adverb_1.append(boundary_interval_3_adverb_1)
intervals_adverb_1.append(interval_3_adverb_1)

interval_4_adverb_1 = []
interval_4_adverb_1.append(boundary_interval_3_adverb_1)
boundary_interval_4_adverb_1 = boundary_interval_3_adverb_1 + h_interval_value_adverb_1
interval_4_adverb_1.append(boundary_interval_4_adverb_1)
intervals_adverb_1.append(interval_4_adverb_1)

interval_5_adverb_1 = []
interval_5_adverb_1.append(boundary_interval_4_adverb_1)
boundary_interval_5_adverb_1 = boundary_interval_4_adverb_1 + h_interval_value_adverb_1
interval_5_adverb_1.append(boundary_interval_5_adverb_1)
intervals_adverb_1.append(interval_5_adverb_1)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ПРИСЛІВНИКИ 1: ", intervals_adverb_1)
##########################################################################################################################################

ni_in_intervals_adverb_1 = []
absolute_frequency_values_in_interval_1_adverb_1 = []
absolute_frequency_values_in_interval_2_adverb_1 = []
absolute_frequency_values_in_interval_3_adverb_1 = []
absolute_frequency_values_in_interval_4_adverb_1 = []
absolute_frequency_values_in_interval_5_adverb_1 = []
for i in xi_adverb_1:
    if i < interval_1_adverb_1[-1]:
        absolute_frequency_values_in_interval_1_adverb_1.append(i)
    elif i > interval_2_adverb_1[0] and i < interval_2_adverb_1[-1]:
        absolute_frequency_values_in_interval_2_adverb_1.append(i)
    elif i > interval_3_adverb_1[0] and i < interval_3_adverb_1[-1]:
        absolute_frequency_values_in_interval_3_adverb_1.append(i)
    elif i > interval_4_adverb_1[0] and i < interval_4_adverb_1[-1]:
        absolute_frequency_values_in_interval_4_adverb_1.append(i)
    elif i > interval_5_adverb_1[0]:
        absolute_frequency_values_in_interval_5_adverb_1.append(i)
ni_in_intervals_adverb_1.append(len(absolute_frequency_values_in_interval_1_adverb_1))
ni_in_intervals_adverb_1.append(len(absolute_frequency_values_in_interval_2_adverb_1))
ni_in_intervals_adverb_1.append(len(absolute_frequency_values_in_interval_3_adverb_1))
ni_in_intervals_adverb_1.append(len(absolute_frequency_values_in_interval_4_adverb_1))
ni_in_intervals_adverb_1.append(len(absolute_frequency_values_in_interval_5_adverb_1))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ПРИСЛІВНИКИ 1: ", ni_in_intervals_adverb_1)
##########################################################################################################################################

mediums_intervals_adverb_1 = []

medium_1_intervals_adverb_1 = []
for item in interval_1_adverb_1:
    middlepoint_1_adverb_1 = (interval_1_adverb_1[0] + interval_1_adverb_1[-1]) / 2
medium_1_intervals_adverb_1.append(middlepoint_1_adverb_1)
mediums_intervals_adverb_1.append(medium_1_intervals_adverb_1)

medium_2_intervals_adverb_1 = []
for item in interval_2_adverb_1:
    middlepoint_2_adverb_1 = (interval_2_adverb_1[0] + interval_2_adverb_1[-1]) / 2
medium_2_intervals_adverb_1.append(middlepoint_2_adverb_1)
mediums_intervals_adverb_1.append(medium_2_intervals_adverb_1)

medium_3_intervals_adverb_1 = []
for item in interval_3_adverb_1:
    middlepoint_3_adverb_1 = (interval_3_adverb_1[0] + interval_3_adverb_1[-1]) / 2
medium_3_intervals_adverb_1.append(middlepoint_3_adverb_1)
mediums_intervals_adverb_1.append(medium_3_intervals_adverb_1)

medium_4_intervals_adverb_1 = []
for item in interval_4_adverb_1:
    middlepoint_4_adverb_1 = (interval_4_adverb_1[0] + interval_4_adverb_1[-1]) / 2
medium_4_intervals_adverb_1.append(middlepoint_4_adverb_1)
mediums_intervals_adverb_1.append(medium_4_intervals_adverb_1)

medium_5_intervals_adverb_1 = []
for item in interval_5_adverb_1:
    middlepoint_5_adverb_1 = (interval_5_adverb_1[0] + interval_5_adverb_1[-1]) / 2
medium_5_intervals_adverb_1.append(middlepoint_5_adverb_1)
mediums_intervals_adverb_1.append(medium_5_intervals_adverb_1)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ПРИСЛІВНИКИ 1: ", mediums_intervals_adverb_1)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_1_adverb_1 = (medium_1_intervals_adverb_1[0] - medium_x_adverb_1)**2*ni_in_intervals_adverb_1[0]
xi_minus_medium_x_power_two_multiply_ni_2_adverb_1 = (medium_2_intervals_adverb_1[0] - medium_x_adverb_1)**2*ni_in_intervals_adverb_1[1]
xi_minus_medium_x_power_two_multiply_ni_3_adverb_1 = (medium_3_intervals_adverb_1[0] - medium_x_adverb_1)**2*ni_in_intervals_adverb_1[2]
xi_minus_medium_x_power_two_multiply_ni_4_adverb_1 = (medium_4_intervals_adverb_1[0] - medium_x_adverb_1)**2*ni_in_intervals_adverb_1[3]
xi_minus_medium_x_power_two_multiply_ni_5_adverb_1 = (medium_5_intervals_adverb_1[0] - medium_x_adverb_1)**2*ni_in_intervals_adverb_1[4]
sum_xi_minus_medium_x_power_two_multiply_ni_adverb_1 = (xi_minus_medium_x_power_two_multiply_ni_1_adverb_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_2_adverb_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_3_adverb_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_4_adverb_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_5_adverb_1)
standard_deviation_for_intervals_adverb_1 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_adverb_1/sum(ni_in_intervals_adverb_1))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_adverb_1)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_adverb_1 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_adverb_1 = medium_x_adverb_1 - standard_deviation_for_intervals_adverb_1
boundary_2_for_absolute_frequencies_distribution_68_per_cent_adverb_1 = medium_x_adverb_1 + standard_deviation_for_intervals_adverb_1
boundaries_for_absolute_frequencies_distribution_68_per_cent_adverb_1.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_adverb_1)
boundaries_for_absolute_frequencies_distribution_68_per_cent_adverb_1.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_adverb_1)
absolute_frequencies_distribution_68_per_cent_adverb_1 = []
for i in xi_adverb_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_adverb_1 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_adverb_1:
        absolute_frequencies_distribution_68_per_cent_adverb_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ПРИСЛІВНИКИ 1: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_adverb_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ПРИСЛІВНИКИ 1: ", len(absolute_frequencies_distribution_68_per_cent_adverb_1))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_adverb_1 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_adverb_1 = medium_x_adverb_1 - 2*standard_deviation_for_intervals_adverb_1
boundary_2_for_absolute_frequencies_distribution_95_per_cent_adverb_1 = medium_x_adverb_1 + 2*standard_deviation_for_intervals_adverb_1
boundaries_for_absolute_frequencies_distribution_95_per_cent_adverb_1.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_adverb_1)
boundaries_for_absolute_frequencies_distribution_95_per_cent_adverb_1.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_adverb_1)
absolute_frequencies_distribution_95_per_cent_adverb_1 = []
for i in xi_adverb_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_adverb_1 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_adverb_1:
        absolute_frequencies_distribution_95_per_cent_adverb_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ПРИСЛІВНИКИ 1: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_adverb_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ПРИСЛІВНИКИ 1: ", len(absolute_frequencies_distribution_95_per_cent_adverb_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

h_interval_value_adverb_2 = (xi_adverb_2[-2]-xi_adverb_2[0])/5

intervals_adverb_2 = []

interval_1_adverb_2 = []
interval_1_adverb_2.append(xi_adverb_2[0])
boundary_interval_1_adverb_2 = xi_adverb_2[0] + h_interval_value_adverb_2
interval_1_adverb_2.append(boundary_interval_1_adverb_2)
intervals_adverb_2.append(interval_1_adverb_2)

interval_2_adverb_2 = []
interval_2_adverb_2.append(boundary_interval_1_adverb_2)
boundary_interval_2_adverb_2 = boundary_interval_1_adverb_2 + h_interval_value_adverb_2
interval_2_adverb_2.append(boundary_interval_2_adverb_2)
intervals_adverb_2.append(interval_2_adverb_2)

interval_3_adverb_2 = []
interval_3_adverb_2.append(boundary_interval_2_adverb_2)
boundary_interval_3_adverb_2 = boundary_interval_2_adverb_2 + h_interval_value_adverb_2
interval_3_adverb_2.append(boundary_interval_3_adverb_2)
intervals_adverb_2.append(interval_3_adverb_2)

interval_4_adverb_2 = []
interval_4_adverb_2.append(boundary_interval_3_adverb_2)
boundary_interval_4_adverb_2 = boundary_interval_3_adverb_2 + h_interval_value_adverb_2
interval_4_adverb_2.append(boundary_interval_4_adverb_2)
intervals_adverb_2.append(interval_4_adverb_2)

interval_5_adverb_2 = []
interval_5_adverb_2.append(boundary_interval_4_adverb_2)
boundary_interval_5_adverb_2 = boundary_interval_4_adverb_2 + h_interval_value_adverb_2
interval_5_adverb_2.append(boundary_interval_5_adverb_2)
intervals_adverb_2.append(interval_5_adverb_2)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ПРИСЛІВНИКИ 2: ", intervals_adverb_2)
##########################################################################################################################################

ni_in_intervals_adverb_2 = []
absolute_frequency_values_in_interval_1_adverb_2 = []
absolute_frequency_values_in_interval_2_adverb_2 = []
absolute_frequency_values_in_interval_3_adverb_2 = []
absolute_frequency_values_in_interval_4_adverb_2 = []
absolute_frequency_values_in_interval_5_adverb_2 = []
for i in xi_adverb_2:
    if i < interval_1_adverb_2[-1]:
        absolute_frequency_values_in_interval_1_adverb_2.append(i)
    elif i > interval_2_adverb_2[0] and i < interval_2_adverb_2[-1]:
        absolute_frequency_values_in_interval_2_adverb_2.append(i)
    elif i > interval_3_adverb_2[0] and i < interval_3_adverb_2[-1]:
        absolute_frequency_values_in_interval_3_adverb_2.append(i)
    elif i > interval_4_adverb_2[0] and i < interval_4_adverb_2[-1]:
        absolute_frequency_values_in_interval_4_adverb_2.append(i)
    elif i > interval_5_adverb_2[0]:
        absolute_frequency_values_in_interval_5_adverb_2.append(i)
ni_in_intervals_adverb_2.append(len(absolute_frequency_values_in_interval_1_adverb_2))
ni_in_intervals_adverb_2.append(len(absolute_frequency_values_in_interval_2_adverb_2))
ni_in_intervals_adverb_2.append(len(absolute_frequency_values_in_interval_3_adverb_2))
ni_in_intervals_adverb_2.append(len(absolute_frequency_values_in_interval_4_adverb_2))
ni_in_intervals_adverb_2.append(len(absolute_frequency_values_in_interval_5_adverb_2))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ПРИСЛІВНИКИ 2: ", ni_in_intervals_adverb_2)
##########################################################################################################################################

mediums_intervals_adverb_2 = []

medium_1_intervals_adverb_2 = []
for item in interval_1_adverb_2:
    middlepoint_1_adverb_2 = (interval_1_adverb_2[0] + interval_1_adverb_2[-1]) / 2
medium_1_intervals_adverb_2.append(middlepoint_1_adverb_2)
mediums_intervals_adverb_2.append(medium_1_intervals_adverb_2)

medium_2_intervals_adverb_2 = []
for item in interval_2_adverb_2:
    middlepoint_2_adverb_2 = (interval_2_adverb_2[0] + interval_2_adverb_2[-1]) / 2
medium_2_intervals_adverb_2.append(middlepoint_2_adverb_2)
mediums_intervals_adverb_2.append(medium_2_intervals_adverb_2)

medium_3_intervals_adverb_2 = []
for item in interval_3_adverb_2:
    middlepoint_3_adverb_2 = (interval_3_adverb_2[0] + interval_3_adverb_2[-1]) / 2
medium_3_intervals_adverb_2.append(middlepoint_3_adverb_2)
mediums_intervals_adverb_2.append(medium_3_intervals_adverb_2)

medium_4_intervals_adverb_2 = []
for item in interval_4_adverb_2:
    middlepoint_4_adverb_2 = (interval_4_adverb_2[0] + interval_4_adverb_2[-1]) / 2
medium_4_intervals_adverb_2.append(middlepoint_4_adverb_2)
mediums_intervals_adverb_2.append(medium_4_intervals_adverb_2)

medium_5_intervals_adverb_2 = []
for item in interval_5_adverb_2:
    middlepoint_5_adverb_2 = (interval_5_adverb_2[0] + interval_5_adverb_2[-1]) / 2
medium_5_intervals_adverb_2.append(middlepoint_5_adverb_2)
mediums_intervals_adverb_2.append(medium_5_intervals_adverb_2)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ПРИСЛІВНИКИ 2: ", mediums_intervals_adverb_2)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_2_adverb_2 = (medium_2_intervals_adverb_2[0] - medium_x_adverb_2)**2*ni_in_intervals_adverb_2[0]
xi_minus_medium_x_power_two_multiply_ni_2_adverb_2 = (medium_2_intervals_adverb_2[0] - medium_x_adverb_2)**2*ni_in_intervals_adverb_2[2]
xi_minus_medium_x_power_two_multiply_ni_3_adverb_2 = (medium_3_intervals_adverb_2[0] - medium_x_adverb_2)**2*ni_in_intervals_adverb_2[2]
xi_minus_medium_x_power_two_multiply_ni_4_adverb_2 = (medium_4_intervals_adverb_2[0] - medium_x_adverb_2)**2*ni_in_intervals_adverb_2[3]
xi_minus_medium_x_power_two_multiply_ni_5_adverb_2 = (medium_5_intervals_adverb_2[0] - medium_x_adverb_2)**2*ni_in_intervals_adverb_2[4]
sum_xi_minus_medium_x_power_two_multiply_ni_adverb_2 = (xi_minus_medium_x_power_two_multiply_ni_2_adverb_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_2_adverb_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_3_adverb_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_4_adverb_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_5_adverb_2)
standard_deviation_for_intervals_adverb_2 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_adverb_2/sum(ni_in_intervals_adverb_2))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_adverb_2)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_adverb_2 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_adverb_2 = medium_x_adverb_2 - standard_deviation_for_intervals_adverb_2
boundary_2_for_absolute_frequencies_distribution_68_per_cent_adverb_2 = medium_x_adverb_2 + standard_deviation_for_intervals_adverb_2
boundaries_for_absolute_frequencies_distribution_68_per_cent_adverb_2.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_adverb_2)
boundaries_for_absolute_frequencies_distribution_68_per_cent_adverb_2.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_adverb_2)
absolute_frequencies_distribution_68_per_cent_adverb_2 = []
for i in xi_adverb_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_adverb_2 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_adverb_2:
        absolute_frequencies_distribution_68_per_cent_adverb_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ПРИСЛІВНИКИ 2: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_adverb_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ПРИСЛІВНИКИ 2: ", len(absolute_frequencies_distribution_68_per_cent_adverb_2))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_adverb_2 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_adverb_2 = medium_x_adverb_2 - 2*standard_deviation_for_intervals_adverb_2
boundary_2_for_absolute_frequencies_distribution_95_per_cent_adverb_2 = medium_x_adverb_2 + 2*standard_deviation_for_intervals_adverb_2
boundaries_for_absolute_frequencies_distribution_95_per_cent_adverb_2.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_adverb_2)
boundaries_for_absolute_frequencies_distribution_95_per_cent_adverb_2.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_adverb_2)
absolute_frequencies_distribution_95_per_cent_adverb_2 = []
for i in xi_adverb_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_adverb_2 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_adverb_2:
        absolute_frequencies_distribution_95_per_cent_adverb_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ПРИСЛІВНИКИ 2: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_adverb_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ПРИСЛІВНИКИ 2: ", len(absolute_frequencies_distribution_95_per_cent_adverb_2))
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

h_interval_value_nominative_pronoun_1 = (xi_nominative_pronoun_1[-1]-xi_nominative_pronoun_1[0])/5

intervals_nominative_pronoun_1 = []

interval_1_nominative_pronoun_1 = []
interval_1_nominative_pronoun_1.append(xi_nominative_pronoun_1[0])
boundary_interval_1_nominative_pronoun_1 = xi_nominative_pronoun_1[0] + h_interval_value_nominative_pronoun_1
interval_1_nominative_pronoun_1.append(boundary_interval_1_nominative_pronoun_1)
intervals_nominative_pronoun_1.append(interval_1_nominative_pronoun_1)

interval_2_nominative_pronoun_1 = []
interval_2_nominative_pronoun_1.append(boundary_interval_1_nominative_pronoun_1)
boundary_interval_2_nominative_pronoun_1 = boundary_interval_1_nominative_pronoun_1 + h_interval_value_nominative_pronoun_1
interval_2_nominative_pronoun_1.append(boundary_interval_2_nominative_pronoun_1)
intervals_nominative_pronoun_1.append(interval_2_nominative_pronoun_1)

interval_3_nominative_pronoun_1 = []
interval_3_nominative_pronoun_1.append(boundary_interval_2_nominative_pronoun_1)
boundary_interval_3_nominative_pronoun_1 = boundary_interval_2_nominative_pronoun_1 + h_interval_value_nominative_pronoun_1
interval_3_nominative_pronoun_1.append(boundary_interval_3_nominative_pronoun_1)
intervals_nominative_pronoun_1.append(interval_3_nominative_pronoun_1)

interval_4_nominative_pronoun_1 = []
interval_4_nominative_pronoun_1.append(boundary_interval_3_nominative_pronoun_1)
boundary_interval_4_nominative_pronoun_1 = boundary_interval_3_nominative_pronoun_1 + h_interval_value_nominative_pronoun_1
interval_4_nominative_pronoun_1.append(boundary_interval_4_nominative_pronoun_1)
intervals_nominative_pronoun_1.append(interval_4_nominative_pronoun_1)

interval_5_nominative_pronoun_1 = []
interval_5_nominative_pronoun_1.append(boundary_interval_4_nominative_pronoun_1)
boundary_interval_5_nominative_pronoun_1 = boundary_interval_4_nominative_pronoun_1 + h_interval_value_nominative_pronoun_1
interval_5_nominative_pronoun_1.append(boundary_interval_5_nominative_pronoun_1)
intervals_nominative_pronoun_1.append(interval_5_nominative_pronoun_1)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", intervals_nominative_pronoun_1)
##########################################################################################################################################

ni_in_intervals_nominative_pronoun_1 = []
absolute_frequency_values_in_interval_1_nominative_pronoun_1 = []
absolute_frequency_values_in_interval_2_nominative_pronoun_1 = []
absolute_frequency_values_in_interval_3_nominative_pronoun_1 = []
absolute_frequency_values_in_interval_4_nominative_pronoun_1 = []
absolute_frequency_values_in_interval_5_nominative_pronoun_1 = []
for i in xi_nominative_pronoun_1:
    if i < interval_1_nominative_pronoun_1[-1]:
        absolute_frequency_values_in_interval_1_nominative_pronoun_1.append(i)
    elif i > interval_2_nominative_pronoun_1[0] and i < interval_2_nominative_pronoun_1[-1]:
        absolute_frequency_values_in_interval_2_nominative_pronoun_1.append(i)
    elif i > interval_3_nominative_pronoun_1[0] and i < interval_3_nominative_pronoun_1[-1]:
        absolute_frequency_values_in_interval_3_nominative_pronoun_1.append(i)
    elif i > interval_4_nominative_pronoun_1[0] and i < interval_4_nominative_pronoun_1[-1]:
        absolute_frequency_values_in_interval_4_nominative_pronoun_1.append(i)
    elif i > interval_5_nominative_pronoun_1[0]:
        absolute_frequency_values_in_interval_5_nominative_pronoun_1.append(i)
ni_in_intervals_nominative_pronoun_1.append(len(absolute_frequency_values_in_interval_1_nominative_pronoun_1))
ni_in_intervals_nominative_pronoun_1.append(len(absolute_frequency_values_in_interval_2_nominative_pronoun_1))
ni_in_intervals_nominative_pronoun_1.append(len(absolute_frequency_values_in_interval_3_nominative_pronoun_1))
ni_in_intervals_nominative_pronoun_1.append(len(absolute_frequency_values_in_interval_4_nominative_pronoun_1))
ni_in_intervals_nominative_pronoun_1.append(len(absolute_frequency_values_in_interval_5_nominative_pronoun_1))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", ni_in_intervals_nominative_pronoun_1)
##########################################################################################################################################

mediums_intervals_nominative_pronoun_1 = []

medium_1_intervals_nominative_pronoun_1 = []
for item in interval_1_nominative_pronoun_1:
    middlepoint_1_nominative_pronoun_1 = (interval_1_nominative_pronoun_1[0] + interval_1_nominative_pronoun_1[-1]) / 2
medium_1_intervals_nominative_pronoun_1.append(middlepoint_1_nominative_pronoun_1)
mediums_intervals_nominative_pronoun_1.append(medium_1_intervals_nominative_pronoun_1)

medium_2_intervals_nominative_pronoun_1 = []
for item in interval_2_nominative_pronoun_1:
    middlepoint_2_nominative_pronoun_1 = (interval_2_nominative_pronoun_1[0] + interval_2_nominative_pronoun_1[-1]) / 2
medium_2_intervals_nominative_pronoun_1.append(middlepoint_2_nominative_pronoun_1)
mediums_intervals_nominative_pronoun_1.append(medium_2_intervals_nominative_pronoun_1)

medium_3_intervals_nominative_pronoun_1 = []
for item in interval_3_nominative_pronoun_1:
    middlepoint_3_nominative_pronoun_1 = (interval_3_nominative_pronoun_1[0] + interval_3_nominative_pronoun_1[-1]) / 2
medium_3_intervals_nominative_pronoun_1.append(middlepoint_3_nominative_pronoun_1)
mediums_intervals_nominative_pronoun_1.append(medium_3_intervals_nominative_pronoun_1)

medium_4_intervals_nominative_pronoun_1 = []
for item in interval_4_nominative_pronoun_1:
    middlepoint_4_nominative_pronoun_1 = (interval_4_nominative_pronoun_1[0] + interval_4_nominative_pronoun_1[-1]) / 2
medium_4_intervals_nominative_pronoun_1.append(middlepoint_4_nominative_pronoun_1)
mediums_intervals_nominative_pronoun_1.append(medium_4_intervals_nominative_pronoun_1)

medium_5_intervals_nominative_pronoun_1 = []
for item in interval_5_nominative_pronoun_1:
    middlepoint_5_nominative_pronoun_1 = (interval_5_nominative_pronoun_1[0] + interval_5_nominative_pronoun_1[-1]) / 2
medium_5_intervals_nominative_pronoun_1.append(middlepoint_5_nominative_pronoun_1)
mediums_intervals_nominative_pronoun_1.append(medium_5_intervals_nominative_pronoun_1)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", mediums_intervals_nominative_pronoun_1)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_1_nominative_pronoun_1 = (medium_1_intervals_nominative_pronoun_1[0] - medium_x_nominative_pronoun_1)**2*ni_in_intervals_nominative_pronoun_1[0]
xi_minus_medium_x_power_two_multiply_ni_2_nominative_pronoun_1 = (medium_2_intervals_nominative_pronoun_1[0] - medium_x_nominative_pronoun_1)**2*ni_in_intervals_nominative_pronoun_1[1]
xi_minus_medium_x_power_two_multiply_ni_3_nominative_pronoun_1 = (medium_3_intervals_nominative_pronoun_1[0] - medium_x_nominative_pronoun_1)**2*ni_in_intervals_nominative_pronoun_1[2]
xi_minus_medium_x_power_two_multiply_ni_4_nominative_pronoun_1 = (medium_4_intervals_nominative_pronoun_1[0] - medium_x_nominative_pronoun_1)**2*ni_in_intervals_nominative_pronoun_1[3]
xi_minus_medium_x_power_two_multiply_ni_5_nominative_pronoun_1 = (medium_5_intervals_nominative_pronoun_1[0] - medium_x_nominative_pronoun_1)**2*ni_in_intervals_nominative_pronoun_1[4]
sum_xi_minus_medium_x_power_two_multiply_ni_nominative_pronoun_1 = (xi_minus_medium_x_power_two_multiply_ni_1_nominative_pronoun_1
                                                                    + xi_minus_medium_x_power_two_multiply_ni_2_nominative_pronoun_1
                                                                    + xi_minus_medium_x_power_two_multiply_ni_3_nominative_pronoun_1
                                                                    + xi_minus_medium_x_power_two_multiply_ni_4_nominative_pronoun_1
                                                                    + xi_minus_medium_x_power_two_multiply_ni_5_nominative_pronoun_1)
standard_deviation_for_intervals_nominative_pronoun_1 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_nominative_pronoun_1/sum(ni_in_intervals_nominative_pronoun_1))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_nominative_pronoun_1)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_1 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_1 = medium_x_nominative_pronoun_1 - standard_deviation_for_intervals_nominative_pronoun_1
boundary_2_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_1 = medium_x_nominative_pronoun_1 + standard_deviation_for_intervals_nominative_pronoun_1
boundaries_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_1.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_1)
boundaries_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_1.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_1)
absolute_frequencies_distribution_68_per_cent_nominative_pronoun_1 = []
for i in xi_nominative_pronoun_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_1 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_1:
        absolute_frequencies_distribution_68_per_cent_nominative_pronoun_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", len(absolute_frequencies_distribution_68_per_cent_nominative_pronoun_1))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_1 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_1 = medium_x_nominative_pronoun_1 - 2*standard_deviation_for_intervals_nominative_pronoun_1
boundary_2_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_1 = medium_x_nominative_pronoun_1 + 2*standard_deviation_for_intervals_nominative_pronoun_1
boundaries_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_1.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_1)
boundaries_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_1.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_1)
absolute_frequencies_distribution_95_per_cent_nominative_pronoun_1 = []
for i in xi_nominative_pronoun_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_1 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_1:
        absolute_frequencies_distribution_95_per_cent_nominative_pronoun_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", len(absolute_frequencies_distribution_95_per_cent_nominative_pronoun_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

h_interval_value_nominative_pronoun_2 = (xi_nominative_pronoun_2[-2]-xi_nominative_pronoun_2[0])/5

intervals_nominative_pronoun_2 = []

interval_1_nominative_pronoun_2 = []
interval_1_nominative_pronoun_2.append(xi_nominative_pronoun_2[0])
boundary_interval_1_nominative_pronoun_2 = xi_nominative_pronoun_2[0] + h_interval_value_nominative_pronoun_2
interval_1_nominative_pronoun_2.append(boundary_interval_1_nominative_pronoun_2)
intervals_nominative_pronoun_2.append(interval_1_nominative_pronoun_2)

interval_2_nominative_pronoun_2 = []
interval_2_nominative_pronoun_2.append(boundary_interval_1_nominative_pronoun_2)
boundary_interval_2_nominative_pronoun_2 = boundary_interval_1_nominative_pronoun_2 + h_interval_value_nominative_pronoun_2
interval_2_nominative_pronoun_2.append(boundary_interval_2_nominative_pronoun_2)
intervals_nominative_pronoun_2.append(interval_2_nominative_pronoun_2)

interval_3_nominative_pronoun_2 = []
interval_3_nominative_pronoun_2.append(boundary_interval_2_nominative_pronoun_2)
boundary_interval_3_nominative_pronoun_2 = boundary_interval_2_nominative_pronoun_2 + h_interval_value_nominative_pronoun_2
interval_3_nominative_pronoun_2.append(boundary_interval_3_nominative_pronoun_2)
intervals_nominative_pronoun_2.append(interval_3_nominative_pronoun_2)

interval_4_nominative_pronoun_2 = []
interval_4_nominative_pronoun_2.append(boundary_interval_3_nominative_pronoun_2)
boundary_interval_4_nominative_pronoun_2 = boundary_interval_3_nominative_pronoun_2 + h_interval_value_nominative_pronoun_2
interval_4_nominative_pronoun_2.append(boundary_interval_4_nominative_pronoun_2)
intervals_nominative_pronoun_2.append(interval_4_nominative_pronoun_2)

interval_5_nominative_pronoun_2 = []
interval_5_nominative_pronoun_2.append(boundary_interval_4_nominative_pronoun_2)
boundary_interval_5_nominative_pronoun_2 = boundary_interval_4_nominative_pronoun_2 + h_interval_value_nominative_pronoun_2
interval_5_nominative_pronoun_2.append(boundary_interval_5_nominative_pronoun_2)
intervals_nominative_pronoun_2.append(interval_5_nominative_pronoun_2)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ЗАЙМЕННИКИ-ІМЕННИКИ 2: ", intervals_nominative_pronoun_2)
##########################################################################################################################################

ni_in_intervals_nominative_pronoun_2 = []
absolute_frequency_values_in_interval_1_nominative_pronoun_2 = []
absolute_frequency_values_in_interval_2_nominative_pronoun_2 = []
absolute_frequency_values_in_interval_3_nominative_pronoun_2 = []
absolute_frequency_values_in_interval_4_nominative_pronoun_2 = []
absolute_frequency_values_in_interval_5_nominative_pronoun_2 = []
for i in xi_nominative_pronoun_2:
    if i < interval_1_nominative_pronoun_2[-1]:
        absolute_frequency_values_in_interval_1_nominative_pronoun_2.append(i)
    elif i > interval_2_nominative_pronoun_2[0] and i < interval_2_nominative_pronoun_2[-1]:
        absolute_frequency_values_in_interval_2_nominative_pronoun_2.append(i)
    elif i > interval_3_nominative_pronoun_2[0] and i < interval_3_nominative_pronoun_2[-1]:
        absolute_frequency_values_in_interval_3_nominative_pronoun_2.append(i)
    elif i > interval_4_nominative_pronoun_2[0] and i < interval_4_nominative_pronoun_2[-1]:
        absolute_frequency_values_in_interval_4_nominative_pronoun_2.append(i)
    elif i > interval_5_nominative_pronoun_2[0]:
        absolute_frequency_values_in_interval_5_nominative_pronoun_2.append(i)
ni_in_intervals_nominative_pronoun_2.append(len(absolute_frequency_values_in_interval_1_nominative_pronoun_2))
ni_in_intervals_nominative_pronoun_2.append(len(absolute_frequency_values_in_interval_2_nominative_pronoun_2))
ni_in_intervals_nominative_pronoun_2.append(len(absolute_frequency_values_in_interval_3_nominative_pronoun_2))
ni_in_intervals_nominative_pronoun_2.append(len(absolute_frequency_values_in_interval_4_nominative_pronoun_2))
ni_in_intervals_nominative_pronoun_2.append(len(absolute_frequency_values_in_interval_5_nominative_pronoun_2))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ЗАЙМЕННИКИ-ІМЕННИКИ 2: ", ni_in_intervals_nominative_pronoun_2)
##########################################################################################################################################

mediums_intervals_nominative_pronoun_2 = []

medium_1_intervals_nominative_pronoun_2 = []
for item in interval_1_nominative_pronoun_2:
    middlepoint_1_nominative_pronoun_2 = (interval_1_nominative_pronoun_2[0] + interval_1_nominative_pronoun_2[-1]) / 2
medium_1_intervals_nominative_pronoun_2.append(middlepoint_1_nominative_pronoun_2)
mediums_intervals_nominative_pronoun_2.append(medium_1_intervals_nominative_pronoun_2)

medium_2_intervals_nominative_pronoun_2 = []
for item in interval_2_nominative_pronoun_2:
    middlepoint_2_nominative_pronoun_2 = (interval_2_nominative_pronoun_2[0] + interval_2_nominative_pronoun_2[-1]) / 2
medium_2_intervals_nominative_pronoun_2.append(middlepoint_2_nominative_pronoun_2)
mediums_intervals_nominative_pronoun_2.append(medium_2_intervals_nominative_pronoun_2)

medium_3_intervals_nominative_pronoun_2 = []
for item in interval_3_nominative_pronoun_2:
    middlepoint_3_nominative_pronoun_2 = (interval_3_nominative_pronoun_2[0] + interval_3_nominative_pronoun_2[-1]) / 2
medium_3_intervals_nominative_pronoun_2.append(middlepoint_3_nominative_pronoun_2)
mediums_intervals_nominative_pronoun_2.append(medium_3_intervals_nominative_pronoun_2)

medium_4_intervals_nominative_pronoun_2 = []
for item in interval_4_nominative_pronoun_2:
    middlepoint_4_nominative_pronoun_2 = (interval_4_nominative_pronoun_2[0] + interval_4_nominative_pronoun_2[-1]) / 2
medium_4_intervals_nominative_pronoun_2.append(middlepoint_4_nominative_pronoun_2)
mediums_intervals_nominative_pronoun_2.append(medium_4_intervals_nominative_pronoun_2)

medium_5_intervals_nominative_pronoun_2 = []
for item in interval_5_nominative_pronoun_2:
    middlepoint_5_nominative_pronoun_2 = (interval_5_nominative_pronoun_2[0] + interval_5_nominative_pronoun_2[-1]) / 2
medium_5_intervals_nominative_pronoun_2.append(middlepoint_5_nominative_pronoun_2)
mediums_intervals_nominative_pronoun_2.append(medium_5_intervals_nominative_pronoun_2)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ЗАЙМЕННИКИ-ІМЕННИКИ 2: ", mediums_intervals_nominative_pronoun_2)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_2_nominative_pronoun_2 = (medium_2_intervals_nominative_pronoun_2[0] - medium_x_nominative_pronoun_2)**2*ni_in_intervals_nominative_pronoun_2[0]
xi_minus_medium_x_power_two_multiply_ni_2_nominative_pronoun_2 = (medium_2_intervals_nominative_pronoun_2[0] - medium_x_nominative_pronoun_2)**2*ni_in_intervals_nominative_pronoun_2[2]
xi_minus_medium_x_power_two_multiply_ni_3_nominative_pronoun_2 = (medium_3_intervals_nominative_pronoun_2[0] - medium_x_nominative_pronoun_2)**2*ni_in_intervals_nominative_pronoun_2[2]
xi_minus_medium_x_power_two_multiply_ni_4_nominative_pronoun_2 = (medium_4_intervals_nominative_pronoun_2[0] - medium_x_nominative_pronoun_2)**2*ni_in_intervals_nominative_pronoun_2[3]
xi_minus_medium_x_power_two_multiply_ni_5_nominative_pronoun_2 = (medium_5_intervals_nominative_pronoun_2[0] - medium_x_nominative_pronoun_2)**2*ni_in_intervals_nominative_pronoun_2[4]
sum_xi_minus_medium_x_power_two_multiply_ni_nominative_pronoun_2 = (xi_minus_medium_x_power_two_multiply_ni_2_nominative_pronoun_2
                                                                    + xi_minus_medium_x_power_two_multiply_ni_2_nominative_pronoun_2
                                                                    + xi_minus_medium_x_power_two_multiply_ni_3_nominative_pronoun_2
                                                                    + xi_minus_medium_x_power_two_multiply_ni_4_nominative_pronoun_2
                                                                    + xi_minus_medium_x_power_two_multiply_ni_5_nominative_pronoun_2)
standard_deviation_for_intervals_nominative_pronoun_2 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_nominative_pronoun_2/sum(ni_in_intervals_nominative_pronoun_2))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_nominative_pronoun_2)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_2 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_2 = medium_x_nominative_pronoun_2 - standard_deviation_for_intervals_nominative_pronoun_2
boundary_2_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_2 = medium_x_nominative_pronoun_2 + standard_deviation_for_intervals_nominative_pronoun_2
boundaries_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_2.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_2)
boundaries_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_2.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_2)
absolute_frequencies_distribution_68_per_cent_nominative_pronoun_2 = []
for i in xi_nominative_pronoun_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_2 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_2:
        absolute_frequencies_distribution_68_per_cent_nominative_pronoun_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ЗАЙМЕННИКИ-ІМЕННИКИ 2: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_nominative_pronoun_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ЗАЙМЕННИКИ-ІМЕННИКИ 2: ", len(absolute_frequencies_distribution_68_per_cent_nominative_pronoun_2))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_2 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_2 = medium_x_nominative_pronoun_2 - 2*standard_deviation_for_intervals_nominative_pronoun_2
boundary_2_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_2 = medium_x_nominative_pronoun_2 + 2*standard_deviation_for_intervals_nominative_pronoun_2
boundaries_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_2.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_2)
boundaries_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_2.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_2)
absolute_frequencies_distribution_95_per_cent_nominative_pronoun_2 = []
for i in xi_nominative_pronoun_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_2 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_2:
        absolute_frequencies_distribution_95_per_cent_nominative_pronoun_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ЗАЙМЕННИКИ-ІМЕННИКИ 2: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_nominative_pronoun_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ЗАЙМЕННИКИ-ІМЕННИКИ 2: ", len(absolute_frequencies_distribution_95_per_cent_nominative_pronoun_2))
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

h_interval_value_preposition_1 = (xi_preposition_1[-1]-xi_preposition_1[0])/5

intervals_preposition_1 = []

interval_1_preposition_1 = []
interval_1_preposition_1.append(xi_preposition_1[0])
boundary_interval_1_preposition_1 = xi_preposition_1[0] + h_interval_value_preposition_1
interval_1_preposition_1.append(boundary_interval_1_preposition_1)
intervals_preposition_1.append(interval_1_preposition_1)

interval_2_preposition_1 = []
interval_2_preposition_1.append(boundary_interval_1_preposition_1)
boundary_interval_2_preposition_1 = boundary_interval_1_preposition_1 + h_interval_value_preposition_1
interval_2_preposition_1.append(boundary_interval_2_preposition_1)
intervals_preposition_1.append(interval_2_preposition_1)

interval_3_preposition_1 = []
interval_3_preposition_1.append(boundary_interval_2_preposition_1)
boundary_interval_3_preposition_1 = boundary_interval_2_preposition_1 + h_interval_value_preposition_1
interval_3_preposition_1.append(boundary_interval_3_preposition_1)
intervals_preposition_1.append(interval_3_preposition_1)

interval_4_preposition_1 = []
interval_4_preposition_1.append(boundary_interval_3_preposition_1)
boundary_interval_4_preposition_1 = boundary_interval_3_preposition_1 + h_interval_value_preposition_1
interval_4_preposition_1.append(boundary_interval_4_preposition_1)
intervals_preposition_1.append(interval_4_preposition_1)

interval_5_preposition_1 = []
interval_5_preposition_1.append(boundary_interval_4_preposition_1)
boundary_interval_5_preposition_1 = boundary_interval_4_preposition_1 + h_interval_value_preposition_1
interval_5_preposition_1.append(boundary_interval_5_preposition_1)
intervals_preposition_1.append(interval_5_preposition_1)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ПРИЙМЕННИКИ 1: ", intervals_preposition_1)
##########################################################################################################################################

ni_in_intervals_preposition_1 = []
absolute_frequency_values_in_interval_1_preposition_1 = []
absolute_frequency_values_in_interval_2_preposition_1 = []
absolute_frequency_values_in_interval_3_preposition_1 = []
absolute_frequency_values_in_interval_4_preposition_1 = []
absolute_frequency_values_in_interval_5_preposition_1 = []
for i in xi_preposition_1:
    if i < interval_1_preposition_1[-1]:
        absolute_frequency_values_in_interval_1_preposition_1.append(i)
    elif i > interval_2_preposition_1[0] and i < interval_2_preposition_1[-1]:
        absolute_frequency_values_in_interval_2_preposition_1.append(i)
    elif i > interval_3_preposition_1[0] and i < interval_3_preposition_1[-1]:
        absolute_frequency_values_in_interval_3_preposition_1.append(i)
    elif i > interval_4_preposition_1[0] and i < interval_4_preposition_1[-1]:
        absolute_frequency_values_in_interval_4_preposition_1.append(i)
    elif i > interval_5_preposition_1[0]:
        absolute_frequency_values_in_interval_5_preposition_1.append(i)
ni_in_intervals_preposition_1.append(len(absolute_frequency_values_in_interval_1_preposition_1))
ni_in_intervals_preposition_1.append(len(absolute_frequency_values_in_interval_2_preposition_1))
ni_in_intervals_preposition_1.append(len(absolute_frequency_values_in_interval_3_preposition_1))
ni_in_intervals_preposition_1.append(len(absolute_frequency_values_in_interval_4_preposition_1))
ni_in_intervals_preposition_1.append(len(absolute_frequency_values_in_interval_5_preposition_1))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ПРИЙМЕННИКИ 1: ", ni_in_intervals_preposition_1)
##########################################################################################################################################

mediums_intervals_preposition_1 = []

medium_1_intervals_preposition_1 = []
for item in interval_1_preposition_1:
    middlepoint_1_preposition_1 = (interval_1_preposition_1[0] + interval_1_preposition_1[-1]) / 2
medium_1_intervals_preposition_1.append(middlepoint_1_preposition_1)
mediums_intervals_preposition_1.append(medium_1_intervals_preposition_1)

medium_2_intervals_preposition_1 = []
for item in interval_2_preposition_1:
    middlepoint_2_preposition_1 = (interval_2_preposition_1[0] + interval_2_preposition_1[-1]) / 2
medium_2_intervals_preposition_1.append(middlepoint_2_preposition_1)
mediums_intervals_preposition_1.append(medium_2_intervals_preposition_1)

medium_3_intervals_preposition_1 = []
for item in interval_3_preposition_1:
    middlepoint_3_preposition_1 = (interval_3_preposition_1[0] + interval_3_preposition_1[-1]) / 2
medium_3_intervals_preposition_1.append(middlepoint_3_preposition_1)
mediums_intervals_preposition_1.append(medium_3_intervals_preposition_1)

medium_4_intervals_preposition_1 = []
for item in interval_4_preposition_1:
    middlepoint_4_preposition_1 = (interval_4_preposition_1[0] + interval_4_preposition_1[-1]) / 2
medium_4_intervals_preposition_1.append(middlepoint_4_preposition_1)
mediums_intervals_preposition_1.append(medium_4_intervals_preposition_1)

medium_5_intervals_preposition_1 = []
for item in interval_5_preposition_1:
    middlepoint_5_preposition_1 = (interval_5_preposition_1[0] + interval_5_preposition_1[-1]) / 2
medium_5_intervals_preposition_1.append(middlepoint_5_preposition_1)
mediums_intervals_preposition_1.append(medium_5_intervals_preposition_1)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ПРИЙМЕННИКИ 1: ", mediums_intervals_preposition_1)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_1_preposition_1 = (medium_1_intervals_preposition_1[0] - medium_x_preposition_1)**2*ni_in_intervals_preposition_1[0]
xi_minus_medium_x_power_two_multiply_ni_2_preposition_1 = (medium_2_intervals_preposition_1[0] - medium_x_preposition_1)**2*ni_in_intervals_preposition_1[1]
xi_minus_medium_x_power_two_multiply_ni_3_preposition_1 = (medium_3_intervals_preposition_1[0] - medium_x_preposition_1)**2*ni_in_intervals_preposition_1[2]
xi_minus_medium_x_power_two_multiply_ni_4_preposition_1 = (medium_4_intervals_preposition_1[0] - medium_x_preposition_1)**2*ni_in_intervals_preposition_1[3]
xi_minus_medium_x_power_two_multiply_ni_5_preposition_1 = (medium_5_intervals_preposition_1[0] - medium_x_preposition_1)**2*ni_in_intervals_preposition_1[4]
sum_xi_minus_medium_x_power_two_multiply_ni_preposition_1 = (xi_minus_medium_x_power_two_multiply_ni_1_preposition_1
                                                            + xi_minus_medium_x_power_two_multiply_ni_2_preposition_1
                                                            + xi_minus_medium_x_power_two_multiply_ni_3_preposition_1
                                                            + xi_minus_medium_x_power_two_multiply_ni_4_preposition_1
                                                            + xi_minus_medium_x_power_two_multiply_ni_5_preposition_1)
standard_deviation_for_intervals_preposition_1 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_preposition_1/sum(ni_in_intervals_preposition_1))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_preposition_1)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_preposition_1 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_preposition_1 = medium_x_preposition_1 - standard_deviation_for_intervals_preposition_1
boundary_2_for_absolute_frequencies_distribution_68_per_cent_preposition_1 = medium_x_preposition_1 + standard_deviation_for_intervals_preposition_1
boundaries_for_absolute_frequencies_distribution_68_per_cent_preposition_1.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_preposition_1)
boundaries_for_absolute_frequencies_distribution_68_per_cent_preposition_1.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_preposition_1)
absolute_frequencies_distribution_68_per_cent_preposition_1 = []
for i in xi_preposition_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_preposition_1 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_preposition_1:
        absolute_frequencies_distribution_68_per_cent_preposition_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ПРИЙМЕННИКИ 1: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_preposition_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ПРИЙМЕННИКИ 1: ", len(absolute_frequencies_distribution_68_per_cent_preposition_1))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_preposition_1 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_preposition_1 = medium_x_preposition_1 - 2*standard_deviation_for_intervals_preposition_1
boundary_2_for_absolute_frequencies_distribution_95_per_cent_preposition_1 = medium_x_preposition_1 + 2*standard_deviation_for_intervals_preposition_1
boundaries_for_absolute_frequencies_distribution_95_per_cent_preposition_1.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_preposition_1)
boundaries_for_absolute_frequencies_distribution_95_per_cent_preposition_1.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_preposition_1)
absolute_frequencies_distribution_95_per_cent_preposition_1 = []
for i in xi_preposition_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_preposition_1 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_preposition_1:
        absolute_frequencies_distribution_95_per_cent_preposition_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ПРИЙМЕННИКИ 1: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_preposition_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ПРИЙМЕННИКИ 1: ", len(absolute_frequencies_distribution_95_per_cent_preposition_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

h_interval_value_preposition_2 = (xi_preposition_2[-2]-xi_preposition_2[0])/5

intervals_preposition_2 = []

interval_1_preposition_2 = []
interval_1_preposition_2.append(xi_preposition_2[0])
boundary_interval_1_preposition_2 = xi_preposition_2[0] + h_interval_value_preposition_2
interval_1_preposition_2.append(boundary_interval_1_preposition_2)
intervals_preposition_2.append(interval_1_preposition_2)

interval_2_preposition_2 = []
interval_2_preposition_2.append(boundary_interval_1_preposition_2)
boundary_interval_2_preposition_2 = boundary_interval_1_preposition_2 + h_interval_value_preposition_2
interval_2_preposition_2.append(boundary_interval_2_preposition_2)
intervals_preposition_2.append(interval_2_preposition_2)

interval_3_preposition_2 = []
interval_3_preposition_2.append(boundary_interval_2_preposition_2)
boundary_interval_3_preposition_2 = boundary_interval_2_preposition_2 + h_interval_value_preposition_2
interval_3_preposition_2.append(boundary_interval_3_preposition_2)
intervals_preposition_2.append(interval_3_preposition_2)

interval_4_preposition_2 = []
interval_4_preposition_2.append(boundary_interval_3_preposition_2)
boundary_interval_4_preposition_2 = boundary_interval_3_preposition_2 + h_interval_value_preposition_2
interval_4_preposition_2.append(boundary_interval_4_preposition_2)
intervals_preposition_2.append(interval_4_preposition_2)

interval_5_preposition_2 = []
interval_5_preposition_2.append(boundary_interval_4_preposition_2)
boundary_interval_5_preposition_2 = boundary_interval_4_preposition_2 + h_interval_value_preposition_2
interval_5_preposition_2.append(boundary_interval_5_preposition_2)
intervals_preposition_2.append(interval_5_preposition_2)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ПРИЙМЕННИКИ 2: ", intervals_preposition_2)
##########################################################################################################################################

ni_in_intervals_preposition_2 = []
absolute_frequency_values_in_interval_1_preposition_2 = []
absolute_frequency_values_in_interval_2_preposition_2 = []
absolute_frequency_values_in_interval_3_preposition_2 = []
absolute_frequency_values_in_interval_4_preposition_2 = []
absolute_frequency_values_in_interval_5_preposition_2 = []
for i in xi_preposition_2:
    if i < interval_1_preposition_2[-1]:
        absolute_frequency_values_in_interval_1_preposition_2.append(i)
    elif i > interval_2_preposition_2[0] and i < interval_2_preposition_2[-1]:
        absolute_frequency_values_in_interval_2_preposition_2.append(i)
    elif i > interval_3_preposition_2[0] and i < interval_3_preposition_2[-1]:
        absolute_frequency_values_in_interval_3_preposition_2.append(i)
    elif i > interval_4_preposition_2[0] and i < interval_4_preposition_2[-1]:
        absolute_frequency_values_in_interval_4_preposition_2.append(i)
    elif i > interval_5_preposition_2[0]:
        absolute_frequency_values_in_interval_5_preposition_2.append(i)
ni_in_intervals_preposition_2.append(len(absolute_frequency_values_in_interval_1_preposition_2))
ni_in_intervals_preposition_2.append(len(absolute_frequency_values_in_interval_2_preposition_2))
ni_in_intervals_preposition_2.append(len(absolute_frequency_values_in_interval_3_preposition_2))
ni_in_intervals_preposition_2.append(len(absolute_frequency_values_in_interval_4_preposition_2))
ni_in_intervals_preposition_2.append(len(absolute_frequency_values_in_interval_5_preposition_2))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ПРИЙМЕННИКИ 2: ", ni_in_intervals_preposition_2)
##########################################################################################################################################

mediums_intervals_preposition_2 = []

medium_1_intervals_preposition_2 = []
for item in interval_1_preposition_2:
    middlepoint_1_preposition_2 = (interval_1_preposition_2[0] + interval_1_preposition_2[-1]) / 2
medium_1_intervals_preposition_2.append(middlepoint_1_preposition_2)
mediums_intervals_preposition_2.append(medium_1_intervals_preposition_2)

medium_2_intervals_preposition_2 = []
for item in interval_2_preposition_2:
    middlepoint_2_preposition_2 = (interval_2_preposition_2[0] + interval_2_preposition_2[-1]) / 2
medium_2_intervals_preposition_2.append(middlepoint_2_preposition_2)
mediums_intervals_preposition_2.append(medium_2_intervals_preposition_2)

medium_3_intervals_preposition_2 = []
for item in interval_3_preposition_2:
    middlepoint_3_preposition_2 = (interval_3_preposition_2[0] + interval_3_preposition_2[-1]) / 2
medium_3_intervals_preposition_2.append(middlepoint_3_preposition_2)
mediums_intervals_preposition_2.append(medium_3_intervals_preposition_2)

medium_4_intervals_preposition_2 = []
for item in interval_4_preposition_2:
    middlepoint_4_preposition_2 = (interval_4_preposition_2[0] + interval_4_preposition_2[-1]) / 2
medium_4_intervals_preposition_2.append(middlepoint_4_preposition_2)
mediums_intervals_preposition_2.append(medium_4_intervals_preposition_2)

medium_5_intervals_preposition_2 = []
for item in interval_5_preposition_2:
    middlepoint_5_preposition_2 = (interval_5_preposition_2[0] + interval_5_preposition_2[-1]) / 2
medium_5_intervals_preposition_2.append(middlepoint_5_preposition_2)
mediums_intervals_preposition_2.append(medium_5_intervals_preposition_2)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ПРИЙМЕННИКИ 2: ", mediums_intervals_preposition_2)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_2_preposition_2 = (medium_2_intervals_preposition_2[0] - medium_x_preposition_2)**2*ni_in_intervals_preposition_2[0]
xi_minus_medium_x_power_two_multiply_ni_2_preposition_2 = (medium_2_intervals_preposition_2[0] - medium_x_preposition_2)**2*ni_in_intervals_preposition_2[2]
xi_minus_medium_x_power_two_multiply_ni_3_preposition_2 = (medium_3_intervals_preposition_2[0] - medium_x_preposition_2)**2*ni_in_intervals_preposition_2[2]
xi_minus_medium_x_power_two_multiply_ni_4_preposition_2 = (medium_4_intervals_preposition_2[0] - medium_x_preposition_2)**2*ni_in_intervals_preposition_2[3]
xi_minus_medium_x_power_two_multiply_ni_5_preposition_2 = (medium_5_intervals_preposition_2[0] - medium_x_preposition_2)**2*ni_in_intervals_preposition_2[4]
sum_xi_minus_medium_x_power_two_multiply_ni_preposition_2 = (xi_minus_medium_x_power_two_multiply_ni_2_preposition_2
                                                            + xi_minus_medium_x_power_two_multiply_ni_2_preposition_2
                                                            + xi_minus_medium_x_power_two_multiply_ni_3_preposition_2
                                                            + xi_minus_medium_x_power_two_multiply_ni_4_preposition_2
                                                            + xi_minus_medium_x_power_two_multiply_ni_5_preposition_2)
standard_deviation_for_intervals_preposition_2 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_preposition_2/sum(ni_in_intervals_preposition_2))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_preposition_2)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_preposition_2 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_preposition_2 = medium_x_preposition_2 - standard_deviation_for_intervals_preposition_2
boundary_2_for_absolute_frequencies_distribution_68_per_cent_preposition_2 = medium_x_preposition_2 + standard_deviation_for_intervals_preposition_2
boundaries_for_absolute_frequencies_distribution_68_per_cent_preposition_2.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_preposition_2)
boundaries_for_absolute_frequencies_distribution_68_per_cent_preposition_2.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_preposition_2)
absolute_frequencies_distribution_68_per_cent_preposition_2 = []
for i in xi_preposition_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_preposition_2 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_preposition_2:
        absolute_frequencies_distribution_68_per_cent_preposition_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ПРИЙМЕННИКИ 2: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_preposition_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ПРИЙМЕННИКИ 2: ", len(absolute_frequencies_distribution_68_per_cent_preposition_2))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_preposition_2 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_preposition_2 = medium_x_preposition_2 - 2*standard_deviation_for_intervals_preposition_2
boundary_2_for_absolute_frequencies_distribution_95_per_cent_preposition_2 = medium_x_preposition_2 + 2*standard_deviation_for_intervals_preposition_2
boundaries_for_absolute_frequencies_distribution_95_per_cent_preposition_2.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_preposition_2)
boundaries_for_absolute_frequencies_distribution_95_per_cent_preposition_2.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_preposition_2)
absolute_frequencies_distribution_95_per_cent_preposition_2 = []
for i in xi_preposition_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_preposition_2 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_preposition_2:
        absolute_frequencies_distribution_95_per_cent_preposition_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ПРИЙМЕННИКИ 2: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_preposition_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ПРИЙМЕННИКИ 2: ", len(absolute_frequencies_distribution_95_per_cent_preposition_2))
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

h_interval_value_conjunction_1 = (xi_conjunction_1[-1]-xi_conjunction_1[0])/5

intervals_conjunction_1 = []

interval_1_conjunction_1 = []
interval_1_conjunction_1.append(xi_conjunction_1[0])
boundary_interval_1_conjunction_1 = xi_conjunction_1[0] + h_interval_value_conjunction_1
interval_1_conjunction_1.append(boundary_interval_1_conjunction_1)
intervals_conjunction_1.append(interval_1_conjunction_1)

interval_2_conjunction_1 = []
interval_2_conjunction_1.append(boundary_interval_1_conjunction_1)
boundary_interval_2_conjunction_1 = boundary_interval_1_conjunction_1 + h_interval_value_conjunction_1
interval_2_conjunction_1.append(boundary_interval_2_conjunction_1)
intervals_conjunction_1.append(interval_2_conjunction_1)

interval_3_conjunction_1 = []
interval_3_conjunction_1.append(boundary_interval_2_conjunction_1)
boundary_interval_3_conjunction_1 = boundary_interval_2_conjunction_1 + h_interval_value_conjunction_1
interval_3_conjunction_1.append(boundary_interval_3_conjunction_1)
intervals_conjunction_1.append(interval_3_conjunction_1)

interval_4_conjunction_1 = []
interval_4_conjunction_1.append(boundary_interval_3_conjunction_1)
boundary_interval_4_conjunction_1 = boundary_interval_3_conjunction_1 + h_interval_value_conjunction_1
interval_4_conjunction_1.append(boundary_interval_4_conjunction_1)
intervals_conjunction_1.append(interval_4_conjunction_1)

interval_5_conjunction_1 = []
interval_5_conjunction_1.append(boundary_interval_4_conjunction_1)
boundary_interval_5_conjunction_1 = boundary_interval_4_conjunction_1 + h_interval_value_conjunction_1
interval_5_conjunction_1.append(boundary_interval_5_conjunction_1)
intervals_conjunction_1.append(interval_5_conjunction_1)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД СПОЛУЧНИКИ 1: ", intervals_conjunction_1)
##########################################################################################################################################

ni_in_intervals_conjunction_1 = []
absolute_frequency_values_in_interval_1_conjunction_1 = []
absolute_frequency_values_in_interval_2_conjunction_1 = []
absolute_frequency_values_in_interval_3_conjunction_1 = []
absolute_frequency_values_in_interval_4_conjunction_1 = []
absolute_frequency_values_in_interval_5_conjunction_1 = []
for i in xi_conjunction_1:
    if i < interval_1_conjunction_1[-1]:
        absolute_frequency_values_in_interval_1_conjunction_1.append(i)
    elif i > interval_2_conjunction_1[0] and i < interval_2_conjunction_1[-1]:
        absolute_frequency_values_in_interval_2_conjunction_1.append(i)
    elif i > interval_3_conjunction_1[0] and i < interval_3_conjunction_1[-1]:
        absolute_frequency_values_in_interval_3_conjunction_1.append(i)
    elif i > interval_4_conjunction_1[0] and i < interval_4_conjunction_1[-1]:
        absolute_frequency_values_in_interval_4_conjunction_1.append(i)
    elif i > interval_5_conjunction_1[0]:
        absolute_frequency_values_in_interval_5_conjunction_1.append(i)
ni_in_intervals_conjunction_1.append(len(absolute_frequency_values_in_interval_1_conjunction_1))
ni_in_intervals_conjunction_1.append(len(absolute_frequency_values_in_interval_2_conjunction_1))
ni_in_intervals_conjunction_1.append(len(absolute_frequency_values_in_interval_3_conjunction_1))
ni_in_intervals_conjunction_1.append(len(absolute_frequency_values_in_interval_4_conjunction_1))
ni_in_intervals_conjunction_1.append(len(absolute_frequency_values_in_interval_5_conjunction_1))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ СПОЛУЧНИКИ 1: ", ni_in_intervals_conjunction_1)
##########################################################################################################################################

mediums_intervals_conjunction_1 = []

medium_1_intervals_conjunction_1 = []
for item in interval_1_conjunction_1:
    middlepoint_1_conjunction_1 = (interval_1_conjunction_1[0] + interval_1_conjunction_1[-1]) / 2
medium_1_intervals_conjunction_1.append(middlepoint_1_conjunction_1)
mediums_intervals_conjunction_1.append(medium_1_intervals_conjunction_1)

medium_2_intervals_conjunction_1 = []
for item in interval_2_conjunction_1:
    middlepoint_2_conjunction_1 = (interval_2_conjunction_1[0] + interval_2_conjunction_1[-1]) / 2
medium_2_intervals_conjunction_1.append(middlepoint_2_conjunction_1)
mediums_intervals_conjunction_1.append(medium_2_intervals_conjunction_1)

medium_3_intervals_conjunction_1 = []
for item in interval_3_conjunction_1:
    middlepoint_3_conjunction_1 = (interval_3_conjunction_1[0] + interval_3_conjunction_1[-1]) / 2
medium_3_intervals_conjunction_1.append(middlepoint_3_conjunction_1)
mediums_intervals_conjunction_1.append(medium_3_intervals_conjunction_1)

medium_4_intervals_conjunction_1 = []
for item in interval_4_conjunction_1:
    middlepoint_4_conjunction_1 = (interval_4_conjunction_1[0] + interval_4_conjunction_1[-1]) / 2
medium_4_intervals_conjunction_1.append(middlepoint_4_conjunction_1)
mediums_intervals_conjunction_1.append(medium_4_intervals_conjunction_1)

medium_5_intervals_conjunction_1 = []
for item in interval_5_conjunction_1:
    middlepoint_5_conjunction_1 = (interval_5_conjunction_1[0] + interval_5_conjunction_1[-1]) / 2
medium_5_intervals_conjunction_1.append(middlepoint_5_conjunction_1)
mediums_intervals_conjunction_1.append(medium_5_intervals_conjunction_1)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ СПОЛУЧНИКИ 1: ", mediums_intervals_conjunction_1)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_1_conjunction_1 = (medium_1_intervals_conjunction_1[0] - medium_x_conjunction_1)**2*ni_in_intervals_conjunction_1[0]
xi_minus_medium_x_power_two_multiply_ni_2_conjunction_1 = (medium_2_intervals_conjunction_1[0] - medium_x_conjunction_1)**2*ni_in_intervals_conjunction_1[1]
xi_minus_medium_x_power_two_multiply_ni_3_conjunction_1 = (medium_3_intervals_conjunction_1[0] - medium_x_conjunction_1)**2*ni_in_intervals_conjunction_1[2]
xi_minus_medium_x_power_two_multiply_ni_4_conjunction_1 = (medium_4_intervals_conjunction_1[0] - medium_x_conjunction_1)**2*ni_in_intervals_conjunction_1[3]
xi_minus_medium_x_power_two_multiply_ni_5_conjunction_1 = (medium_5_intervals_conjunction_1[0] - medium_x_conjunction_1)**2*ni_in_intervals_conjunction_1[4]
sum_xi_minus_medium_x_power_two_multiply_ni_conjunction_1 = (xi_minus_medium_x_power_two_multiply_ni_1_conjunction_1
                                                            + xi_minus_medium_x_power_two_multiply_ni_2_conjunction_1
                                                            + xi_minus_medium_x_power_two_multiply_ni_3_conjunction_1
                                                            + xi_minus_medium_x_power_two_multiply_ni_4_conjunction_1
                                                            + xi_minus_medium_x_power_two_multiply_ni_5_conjunction_1)
standard_deviation_for_intervals_conjunction_1 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_conjunction_1/sum(ni_in_intervals_conjunction_1))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_conjunction_1)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_conjunction_1 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_conjunction_1 = medium_x_conjunction_1 - standard_deviation_for_intervals_conjunction_1
boundary_2_for_absolute_frequencies_distribution_68_per_cent_conjunction_1 = medium_x_conjunction_1 + standard_deviation_for_intervals_conjunction_1
boundaries_for_absolute_frequencies_distribution_68_per_cent_conjunction_1.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_conjunction_1)
boundaries_for_absolute_frequencies_distribution_68_per_cent_conjunction_1.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_conjunction_1)
absolute_frequencies_distribution_68_per_cent_conjunction_1 = []
for i in xi_conjunction_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_conjunction_1 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_conjunction_1:
        absolute_frequencies_distribution_68_per_cent_conjunction_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% СПОЛУЧНИКИ 1: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_conjunction_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% СПОЛУЧНИКИ 1: ", len(absolute_frequencies_distribution_68_per_cent_conjunction_1))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_conjunction_1 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_conjunction_1 = medium_x_conjunction_1 - 2*standard_deviation_for_intervals_conjunction_1
boundary_2_for_absolute_frequencies_distribution_95_per_cent_conjunction_1 = medium_x_conjunction_1 + 2*standard_deviation_for_intervals_conjunction_1
boundaries_for_absolute_frequencies_distribution_95_per_cent_conjunction_1.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_conjunction_1)
boundaries_for_absolute_frequencies_distribution_95_per_cent_conjunction_1.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_conjunction_1)
absolute_frequencies_distribution_95_per_cent_conjunction_1 = []
for i in xi_conjunction_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_conjunction_1 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_conjunction_1:
        absolute_frequencies_distribution_95_per_cent_conjunction_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% СПОЛУЧНИКИ 1: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_conjunction_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% СПОЛУЧНИКИ 1: ", len(absolute_frequencies_distribution_95_per_cent_conjunction_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

h_interval_value_conjunction_2 = (xi_conjunction_2[-2]-xi_conjunction_2[0])/5

intervals_conjunction_2 = []

interval_1_conjunction_2 = []
interval_1_conjunction_2.append(xi_conjunction_2[0])
boundary_interval_1_conjunction_2 = xi_conjunction_2[0] + h_interval_value_conjunction_2
interval_1_conjunction_2.append(boundary_interval_1_conjunction_2)
intervals_conjunction_2.append(interval_1_conjunction_2)

interval_2_conjunction_2 = []
interval_2_conjunction_2.append(boundary_interval_1_conjunction_2)
boundary_interval_2_conjunction_2 = boundary_interval_1_conjunction_2 + h_interval_value_conjunction_2
interval_2_conjunction_2.append(boundary_interval_2_conjunction_2)
intervals_conjunction_2.append(interval_2_conjunction_2)

interval_3_conjunction_2 = []
interval_3_conjunction_2.append(boundary_interval_2_conjunction_2)
boundary_interval_3_conjunction_2 = boundary_interval_2_conjunction_2 + h_interval_value_conjunction_2
interval_3_conjunction_2.append(boundary_interval_3_conjunction_2)
intervals_conjunction_2.append(interval_3_conjunction_2)

interval_4_conjunction_2 = []
interval_4_conjunction_2.append(boundary_interval_3_conjunction_2)
boundary_interval_4_conjunction_2 = boundary_interval_3_conjunction_2 + h_interval_value_conjunction_2
interval_4_conjunction_2.append(boundary_interval_4_conjunction_2)
intervals_conjunction_2.append(interval_4_conjunction_2)

interval_5_conjunction_2 = []
interval_5_conjunction_2.append(boundary_interval_4_conjunction_2)
boundary_interval_5_conjunction_2 = boundary_interval_4_conjunction_2 + h_interval_value_conjunction_2
interval_5_conjunction_2.append(boundary_interval_5_conjunction_2)
intervals_conjunction_2.append(interval_5_conjunction_2)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД СПОЛУЧНИКИ 2: ", intervals_conjunction_2)
##########################################################################################################################################

ni_in_intervals_conjunction_2 = []
absolute_frequency_values_in_interval_1_conjunction_2 = []
absolute_frequency_values_in_interval_2_conjunction_2 = []
absolute_frequency_values_in_interval_3_conjunction_2 = []
absolute_frequency_values_in_interval_4_conjunction_2 = []
absolute_frequency_values_in_interval_5_conjunction_2 = []
for i in xi_conjunction_2:
    if i < interval_1_conjunction_2[-1]:
        absolute_frequency_values_in_interval_1_conjunction_2.append(i)
    elif i > interval_2_conjunction_2[0] and i < interval_2_conjunction_2[-1]:
        absolute_frequency_values_in_interval_2_conjunction_2.append(i)
    elif i > interval_3_conjunction_2[0] and i < interval_3_conjunction_2[-1]:
        absolute_frequency_values_in_interval_3_conjunction_2.append(i)
    elif i > interval_4_conjunction_2[0] and i < interval_4_conjunction_2[-1]:
        absolute_frequency_values_in_interval_4_conjunction_2.append(i)
    elif i > interval_5_conjunction_2[0]:
        absolute_frequency_values_in_interval_5_conjunction_2.append(i)
ni_in_intervals_conjunction_2.append(len(absolute_frequency_values_in_interval_1_conjunction_2))
ni_in_intervals_conjunction_2.append(len(absolute_frequency_values_in_interval_2_conjunction_2))
ni_in_intervals_conjunction_2.append(len(absolute_frequency_values_in_interval_3_conjunction_2))
ni_in_intervals_conjunction_2.append(len(absolute_frequency_values_in_interval_4_conjunction_2))
ni_in_intervals_conjunction_2.append(len(absolute_frequency_values_in_interval_5_conjunction_2))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ СПОЛУЧНИКИ 2: ", ni_in_intervals_conjunction_2)
##########################################################################################################################################

mediums_intervals_conjunction_2 = []

medium_1_intervals_conjunction_2 = []
for item in interval_1_conjunction_2:
    middlepoint_1_conjunction_2 = (interval_1_conjunction_2[0] + interval_1_conjunction_2[-1]) / 2
medium_1_intervals_conjunction_2.append(middlepoint_1_conjunction_2)
mediums_intervals_conjunction_2.append(medium_1_intervals_conjunction_2)

medium_2_intervals_conjunction_2 = []
for item in interval_2_conjunction_2:
    middlepoint_2_conjunction_2 = (interval_2_conjunction_2[0] + interval_2_conjunction_2[-1]) / 2
medium_2_intervals_conjunction_2.append(middlepoint_2_conjunction_2)
mediums_intervals_conjunction_2.append(medium_2_intervals_conjunction_2)

medium_3_intervals_conjunction_2 = []
for item in interval_3_conjunction_2:
    middlepoint_3_conjunction_2 = (interval_3_conjunction_2[0] + interval_3_conjunction_2[-1]) / 2
medium_3_intervals_conjunction_2.append(middlepoint_3_conjunction_2)
mediums_intervals_conjunction_2.append(medium_3_intervals_conjunction_2)

medium_4_intervals_conjunction_2 = []
for item in interval_4_conjunction_2:
    middlepoint_4_conjunction_2 = (interval_4_conjunction_2[0] + interval_4_conjunction_2[-1]) / 2
medium_4_intervals_conjunction_2.append(middlepoint_4_conjunction_2)
mediums_intervals_conjunction_2.append(medium_4_intervals_conjunction_2)

medium_5_intervals_conjunction_2 = []
for item in interval_5_conjunction_2:
    middlepoint_5_conjunction_2 = (interval_5_conjunction_2[0] + interval_5_conjunction_2[-1]) / 2
medium_5_intervals_conjunction_2.append(middlepoint_5_conjunction_2)
mediums_intervals_conjunction_2.append(medium_5_intervals_conjunction_2)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ СПОЛУЧНИКИ 2: ", mediums_intervals_conjunction_2)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_2_conjunction_2 = (medium_2_intervals_conjunction_2[0] - medium_x_conjunction_2)**2*ni_in_intervals_conjunction_2[0]
xi_minus_medium_x_power_two_multiply_ni_2_conjunction_2 = (medium_2_intervals_conjunction_2[0] - medium_x_conjunction_2)**2*ni_in_intervals_conjunction_2[2]
xi_minus_medium_x_power_two_multiply_ni_3_conjunction_2 = (medium_3_intervals_conjunction_2[0] - medium_x_conjunction_2)**2*ni_in_intervals_conjunction_2[2]
xi_minus_medium_x_power_two_multiply_ni_4_conjunction_2 = (medium_4_intervals_conjunction_2[0] - medium_x_conjunction_2)**2*ni_in_intervals_conjunction_2[3]
xi_minus_medium_x_power_two_multiply_ni_5_conjunction_2 = (medium_5_intervals_conjunction_2[0] - medium_x_conjunction_2)**2*ni_in_intervals_conjunction_2[4]
sum_xi_minus_medium_x_power_two_multiply_ni_conjunction_2 = (xi_minus_medium_x_power_two_multiply_ni_2_conjunction_2
                                                            + xi_minus_medium_x_power_two_multiply_ni_2_conjunction_2
                                                            + xi_minus_medium_x_power_two_multiply_ni_3_conjunction_2
                                                            + xi_minus_medium_x_power_two_multiply_ni_4_conjunction_2
                                                            + xi_minus_medium_x_power_two_multiply_ni_5_conjunction_2)
standard_deviation_for_intervals_conjunction_2 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_conjunction_2/sum(ni_in_intervals_conjunction_2))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_conjunction_2)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_conjunction_2 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_conjunction_2 = medium_x_conjunction_2 - standard_deviation_for_intervals_conjunction_2
boundary_2_for_absolute_frequencies_distribution_68_per_cent_conjunction_2 = medium_x_conjunction_2 + standard_deviation_for_intervals_conjunction_2
boundaries_for_absolute_frequencies_distribution_68_per_cent_conjunction_2.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_conjunction_2)
boundaries_for_absolute_frequencies_distribution_68_per_cent_conjunction_2.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_conjunction_2)
absolute_frequencies_distribution_68_per_cent_conjunction_2 = []
for i in xi_conjunction_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_conjunction_2 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_conjunction_2:
        absolute_frequencies_distribution_68_per_cent_conjunction_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% СПОЛУЧНИКИ 2: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_conjunction_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% СПОЛУЧНИКИ 2: ", len(absolute_frequencies_distribution_68_per_cent_conjunction_2))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_conjunction_2 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_conjunction_2 = medium_x_conjunction_2 - 2*standard_deviation_for_intervals_conjunction_2
boundary_2_for_absolute_frequencies_distribution_95_per_cent_conjunction_2 = medium_x_conjunction_2 + 2*standard_deviation_for_intervals_conjunction_2
boundaries_for_absolute_frequencies_distribution_95_per_cent_conjunction_2.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_conjunction_2)
boundaries_for_absolute_frequencies_distribution_95_per_cent_conjunction_2.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_conjunction_2)
absolute_frequencies_distribution_95_per_cent_conjunction_2 = []
for i in xi_conjunction_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_conjunction_2 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_conjunction_2:
        absolute_frequencies_distribution_95_per_cent_conjunction_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% СПОЛУЧНИКИ 2: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_conjunction_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% СПОЛУЧНИКИ 2: ", len(absolute_frequencies_distribution_95_per_cent_conjunction_2))
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

h_interval_value_particle_1 = (xi_particle_1[-1]-xi_particle_1[0])/5

intervals_particle_1 = []

interval_1_particle_1 = []
interval_1_particle_1.append(xi_particle_1[0])
boundary_interval_1_particle_1 = xi_particle_1[0] + h_interval_value_particle_1
interval_1_particle_1.append(boundary_interval_1_particle_1)
intervals_particle_1.append(interval_1_particle_1)

interval_2_particle_1 = []
interval_2_particle_1.append(boundary_interval_1_particle_1)
boundary_interval_2_particle_1 = boundary_interval_1_particle_1 + h_interval_value_particle_1
interval_2_particle_1.append(boundary_interval_2_particle_1)
intervals_particle_1.append(interval_2_particle_1)

interval_3_particle_1 = []
interval_3_particle_1.append(boundary_interval_2_particle_1)
boundary_interval_3_particle_1 = boundary_interval_2_particle_1 + h_interval_value_particle_1
interval_3_particle_1.append(boundary_interval_3_particle_1)
intervals_particle_1.append(interval_3_particle_1)

interval_4_particle_1 = []
interval_4_particle_1.append(boundary_interval_3_particle_1)
boundary_interval_4_particle_1 = boundary_interval_3_particle_1 + h_interval_value_particle_1
interval_4_particle_1.append(boundary_interval_4_particle_1)
intervals_particle_1.append(interval_4_particle_1)

interval_5_particle_1 = []
interval_5_particle_1.append(boundary_interval_4_particle_1)
boundary_interval_5_particle_1 = boundary_interval_4_particle_1 + h_interval_value_particle_1
interval_5_particle_1.append(boundary_interval_5_particle_1)
intervals_particle_1.append(interval_5_particle_1)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ЧАСТКИ 1: ", intervals_particle_1)
##########################################################################################################################################

ni_in_intervals_particle_1 = []
absolute_frequency_values_in_interval_1_particle_1 = []
absolute_frequency_values_in_interval_2_particle_1 = []
absolute_frequency_values_in_interval_3_particle_1 = []
absolute_frequency_values_in_interval_4_particle_1 = []
absolute_frequency_values_in_interval_5_particle_1 = []
for i in xi_particle_1:
    if i < interval_1_particle_1[-1]:
        absolute_frequency_values_in_interval_1_particle_1.append(i)
    elif i > interval_2_particle_1[0] and i < interval_2_particle_1[-1]:
        absolute_frequency_values_in_interval_2_particle_1.append(i)
    elif i > interval_3_particle_1[0] and i < interval_3_particle_1[-1]:
        absolute_frequency_values_in_interval_3_particle_1.append(i)
    elif i > interval_4_particle_1[0] and i < interval_4_particle_1[-1]:
        absolute_frequency_values_in_interval_4_particle_1.append(i)
    elif i > interval_5_particle_1[0]:
        absolute_frequency_values_in_interval_5_particle_1.append(i)
ni_in_intervals_particle_1.append(len(absolute_frequency_values_in_interval_1_particle_1))
ni_in_intervals_particle_1.append(len(absolute_frequency_values_in_interval_2_particle_1))
ni_in_intervals_particle_1.append(len(absolute_frequency_values_in_interval_3_particle_1))
ni_in_intervals_particle_1.append(len(absolute_frequency_values_in_interval_4_particle_1))
ni_in_intervals_particle_1.append(len(absolute_frequency_values_in_interval_5_particle_1))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ЧАСТКИ 1: ", ni_in_intervals_particle_1)
##########################################################################################################################################

mediums_intervals_particle_1 = []

medium_1_intervals_particle_1 = []
for item in interval_1_particle_1:
    middlepoint_1_particle_1 = (interval_1_particle_1[0] + interval_1_particle_1[-1]) / 2
medium_1_intervals_particle_1.append(middlepoint_1_particle_1)
mediums_intervals_particle_1.append(medium_1_intervals_particle_1)

medium_2_intervals_particle_1 = []
for item in interval_2_particle_1:
    middlepoint_2_particle_1 = (interval_2_particle_1[0] + interval_2_particle_1[-1]) / 2
medium_2_intervals_particle_1.append(middlepoint_2_particle_1)
mediums_intervals_particle_1.append(medium_2_intervals_particle_1)

medium_3_intervals_particle_1 = []
for item in interval_3_particle_1:
    middlepoint_3_particle_1 = (interval_3_particle_1[0] + interval_3_particle_1[-1]) / 2
medium_3_intervals_particle_1.append(middlepoint_3_particle_1)
mediums_intervals_particle_1.append(medium_3_intervals_particle_1)

medium_4_intervals_particle_1 = []
for item in interval_4_particle_1:
    middlepoint_4_particle_1 = (interval_4_particle_1[0] + interval_4_particle_1[-1]) / 2
medium_4_intervals_particle_1.append(middlepoint_4_particle_1)
mediums_intervals_particle_1.append(medium_4_intervals_particle_1)

medium_5_intervals_particle_1 = []
for item in interval_5_particle_1:
    middlepoint_5_particle_1 = (interval_5_particle_1[0] + interval_5_particle_1[-1]) / 2
medium_5_intervals_particle_1.append(middlepoint_5_particle_1)
mediums_intervals_particle_1.append(medium_5_intervals_particle_1)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ЧАСТКИ 1: ", mediums_intervals_particle_1)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_1_particle_1 = (medium_1_intervals_particle_1[0] - medium_x_particle_1)**2*ni_in_intervals_particle_1[0]
xi_minus_medium_x_power_two_multiply_ni_2_particle_1 = (medium_2_intervals_particle_1[0] - medium_x_particle_1)**2*ni_in_intervals_particle_1[1]
xi_minus_medium_x_power_two_multiply_ni_3_particle_1 = (medium_3_intervals_particle_1[0] - medium_x_particle_1)**2*ni_in_intervals_particle_1[2]
xi_minus_medium_x_power_two_multiply_ni_4_particle_1 = (medium_4_intervals_particle_1[0] - medium_x_particle_1)**2*ni_in_intervals_particle_1[3]
xi_minus_medium_x_power_two_multiply_ni_5_particle_1 = (medium_5_intervals_particle_1[0] - medium_x_particle_1)**2*ni_in_intervals_particle_1[4]
sum_xi_minus_medium_x_power_two_multiply_ni_particle_1 = (xi_minus_medium_x_power_two_multiply_ni_1_particle_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_2_particle_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_3_particle_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_4_particle_1
                                                        + xi_minus_medium_x_power_two_multiply_ni_5_particle_1)
standard_deviation_for_intervals_particle_1 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_particle_1/sum(ni_in_intervals_particle_1))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_particle_1)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_particle_1 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_particle_1 = medium_x_particle_1 - standard_deviation_for_intervals_particle_1
boundary_2_for_absolute_frequencies_distribution_68_per_cent_particle_1 = medium_x_particle_1 + standard_deviation_for_intervals_particle_1
boundaries_for_absolute_frequencies_distribution_68_per_cent_particle_1.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_particle_1)
boundaries_for_absolute_frequencies_distribution_68_per_cent_particle_1.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_particle_1)
absolute_frequencies_distribution_68_per_cent_particle_1 = []
for i in xi_particle_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_particle_1 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_particle_1:
        absolute_frequencies_distribution_68_per_cent_particle_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ЧАСТКИ 1: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_particle_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ЧАСТКИ 1: ", len(absolute_frequencies_distribution_68_per_cent_particle_1))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_particle_1 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_particle_1 = medium_x_particle_1 - 2*standard_deviation_for_intervals_particle_1
boundary_2_for_absolute_frequencies_distribution_95_per_cent_particle_1 = medium_x_particle_1 + 2*standard_deviation_for_intervals_particle_1
boundaries_for_absolute_frequencies_distribution_95_per_cent_particle_1.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_particle_1)
boundaries_for_absolute_frequencies_distribution_95_per_cent_particle_1.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_particle_1)
absolute_frequencies_distribution_95_per_cent_particle_1 = []
for i in xi_particle_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_particle_1 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_particle_1:
        absolute_frequencies_distribution_95_per_cent_particle_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ЧАСТКИ 1: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_particle_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ЧАСТКИ 1: ", len(absolute_frequencies_distribution_95_per_cent_particle_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

h_interval_value_particle_2 = (xi_particle_2[-2]-xi_particle_2[0])/5

intervals_particle_2 = []

interval_1_particle_2 = []
interval_1_particle_2.append(xi_particle_2[0])
boundary_interval_1_particle_2 = xi_particle_2[0] + h_interval_value_particle_2
interval_1_particle_2.append(boundary_interval_1_particle_2)
intervals_particle_2.append(interval_1_particle_2)

interval_2_particle_2 = []
interval_2_particle_2.append(boundary_interval_1_particle_2)
boundary_interval_2_particle_2 = boundary_interval_1_particle_2 + h_interval_value_particle_2
interval_2_particle_2.append(boundary_interval_2_particle_2)
intervals_particle_2.append(interval_2_particle_2)

interval_3_particle_2 = []
interval_3_particle_2.append(boundary_interval_2_particle_2)
boundary_interval_3_particle_2 = boundary_interval_2_particle_2 + h_interval_value_particle_2
interval_3_particle_2.append(boundary_interval_3_particle_2)
intervals_particle_2.append(interval_3_particle_2)

interval_4_particle_2 = []
interval_4_particle_2.append(boundary_interval_3_particle_2)
boundary_interval_4_particle_2 = boundary_interval_3_particle_2 + h_interval_value_particle_2
interval_4_particle_2.append(boundary_interval_4_particle_2)
intervals_particle_2.append(interval_4_particle_2)

interval_5_particle_2 = []
interval_5_particle_2.append(boundary_interval_4_particle_2)
boundary_interval_5_particle_2 = boundary_interval_4_particle_2 + h_interval_value_particle_2
interval_5_particle_2.append(boundary_interval_5_particle_2)
intervals_particle_2.append(interval_5_particle_2)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ЧАСТКИ 2: ", intervals_particle_2)
##########################################################################################################################################

ni_in_intervals_particle_2 = []
absolute_frequency_values_in_interval_1_particle_2 = []
absolute_frequency_values_in_interval_2_particle_2 = []
absolute_frequency_values_in_interval_3_particle_2 = []
absolute_frequency_values_in_interval_4_particle_2 = []
absolute_frequency_values_in_interval_5_particle_2 = []
for i in xi_particle_2:
    if i < interval_1_particle_2[-1]:
        absolute_frequency_values_in_interval_1_particle_2.append(i)
    elif i > interval_2_particle_2[0] and i < interval_2_particle_2[-1]:
        absolute_frequency_values_in_interval_2_particle_2.append(i)
    elif i > interval_3_particle_2[0] and i < interval_3_particle_2[-1]:
        absolute_frequency_values_in_interval_3_particle_2.append(i)
    elif i > interval_4_particle_2[0] and i < interval_4_particle_2[-1]:
        absolute_frequency_values_in_interval_4_particle_2.append(i)
    elif i > interval_5_particle_2[0]:
        absolute_frequency_values_in_interval_5_particle_2.append(i)
ni_in_intervals_particle_2.append(len(absolute_frequency_values_in_interval_1_particle_2))
ni_in_intervals_particle_2.append(len(absolute_frequency_values_in_interval_2_particle_2))
ni_in_intervals_particle_2.append(len(absolute_frequency_values_in_interval_3_particle_2))
ni_in_intervals_particle_2.append(len(absolute_frequency_values_in_interval_4_particle_2))
ni_in_intervals_particle_2.append(len(absolute_frequency_values_in_interval_5_particle_2))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ЧАСТКИ 2: ", ni_in_intervals_particle_2)
##########################################################################################################################################

mediums_intervals_particle_2 = []

medium_1_intervals_particle_2 = []
for item in interval_1_particle_2:
    middlepoint_1_particle_2 = (interval_1_particle_2[0] + interval_1_particle_2[-1]) / 2
medium_1_intervals_particle_2.append(middlepoint_1_particle_2)
mediums_intervals_particle_2.append(medium_1_intervals_particle_2)

medium_2_intervals_particle_2 = []
for item in interval_2_particle_2:
    middlepoint_2_particle_2 = (interval_2_particle_2[0] + interval_2_particle_2[-1]) / 2
medium_2_intervals_particle_2.append(middlepoint_2_particle_2)
mediums_intervals_particle_2.append(medium_2_intervals_particle_2)

medium_3_intervals_particle_2 = []
for item in interval_3_particle_2:
    middlepoint_3_particle_2 = (interval_3_particle_2[0] + interval_3_particle_2[-1]) / 2
medium_3_intervals_particle_2.append(middlepoint_3_particle_2)
mediums_intervals_particle_2.append(medium_3_intervals_particle_2)

medium_4_intervals_particle_2 = []
for item in interval_4_particle_2:
    middlepoint_4_particle_2 = (interval_4_particle_2[0] + interval_4_particle_2[-1]) / 2
medium_4_intervals_particle_2.append(middlepoint_4_particle_2)
mediums_intervals_particle_2.append(medium_4_intervals_particle_2)

medium_5_intervals_particle_2 = []
for item in interval_5_particle_2:
    middlepoint_5_particle_2 = (interval_5_particle_2[0] + interval_5_particle_2[-1]) / 2
medium_5_intervals_particle_2.append(middlepoint_5_particle_2)
mediums_intervals_particle_2.append(medium_5_intervals_particle_2)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ЧАСТКИ 2: ", mediums_intervals_particle_2)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_2_particle_2 = (medium_2_intervals_particle_2[0] - medium_x_particle_2)**2*ni_in_intervals_particle_2[0]
xi_minus_medium_x_power_two_multiply_ni_2_particle_2 = (medium_2_intervals_particle_2[0] - medium_x_particle_2)**2*ni_in_intervals_particle_2[2]
xi_minus_medium_x_power_two_multiply_ni_3_particle_2 = (medium_3_intervals_particle_2[0] - medium_x_particle_2)**2*ni_in_intervals_particle_2[2]
xi_minus_medium_x_power_two_multiply_ni_4_particle_2 = (medium_4_intervals_particle_2[0] - medium_x_particle_2)**2*ni_in_intervals_particle_2[3]
xi_minus_medium_x_power_two_multiply_ni_5_particle_2 = (medium_5_intervals_particle_2[0] - medium_x_particle_2)**2*ni_in_intervals_particle_2[4]
sum_xi_minus_medium_x_power_two_multiply_ni_particle_2 = (xi_minus_medium_x_power_two_multiply_ni_2_particle_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_2_particle_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_3_particle_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_4_particle_2
                                                        + xi_minus_medium_x_power_two_multiply_ni_5_particle_2)
standard_deviation_for_intervals_particle_2 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_particle_2/sum(ni_in_intervals_particle_2))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_particle_2)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_particle_2 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_particle_2 = medium_x_particle_2 - standard_deviation_for_intervals_particle_2
boundary_2_for_absolute_frequencies_distribution_68_per_cent_particle_2 = medium_x_particle_2 + standard_deviation_for_intervals_particle_2
boundaries_for_absolute_frequencies_distribution_68_per_cent_particle_2.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_particle_2)
boundaries_for_absolute_frequencies_distribution_68_per_cent_particle_2.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_particle_2)
absolute_frequencies_distribution_68_per_cent_particle_2 = []
for i in xi_particle_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_particle_2 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_particle_2:
        absolute_frequencies_distribution_68_per_cent_particle_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ЧАСТКИ 2: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_particle_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ЧАСТКИ 2: ", len(absolute_frequencies_distribution_68_per_cent_particle_2))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_particle_2 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_particle_2 = medium_x_particle_2 - 2*standard_deviation_for_intervals_particle_2
boundary_2_for_absolute_frequencies_distribution_95_per_cent_particle_2 = medium_x_particle_2 + 2*standard_deviation_for_intervals_particle_2
boundaries_for_absolute_frequencies_distribution_95_per_cent_particle_2.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_particle_2)
boundaries_for_absolute_frequencies_distribution_95_per_cent_particle_2.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_particle_2)
absolute_frequencies_distribution_95_per_cent_particle_2 = []
for i in xi_particle_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_particle_2 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_particle_2:
        absolute_frequencies_distribution_95_per_cent_particle_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ЧАСТКИ 2: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_particle_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ЧАСТКИ 2: ", len(absolute_frequencies_distribution_95_per_cent_particle_2))
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

h_interval_value_interjection_1 = (xi_interjection_1[-1]-xi_interjection_1[0])/5

intervals_interjection_1 = []

interval_1_interjection_1 = []
interval_1_interjection_1.append(xi_interjection_1[0])
boundary_interval_1_interjection_1 = xi_interjection_1[0] + h_interval_value_interjection_1
interval_1_interjection_1.append(boundary_interval_1_interjection_1)
intervals_interjection_1.append(interval_1_interjection_1)

interval_2_interjection_1 = []
interval_2_interjection_1.append(boundary_interval_1_interjection_1)
boundary_interval_2_interjection_1 = boundary_interval_1_interjection_1 + h_interval_value_interjection_1
interval_2_interjection_1.append(boundary_interval_2_interjection_1)
intervals_interjection_1.append(interval_2_interjection_1)

interval_3_interjection_1 = []
interval_3_interjection_1.append(boundary_interval_2_interjection_1)
boundary_interval_3_interjection_1 = boundary_interval_2_interjection_1 + h_interval_value_interjection_1
interval_3_interjection_1.append(boundary_interval_3_interjection_1)
intervals_interjection_1.append(interval_3_interjection_1)

interval_4_interjection_1 = []
interval_4_interjection_1.append(boundary_interval_3_interjection_1)
boundary_interval_4_interjection_1 = boundary_interval_3_interjection_1 + h_interval_value_interjection_1
interval_4_interjection_1.append(boundary_interval_4_interjection_1)
intervals_interjection_1.append(interval_4_interjection_1)

interval_5_interjection_1 = []
interval_5_interjection_1.append(boundary_interval_4_interjection_1)
boundary_interval_5_interjection_1 = boundary_interval_4_interjection_1 + h_interval_value_interjection_1
interval_5_interjection_1.append(boundary_interval_5_interjection_1)
intervals_interjection_1.append(interval_5_interjection_1)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ВИГУКИ 1: ", intervals_interjection_1)
##########################################################################################################################################

ni_in_intervals_interjection_1 = []
absolute_frequency_values_in_interval_1_interjection_1 = []
absolute_frequency_values_in_interval_2_interjection_1 = []
absolute_frequency_values_in_interval_3_interjection_1 = []
absolute_frequency_values_in_interval_4_interjection_1 = []
absolute_frequency_values_in_interval_5_interjection_1 = []
for i in xi_interjection_1:
    if i < interval_1_interjection_1[-1]:
        absolute_frequency_values_in_interval_1_interjection_1.append(i)
    elif i > interval_2_interjection_1[0] and i < interval_2_interjection_1[-1]:
        absolute_frequency_values_in_interval_2_interjection_1.append(i)
    elif i > interval_3_interjection_1[0] and i < interval_3_interjection_1[-1]:
        absolute_frequency_values_in_interval_3_interjection_1.append(i)
    elif i > interval_4_interjection_1[0] and i < interval_4_interjection_1[-1]:
        absolute_frequency_values_in_interval_4_interjection_1.append(i)
    elif i > interval_5_interjection_1[0]:
        absolute_frequency_values_in_interval_5_interjection_1.append(i)
ni_in_intervals_interjection_1.append(len(absolute_frequency_values_in_interval_1_interjection_1))
ni_in_intervals_interjection_1.append(len(absolute_frequency_values_in_interval_2_interjection_1))
ni_in_intervals_interjection_1.append(len(absolute_frequency_values_in_interval_3_interjection_1))
ni_in_intervals_interjection_1.append(len(absolute_frequency_values_in_interval_4_interjection_1))
ni_in_intervals_interjection_1.append(len(absolute_frequency_values_in_interval_5_interjection_1))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ВИГУКИ 1: ", ni_in_intervals_interjection_1)
##########################################################################################################################################

mediums_intervals_interjection_1 = []

medium_1_intervals_interjection_1 = []
for item in interval_1_interjection_1:
    middlepoint_1_interjection_1 = (interval_1_interjection_1[0] + interval_1_interjection_1[-1]) / 2
medium_1_intervals_interjection_1.append(middlepoint_1_interjection_1)
mediums_intervals_interjection_1.append(medium_1_intervals_interjection_1)

medium_2_intervals_interjection_1 = []
for item in interval_2_interjection_1:
    middlepoint_2_interjection_1 = (interval_2_interjection_1[0] + interval_2_interjection_1[-1]) / 2
medium_2_intervals_interjection_1.append(middlepoint_2_interjection_1)
mediums_intervals_interjection_1.append(medium_2_intervals_interjection_1)

medium_3_intervals_interjection_1 = []
for item in interval_3_interjection_1:
    middlepoint_3_interjection_1 = (interval_3_interjection_1[0] + interval_3_interjection_1[-1]) / 2
medium_3_intervals_interjection_1.append(middlepoint_3_interjection_1)
mediums_intervals_interjection_1.append(medium_3_intervals_interjection_1)

medium_4_intervals_interjection_1 = []
for item in interval_4_interjection_1:
    middlepoint_4_interjection_1 = (interval_4_interjection_1[0] + interval_4_interjection_1[-1]) / 2
medium_4_intervals_interjection_1.append(middlepoint_4_interjection_1)
mediums_intervals_interjection_1.append(medium_4_intervals_interjection_1)

medium_5_intervals_interjection_1 = []
for item in interval_5_interjection_1:
    middlepoint_5_interjection_1 = (interval_5_interjection_1[0] + interval_5_interjection_1[-1]) / 2
medium_5_intervals_interjection_1.append(middlepoint_5_interjection_1)
mediums_intervals_interjection_1.append(medium_5_intervals_interjection_1)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ВИГУКИ 1: ", mediums_intervals_interjection_1)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_1_interjection_1 = (medium_1_intervals_interjection_1[0] - medium_x_interjection_1)**2*ni_in_intervals_interjection_1[0]
xi_minus_medium_x_power_two_multiply_ni_2_interjection_1 = (medium_2_intervals_interjection_1[0] - medium_x_interjection_1)**2*ni_in_intervals_interjection_1[1]
xi_minus_medium_x_power_two_multiply_ni_3_interjection_1 = (medium_3_intervals_interjection_1[0] - medium_x_interjection_1)**2*ni_in_intervals_interjection_1[2]
xi_minus_medium_x_power_two_multiply_ni_4_interjection_1 = (medium_4_intervals_interjection_1[0] - medium_x_interjection_1)**2*ni_in_intervals_interjection_1[3]
xi_minus_medium_x_power_two_multiply_ni_5_interjection_1 = (medium_5_intervals_interjection_1[0] - medium_x_interjection_1)**2*ni_in_intervals_interjection_1[4]
sum_xi_minus_medium_x_power_two_multiply_ni_interjection_1 = (xi_minus_medium_x_power_two_multiply_ni_1_interjection_1
                                                            + xi_minus_medium_x_power_two_multiply_ni_2_interjection_1
                                                            + xi_minus_medium_x_power_two_multiply_ni_3_interjection_1
                                                            + xi_minus_medium_x_power_two_multiply_ni_4_interjection_1
                                                            + xi_minus_medium_x_power_two_multiply_ni_5_interjection_1)
standard_deviation_for_intervals_interjection_1 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_interjection_1/sum(ni_in_intervals_interjection_1))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_interjection_1)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_interjection_1 = []
boundary_1_for_absolute_frequencies_distribution_68_per_cent_interjection_1 = medium_x_interjection_1 - standard_deviation_for_intervals_interjection_1
boundary_2_for_absolute_frequencies_distribution_68_per_cent_interjection_1 = medium_x_interjection_1 + standard_deviation_for_intervals_interjection_1
boundaries_for_absolute_frequencies_distribution_68_per_cent_interjection_1.append(boundary_1_for_absolute_frequencies_distribution_68_per_cent_interjection_1)
boundaries_for_absolute_frequencies_distribution_68_per_cent_interjection_1.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_interjection_1)
absolute_frequencies_distribution_68_per_cent_interjection_1 = []
for i in xi_interjection_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_68_per_cent_interjection_1 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_interjection_1:
        absolute_frequencies_distribution_68_per_cent_interjection_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ВИГУКИ 1: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_interjection_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ВИГУКИ 1: ", len(absolute_frequencies_distribution_68_per_cent_interjection_1))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_interjection_1 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_interjection_1 = medium_x_interjection_1 - 2*standard_deviation_for_intervals_interjection_1
boundary_2_for_absolute_frequencies_distribution_95_per_cent_interjection_1 = medium_x_interjection_1 + 2*standard_deviation_for_intervals_interjection_1
boundaries_for_absolute_frequencies_distribution_95_per_cent_interjection_1.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_interjection_1)
boundaries_for_absolute_frequencies_distribution_95_per_cent_interjection_1.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_interjection_1)
absolute_frequencies_distribution_95_per_cent_interjection_1 = []
for i in xi_interjection_1:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_interjection_1 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_interjection_1:
        absolute_frequencies_distribution_95_per_cent_interjection_1.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ВИГУКИ 1: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_interjection_1)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ВИГУКИ 1: ", len(absolute_frequencies_distribution_95_per_cent_interjection_1))
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

h_interval_value_interjection_2 = (xi_interjection_2[-2]-xi_interjection_2[0])/5

intervals_interjection_2 = []

interval_1_interjection_2 = []
interval_1_interjection_2.append(xi_interjection_2[0])
boundary_interval_1_interjection_2 = xi_interjection_2[0] + h_interval_value_interjection_2
interval_1_interjection_2.append(boundary_interval_1_interjection_2)
intervals_interjection_2.append(interval_1_interjection_2)

interval_2_interjection_2 = []
interval_2_interjection_2.append(boundary_interval_1_interjection_2)
boundary_interval_2_interjection_2 = boundary_interval_1_interjection_2 + h_interval_value_interjection_2
interval_2_interjection_2.append(boundary_interval_2_interjection_2)
intervals_interjection_2.append(interval_2_interjection_2)

interval_3_interjection_2 = []
interval_3_interjection_2.append(boundary_interval_2_interjection_2)
boundary_interval_3_interjection_2 = boundary_interval_2_interjection_2 + h_interval_value_interjection_2
interval_3_interjection_2.append(boundary_interval_3_interjection_2)
intervals_interjection_2.append(interval_3_interjection_2)

interval_4_interjection_2 = []
interval_4_interjection_2.append(boundary_interval_3_interjection_2)
boundary_interval_4_interjection_2 = boundary_interval_3_interjection_2 + h_interval_value_interjection_2
interval_4_interjection_2.append(boundary_interval_4_interjection_2)
intervals_interjection_2.append(interval_4_interjection_2)

interval_5_interjection_2 = []
interval_5_interjection_2.append(boundary_interval_4_interjection_2)
boundary_interval_5_interjection_2 = boundary_interval_4_interjection_2 + h_interval_value_interjection_2
interval_5_interjection_2.append(boundary_interval_5_interjection_2)
intervals_interjection_2.append(interval_5_interjection_2)
##########################################################################################################################################
# print("ІНТЕРВАЛЬНИЙ РЯД ВИГУКИ 2: ", intervals_interjection_2)
##########################################################################################################################################

ni_in_intervals_interjection_2 = []
absolute_frequency_values_in_interval_1_interjection_2 = []
absolute_frequency_values_in_interval_2_interjection_2 = []
absolute_frequency_values_in_interval_3_interjection_2 = []
absolute_frequency_values_in_interval_4_interjection_2 = []
absolute_frequency_values_in_interval_5_interjection_2 = []
for i in xi_interjection_2:
    if i < interval_1_interjection_2[-1]:
        absolute_frequency_values_in_interval_1_interjection_2.append(i)
    elif i > interval_2_interjection_2[0] and i < interval_2_interjection_2[-1]:
        absolute_frequency_values_in_interval_2_interjection_2.append(i)
    elif i > interval_3_interjection_2[0] and i < interval_3_interjection_2[-1]:
        absolute_frequency_values_in_interval_3_interjection_2.append(i)
    elif i > interval_4_interjection_2[0] and i < interval_4_interjection_2[-1]:
        absolute_frequency_values_in_interval_4_interjection_2.append(i)
    elif i > interval_5_interjection_2[0]:
        absolute_frequency_values_in_interval_5_interjection_2.append(i)
ni_in_intervals_interjection_2.append(len(absolute_frequency_values_in_interval_1_interjection_2))
ni_in_intervals_interjection_2.append(len(absolute_frequency_values_in_interval_2_interjection_2))
ni_in_intervals_interjection_2.append(len(absolute_frequency_values_in_interval_3_interjection_2))
ni_in_intervals_interjection_2.append(len(absolute_frequency_values_in_interval_4_interjection_2))
ni_in_intervals_interjection_2.append(len(absolute_frequency_values_in_interval_5_interjection_2))
##########################################################################################################################################
# print("АЧ В ІНТЕРВАЛАХ ВИГУКИ 2: ", ni_in_intervals_interjection_2)
##########################################################################################################################################

mediums_intervals_interjection_2 = []

medium_1_intervals_interjection_2 = []
for item in interval_1_interjection_2:
    middlepoint_1_interjection_2 = (interval_1_interjection_2[0] + interval_1_interjection_2[-1]) / 2
medium_1_intervals_interjection_2.append(middlepoint_1_interjection_2)
mediums_intervals_interjection_2.append(medium_1_intervals_interjection_2)

medium_2_intervals_interjection_2 = []
for item in interval_2_interjection_2:
    middlepoint_2_interjection_2 = (interval_2_interjection_2[0] + interval_2_interjection_2[-1]) / 2
medium_2_intervals_interjection_2.append(middlepoint_2_interjection_2)
mediums_intervals_interjection_2.append(medium_2_intervals_interjection_2)

medium_3_intervals_interjection_2 = []
for item in interval_3_interjection_2:
    middlepoint_3_interjection_2 = (interval_3_interjection_2[0] + interval_3_interjection_2[-1]) / 2
medium_3_intervals_interjection_2.append(middlepoint_3_interjection_2)
mediums_intervals_interjection_2.append(medium_3_intervals_interjection_2)

medium_4_intervals_interjection_2 = []
for item in interval_4_interjection_2:
    middlepoint_4_interjection_2 = (interval_4_interjection_2[0] + interval_4_interjection_2[-1]) / 2
medium_4_intervals_interjection_2.append(middlepoint_4_interjection_2)
mediums_intervals_interjection_2.append(medium_4_intervals_interjection_2)

medium_5_intervals_interjection_2 = []
for item in interval_5_interjection_2:
    middlepoint_5_interjection_2 = (interval_5_interjection_2[0] + interval_5_interjection_2[-1]) / 2
medium_5_intervals_interjection_2.append(middlepoint_5_interjection_2)
mediums_intervals_interjection_2.append(medium_5_intervals_interjection_2)
##########################################################################################################################################
# print("СЕРЕДИНИ ІНТЕРВАЛІВ ВИГУКИ 2: ", mediums_intervals_interjection_2)
##########################################################################################################################################

xi_minus_medium_x_power_two_multiply_ni_2_interjection_2 = (medium_2_intervals_interjection_2[0] - medium_x_interjection_2)**2*ni_in_intervals_interjection_2[0]
xi_minus_medium_x_power_two_multiply_ni_2_interjection_2 = (medium_2_intervals_interjection_2[0] - medium_x_interjection_2)**2*ni_in_intervals_interjection_2[2]
xi_minus_medium_x_power_two_multiply_ni_3_interjection_2 = (medium_3_intervals_interjection_2[0] - medium_x_interjection_2)**2*ni_in_intervals_interjection_2[2]
xi_minus_medium_x_power_two_multiply_ni_4_interjection_2 = (medium_4_intervals_interjection_2[0] - medium_x_interjection_2)**2*ni_in_intervals_interjection_2[3]
xi_minus_medium_x_power_two_multiply_ni_5_interjection_2 = (medium_5_intervals_interjection_2[0] - medium_x_interjection_2)**2*ni_in_intervals_interjection_2[4]
sum_xi_minus_medium_x_power_two_multiply_ni_interjection_2 = (xi_minus_medium_x_power_two_multiply_ni_2_interjection_2
                                                            + xi_minus_medium_x_power_two_multiply_ni_2_interjection_2
                                                            + xi_minus_medium_x_power_two_multiply_ni_3_interjection_2
                                                            + xi_minus_medium_x_power_two_multiply_ni_4_interjection_2
                                                            + xi_minus_medium_x_power_two_multiply_ni_5_interjection_2)
standard_deviation_for_intervals_interjection_2 = math.sqrt(sum_xi_minus_medium_x_power_two_multiply_ni_interjection_2/sum(ni_in_intervals_interjection_2))
##########################################################################################################################################
# print(sum_xi_minus_medium_x_power_two_multiply_ni_interjection_2)
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_68_per_cent_interjection_2 = []
boundary_2_for_absolute_frequencies_distribution_68_per_cent_interjection_2 = medium_x_interjection_2 - standard_deviation_for_intervals_interjection_2
boundary_2_for_absolute_frequencies_distribution_68_per_cent_interjection_2 = medium_x_interjection_2 + standard_deviation_for_intervals_interjection_2
boundaries_for_absolute_frequencies_distribution_68_per_cent_interjection_2.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_interjection_2)
boundaries_for_absolute_frequencies_distribution_68_per_cent_interjection_2.append(boundary_2_for_absolute_frequencies_distribution_68_per_cent_interjection_2)
absolute_frequencies_distribution_68_per_cent_interjection_2 = []
for i in xi_interjection_2:
    if i >= boundary_2_for_absolute_frequencies_distribution_68_per_cent_interjection_2 and i <= boundary_2_for_absolute_frequencies_distribution_68_per_cent_interjection_2:
        absolute_frequencies_distribution_68_per_cent_interjection_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 68% ВИГУКИ 2: ", boundaries_for_absolute_frequencies_distribution_68_per_cent_interjection_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 68% ВИГУКИ 2: ", len(absolute_frequencies_distribution_68_per_cent_interjection_2))
##########################################################################################################################################
boundaries_for_absolute_frequencies_distribution_95_per_cent_interjection_2 = []
boundary_1_for_absolute_frequencies_distribution_95_per_cent_interjection_2 = medium_x_interjection_2 - 2*standard_deviation_for_intervals_interjection_2
boundary_2_for_absolute_frequencies_distribution_95_per_cent_interjection_2 = medium_x_interjection_2 + 2*standard_deviation_for_intervals_interjection_2
boundaries_for_absolute_frequencies_distribution_95_per_cent_interjection_2.append(boundary_1_for_absolute_frequencies_distribution_95_per_cent_interjection_2)
boundaries_for_absolute_frequencies_distribution_95_per_cent_interjection_2.append(boundary_2_for_absolute_frequencies_distribution_95_per_cent_interjection_2)
absolute_frequencies_distribution_95_per_cent_interjection_2 = []
for i in xi_interjection_2:
    if i >= boundary_1_for_absolute_frequencies_distribution_95_per_cent_interjection_2 and i <= boundary_2_for_absolute_frequencies_distribution_95_per_cent_interjection_2:
        absolute_frequencies_distribution_95_per_cent_interjection_2.append(i)
##########################################################################################################################################
# print("МЕЖІ СМУГИ КОЛИВАННЯ 95% ВИГУКИ 2: ", boundaries_for_absolute_frequencies_distribution_95_per_cent_interjection_2)
# print("КІЛЬКІСТЬ АЧ У СМУЗІ КОЛИВАННЯ 95% ВИГУКИ 2: ", len(absolute_frequencies_distribution_95_per_cent_interjection_2))
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# цей блок перевіряє, чи є межа останнього інтервалу більшою за найбільшу абсолютну частоту, чи навпаки, меншою,
# і видає користувачеві (-ці) повідомлення про це
# створюємо змінну user_answer_concerning_interval_boundaries, яка просить користувача (-ку) написати стверджувальну відповідь ("ок"),
# щоб програма показала інформацію про межі останніх інтервалів і найбільші частоти
# пишемо цикл, який перевіряє відповідь користувача (-ки) на питання програми
# за його умовою, програму буде зупинено лише тоді, коли користувач (-ка) напише "ок",
# інакше програма буде тривати нескінченно
##########################################################################################################################################
##########################################################################################################################################
# user_answer_concerning_interval_boundaries = input("Повідомлення про межі інтервалів варіяційних рядів частин мови. Щоб його прочитати, напишіть 'ок' ")
# while user_answer_concerning_interval_boundaries != 'ок':
#     user_answer_concerning_interval_boundaries = input("Спробуйте ще раз, напишіть саме 'ок' ")
# else:
# ############################################################## ВИБІРКА 1 ###############################################################
#     if interval_5_noun_1[-1] > xi_noun_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_noun_1} більша за останнє значення варіяційного ряду іменників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду іменників (ВИБІРКА 1): ", xi_noun_1[-1])
#     elif interval_5_noun_1[-1] < xi_noun_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_noun_1} менша за останнє значення варіяційного ряду іменників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду іменників (ВИБІРКА 1): ", xi_noun_1[-1])
#     if interval_5_adjective_1[-1] > xi_adjective_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_adjective_1} більша за останнє значення варіяційного ряду прикметників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду прикметників (ВИБІРКА 1): ", xi_adjective_1[-1])
#     elif interval_5_adjective_1[-1] < xi_adjective_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_adjective_1} менша за останнє значення варіяційного ряду прикметників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду прикметників (ВИБІРКА 1): ", xi_adjective_1[-1])
#     if interval_5_verb_1[-1] > xi_verb_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_verb_1} більша за останнє значення варіяційного ряду дієслів (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду дієслів (ВИБІРКА 1): ", xi_verb_1[-1])
#     elif interval_5_verb_1[-1] < xi_verb_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_verb_1} менша за останнє значення варіяційного ряду дієслів (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду дієслів (ВИБІРКА 1): ", xi_verb_1[-1])
#     if interval_5_gerund_1[-1] > xi_gerund_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_gerund_1} більша за останнє значення варіяційного ряду дієприслівників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду дієприслівників (ВИБІРКА 1): ", xi_gerund_1[-1])
#     elif interval_5_gerund_1[-1] < xi_gerund_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_gerund_1} менша за останнє значення варіяційного ряду дієприслівників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду дієприслівників (ВИБІРКА 1): ", xi_gerund_1[-1])
#     if interval_5_numeral_1[-1] > xi_numeral_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_numeral_1} більша за останнє значення варіяційного ряду числівників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду числівників (ВИБІРКА 1): ", xi_numeral_1[-1])
#     elif interval_5_numeral_1[-1] < xi_numeral_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_numeral_1} менша за останнє значення варіяційного ряду числівників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду числівників (ВИБІРКА 1): ", xi_numeral_1[-1])
#     if interval_5_adverb_1[-1] > xi_adverb_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_adverb_1} більша за останнє значення варіяційного ряду прислівників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду прислівників (ВИБІРКА 1): ", xi_adverb_1[-1])
#     elif interval_5_adverb_1[-1] < xi_adverb_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_adverb_1} менша за останнє значення варіяційного ряду прислівників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду прислівників (ВИБІРКА 1): ", xi_adverb_1[-1])
#     if interval_5_nominative_pronoun_1[-1] > xi_nominative_pronoun_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_nominative_pronoun_1} більша за останнє значення варіяційного ряду займенників-іменників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду займенників-іменників (ВИБІРКА 1): ", xi_nominative_pronoun_1[-1])
#     elif interval_5_nominative_pronoun_1[-1] < xi_nominative_pronoun_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_nominative_pronoun_1} менша за останнє значення варіяційного ряду займенників-іменників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду займенників-іменників (ВИБІРКА 1): ", xi_nominative_pronoun_1[-1])
#     if interval_5_preposition_1[-1] > xi_preposition_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_preposition_1} більша за останнє значення варіяційного ряду прийменників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду прийменників (ВИБІРКА 1): ", xi_preposition_1[-1])
#     elif interval_5_preposition_1[-1] < xi_preposition_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_preposition_1} менша за останнє значення варіяційного ряду прийменників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду прийменників (ВИБІРКА 1): ", xi_preposition_1[-1])
#     if interval_5_conjunction_1[-1] > xi_conjunction_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_conjunction_1} більша за останнє значення варіяційного ряду сполучників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду сполучників (ВИБІРКА 1): ", xi_conjunction_1[-1])
#     elif interval_5_conjunction_1[-1] < xi_conjunction_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_conjunction_1} менша за останнє значення варіяційного ряду сполучників (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду сполучників (ВИБІРКА 1): ", xi_conjunction_1[-1])
#     if interval_5_particle_1[-1] > xi_particle_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_particle_1} більша за останнє значення варіяційного ряду часток (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду часток (ВИБІРКА 1): ", xi_particle_1[-1])
#     elif interval_5_particle_1[-1] < xi_particle_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_particle_1} менша за останнє значення варіяційного ряду часток (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду часток (ВИБІРКА 1): ", xi_particle_1[-1])
#     if interval_5_interjection_1[-1] > xi_interjection_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_interjection_1} більша за останнє значення варіяційного ряду вигуків (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду вигуків (ВИБІРКА 1): ", xi_interjection_1[-1])
#     elif interval_5_interjection_1[-1] < xi_interjection_1[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_interjection_1} менша за останнє значення варіяційного ряду вигуків (ВИБІРКА 1)!")
#         print("Останнє значення варіяційного ряду вигуків (ВИБІРКА 1): ", xi_interjection_1[-1])
# ############################################################## ВИБІРКА 2 ###############################################################
#     if interval_5_noun_2[-1] > xi_noun_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_noun_2} більша за останнє значення варіяційного ряду іменників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду іменників (ВИБІРКА 2): ", xi_noun_2[-1])
#     elif interval_5_noun_2[-1] < xi_noun_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_noun_2} менша за останнє значення варіяційного ряду іменників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду іменників (ВИБІРКА 2): ", xi_noun_2[-1])
#     if interval_5_adjective_2[-1] > xi_adjective_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_adjective_2} більша за останнє значення варіяційного ряду прикметників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду прикметників (ВИБІРКА 2): ", xi_adjective_2[-1])
#     elif interval_5_adjective_2[-1] < xi_adjective_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_adjective_2} менша за останнє значення варіяційного ряду прикметників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду прикметників (ВИБІРКА 2): ", xi_adjective_2[-1])
#     if interval_5_verb_2[-1] > xi_verb_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_verb_2} більша за останнє значення варіяційного ряду дієслів (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду дієслів (ВИБІРКА 2): ", xi_verb_2[-1])
#     elif interval_5_verb_2[-1] < xi_verb_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_verb_2} менша за останнє значення варіяційного ряду дієслів (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду дієслів (ВИБІРКА 2): ", xi_verb_2[-1])
#     if interval_5_gerund_2[-1] > xi_gerund_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_gerund_2} більша за останнє значення варіяційного ряду дієприслівників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду дієприслівників (ВИБІРКА 2): ", xi_gerund_2[-1])
#     elif interval_5_gerund_2[-1] < xi_gerund_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_gerund_2} менша за останнє значення варіяційного ряду дієприслівників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду дієприслівників (ВИБІРКА 2): ", xi_gerund_2[-1])
#     if interval_5_numeral_2[-1] > xi_numeral_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_numeral_2} більша за останнє значення варіяційного ряду числівників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду числівників (ВИБІРКА 2): ", xi_numeral_2[-1])
#     elif interval_5_numeral_2[-1] < xi_numeral_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_numeral_2} менша за останнє значення варіяційного ряду числівників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду числівників (ВИБІРКА 2): ", xi_numeral_2[-1])
#     if interval_5_adverb_2[-1] > xi_adverb_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_adverb_2} більша за останнє значення варіяційного ряду прислівників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду прислівників (ВИБІРКА 2): ", xi_adverb_2[-1])
#     elif interval_5_adverb_2[-1] < xi_adverb_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_adverb_2} менша за останнє значення варіяційного ряду прислівників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду прислівників (ВИБІРКА 2): ", xi_adverb_2[-1])
#     if interval_5_nominative_pronoun_2[-1] > xi_nominative_pronoun_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_nominative_pronoun_2} більша за останнє значення варіяційного ряду займенників-іменників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду займенників-іменників (ВИБІРКА 2): ", xi_nominative_pronoun_2[-1])
#     elif interval_5_nominative_pronoun_2[-1] < xi_nominative_pronoun_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_nominative_pronoun_2} менша за останнє значення варіяційного ряду займенників-іменників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду займенників-іменників (ВИБІРКА 2): ", xi_nominative_pronoun_2[-1])
#     if interval_5_preposition_2[-1] > xi_preposition_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_preposition_2} більша за останнє значення варіяційного ряду прийменників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду прийменників (ВИБІРКА 2): ", xi_preposition_2[-1])
#     elif interval_5_preposition_2[-1] < xi_preposition_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_preposition_2} менша за останнє значення варіяційного ряду прийменників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду прийменників (ВИБІРКА 2): ", xi_preposition_2[-1])
#     if interval_5_conjunction_2[-1] > xi_conjunction_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_conjunction_2} більша за останнє значення варіяційного ряду сполучників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду сполучників (ВИБІРКА 2): ", xi_conjunction_2[-1])
#     elif interval_5_conjunction_2[-1] < xi_conjunction_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_conjunction_2} менша за останнє значення варіяційного ряду сполучників (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду сполучників (ВИБІРКА 2): ", xi_conjunction_2[-1])
#     if interval_5_particle_2[-1] > xi_particle_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_particle_2} більша за останнє значення варіяційного ряду часток (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду часток (ВИБІРКА 2): ", xi_particle_2[-1])
#     elif interval_5_particle_2[-1] < xi_particle_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_particle_2} менша за останнє значення варіяційного ряду часток (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду часток (ВИБІРКА 2): ", xi_particle_2[-1])
#     if interval_5_interjection_2[-1] > xi_interjection_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_interjection_2} більша за останнє значення варіяційного ряду вигуків (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду вигуків (ВИБІРКА 2): ", xi_interjection_2[-1])
#     elif interval_5_interjection_2[-1] < xi_interjection_2[-1]:
#         print(f"Друга межа останнього інтервалу {interval_5_interjection_2} менша за останнє значення варіяційного ряду вигуків (ВИБІРКА 2)!")
#         print("Останнє значення варіяційного ряду вигуків (ВИБІРКА 2): ", xi_interjection_2[-1])
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# вираховуємо відносну похибку для кожної частини мови в межах обох вибірок
# для цього загадуємо змінні, значеннями яких є відносні похибки
# (пишемо формулу, де застосовуємо метод sqrt() з бібліотеки math,
# а також метод list() для значень з частотних словників абсолютних частот частин мови
# (а оскільки після цього методу значення із словників сприймаються програмою як елементи списків,
# тут же пишемо індекс потрібного елемента у квадратних дужках)
# у всіх моїх ЧС частин мови ключі є однаковими, розташованими в однаковому порядку,
# тому я знаю, що іменник є першим елементом, отже, його індекс дорівнює 0,
# що прикметник - другий, тому й індекс 1 тощо)
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

absolute_frequency_parts_of_speech_sample_1_values = list(absolute_frequency_parts_of_speech_sample_1.values())


relative_error_noun_1 = (1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_1_values[0])*100, "%")
relative_error_noun_1 = ' '.join([str(element) for element in relative_error_noun_1])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ІМЕННИКИ 1: ", relative_error_noun_1)
##########################################################################################################################################

relative_error_adjective_1 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_1_values[1]))*100, "%")
relative_error_adjective_1 = ' '.join([str(element) for element in relative_error_adjective_1])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ПРИКМЕТНИКИ 1: ",relative_error_adjective_1)
##########################################################################################################################################

relative_error_verb_1 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_1_values[2]))*100, "%")
relative_error_verb_1 = ' '.join([str(element) for element in relative_error_verb_1])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ДІЄСЛОВА 1: ", relative_error_verb_1)
##########################################################################################################################################

relative_error_gerund_1 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_1_values[3]))*100, "%")
relative_error_gerund_1 = ' '.join([str(element) for element in relative_error_gerund_1])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ДІЄПРИСЛІВНИКИ 1: ", relative_error_gerund_1)
##########################################################################################################################################

relative_error_numeral_1 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_1_values[4]))*100, "%")
relative_error_numeral_1 = ' '.join([str(element) for element in relative_error_numeral_1])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ЧИСЛІВНИКИ 1: ", relative_error_numeral_1)
##########################################################################################################################################

relative_error_adverb_1 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_1_values[5]))*100, "%")
relative_error_adverb_1 = ' '.join([str(element) for element in relative_error_adverb_1])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ПРИСЛІВНИКИ 1: ", relative_error_adverb_1)
##########################################################################################################################################

relative_error_nominative_pronoun_1 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_1_values[6]))*100, "%")
relative_error_nominative_pronoun_1 = ' '.join([str(element) for element in relative_error_nominative_pronoun_1])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ЗАЙМЕННИКИ-ІМЕННИКИ 1: ", relative_error_nominative_pronoun_1)
##########################################################################################################################################

relative_error_preposition_1 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_1_values[7]))*100, "%")
relative_error_preposition_1 = ' '.join([str(element) for element in relative_error_preposition_1])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ПРИЙМЕННИКИ 1: ", relative_error_preposition_1)
##########################################################################################################################################

relative_error_conjunction_1 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_1_values[8]))*100, "%")
relative_error_conjunction_1 = ' '.join([str(element) for element in relative_error_conjunction_1])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА СПОЛУЧНИКИ 1: ", relative_error_conjunction_1)
##########################################################################################################################################

relative_error_particle_1 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_1_values[9]))*100, "%")
relative_error_particle_1 = ' '.join([str(element) for element in relative_error_particle_1])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ЧАСТКИ 1: ", relative_error_particle_1)
##########################################################################################################################################

relative_error_interjection_1 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_1_values[10]))*100, "%")
relative_error_interjection_1 = ' '.join([str(element) for element in relative_error_interjection_1])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ВИГУКИ 1: ", relative_error_interjection_1)
##########################################################################################################################################

############################################################### ВИБІРКА 2 ###############################################################

absolute_frequency_parts_of_speech_sample_2_values = list(absolute_frequency_parts_of_speech_sample_2.values())

relative_error_noun_2 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_2_values[0]))*100, "%")
relative_error_noun_2 = ' '.join([str(element) for element in relative_error_noun_2])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ІМЕННИКИ 2: ", relative_error_noun_2)
##########################################################################################################################################

relative_error_adjective_2 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_2_values[1]))*100, "%")
relative_error_adjective_2 = ' '.join([str(element) for element in relative_error_adjective_2])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ПРИКМЕТНИКИ 2: ", relative_error_adjective_2)
##########################################################################################################################################

relative_error_verb_2 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_2_values[2]))*100, "%")
relative_error_verb_2 = ' '.join([str(element) for element in relative_error_verb_2])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ДІЄСЛОВА 2: ", relative_error_verb_2)
##########################################################################################################################################

relative_error_gerund_2 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_2_values[3]))*100, "%")
relative_error_gerund_2 = ' '.join([str(element) for element in relative_error_gerund_2])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ДІЄПРИСЛІВНИКИ 2: ", relative_error_gerund_2)
##########################################################################################################################################

relative_error_numeral_2 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_2_values[4]))*100, "%")
relative_error_numeral_2 = ' '.join([str(element) for element in relative_error_numeral_2])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ЧИСЛІВНИКИ 2: ", relative_error_numeral_2)
##########################################################################################################################################

relative_error_adverb_2 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_2_values[5]))*100, "%")
relative_error_adverb_2 = ' '.join([str(element) for element in relative_error_adverb_2])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ПРИСЛІВНИКИ 2: ", relative_error_adverb_2)
##########################################################################################################################################

relative_error_nominative_pronoun_2 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_2_values[6]))*100, "%")
relative_error_nominative_pronoun_2 = ' '.join([str(element) for element in relative_error_nominative_pronoun_2])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ЗАЙМЕННИКИ-ІМЕННИКИ 2:", relative_error_nominative_pronoun_2)
##########################################################################################################################################

relative_error_preposition_2 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_2_values[7]))*100, "%")
relative_error_preposition_2 = ' '.join([str(element) for element in relative_error_preposition_2])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ПРИЙМЕННИКИ 2: ", relative_error_preposition_2)
##########################################################################################################################################

relative_error_conjunction_2 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_2_values[8]))*100, "%")
relative_error_conjunction_2 = ' '.join([str(element) for element in relative_error_conjunction_2])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА СПОЛУЧНИКИ 2: ", relative_error_conjunction_2)
##########################################################################################################################################

relative_error_particle_2 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_2_values[9]))*100, "%")
relative_error_particle_2 = ' '.join([str(element) for element in relative_error_particle_2])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ЧАСТКИ 2: ", relative_error_particle_2)
##########################################################################################################################################

relative_error_interjection_2 = ((1.96/math.sqrt(absolute_frequency_parts_of_speech_sample_2_values[10]))*100, "%")
relative_error_interjection_2 = ' '.join([str(element) for element in relative_error_interjection_2])
##########################################################################################################################################
# print("ВІДНОСНА ПОХИБКА ВИГУКИ 2: ", relative_error_interjection_2)
##########################################################################################################################################



##########################################################################################################################################
##########################################################################################################################################
# знаходження критерію однорідности для іменників, дієслів і сполучників
# ця формула передбачає певні операції з кожною АЧ з усіх вибірок, з яких цей критерій шукають,
# у цій роботі 40 АЧ (по 20 з кожної вибірки)
# у результаті перетворень з кожною АЧ утворюється дріб,
# тому для того, щоб було легше читати код,
# і створено 40 змінних для 40-а дробів
# тільки потім створено змінну, значенням якої є критерій однорідности
# (бачимо, що сума кількостей АЧ з 2-ох вибірок множиться на суму всіх 40-а дробів,
# від якої (тобто від суми всіх дробів), у свою чергу, віднімається 1)
# при друкуванні результату застосовується метод abs(),
# оскільки при перевірці мною роботи коду помітила,
# що часом може бути від'ємний результат
# не знаю, з чим це пов'язано, можливо це тому,
# що кількість АЧ дуже велика
##########################################################################################################################################
##########################################################################################################################################
criterion_of_uniformity_noun_fraction_1 = (variants_absolute_frequency_noun_1[0]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[0]*variants_absolute_frequency_noun_2[0])))
criterion_of_uniformity_noun_fraction_2 = (variants_absolute_frequency_noun_1[1]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[1]*variants_absolute_frequency_noun_2[1])))
criterion_of_uniformity_noun_fraction_3 = (variants_absolute_frequency_noun_1[2]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[2]*variants_absolute_frequency_noun_2[2])))
criterion_of_uniformity_noun_fraction_4 = (variants_absolute_frequency_noun_1[3]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[3]*variants_absolute_frequency_noun_2[3])))
criterion_of_uniformity_noun_fraction_5 = (variants_absolute_frequency_noun_1[4]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[4]*variants_absolute_frequency_noun_2[4])))
criterion_of_uniformity_noun_fraction_6 = (variants_absolute_frequency_noun_1[5]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[5]*variants_absolute_frequency_noun_2[5])))
criterion_of_uniformity_noun_fraction_7 = (variants_absolute_frequency_noun_1[6]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[6]*variants_absolute_frequency_noun_2[6])))
criterion_of_uniformity_noun_fraction_8 = (variants_absolute_frequency_noun_1[7]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[7]*variants_absolute_frequency_noun_2[7])))
criterion_of_uniformity_noun_fraction_9 = (variants_absolute_frequency_noun_1[8]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[8]*variants_absolute_frequency_noun_2[8])))
criterion_of_uniformity_noun_fraction_10 = (variants_absolute_frequency_noun_1[9]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[9]*variants_absolute_frequency_noun_2[9])))
criterion_of_uniformity_noun_fraction_11 = (variants_absolute_frequency_noun_1[10]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[10]*variants_absolute_frequency_noun_2[10])))
criterion_of_uniformity_noun_fraction_12 = (variants_absolute_frequency_noun_1[11]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[11]*variants_absolute_frequency_noun_2[11])))
criterion_of_uniformity_noun_fraction_13 = (variants_absolute_frequency_noun_1[12]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[12]*variants_absolute_frequency_noun_2[12])))
criterion_of_uniformity_noun_fraction_14 = (variants_absolute_frequency_noun_1[13]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[13]*variants_absolute_frequency_noun_2[13])))
criterion_of_uniformity_noun_fraction_15 = (variants_absolute_frequency_noun_1[14]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[14]*variants_absolute_frequency_noun_2[14])))
criterion_of_uniformity_noun_fraction_16 = (variants_absolute_frequency_noun_1[15]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[15]*variants_absolute_frequency_noun_2[15])))
criterion_of_uniformity_noun_fraction_17 = (variants_absolute_frequency_noun_1[16]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[16]*variants_absolute_frequency_noun_2[16])))
criterion_of_uniformity_noun_fraction_18 = (variants_absolute_frequency_noun_1[17]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[17]*variants_absolute_frequency_noun_2[17])))
criterion_of_uniformity_noun_fraction_19 = (variants_absolute_frequency_noun_1[18]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[18]*variants_absolute_frequency_noun_2[18])))
criterion_of_uniformity_noun_fraction_20 = (variants_absolute_frequency_noun_1[19]**2 / (sum(variants_absolute_frequency_noun_1)*(variants_absolute_frequency_noun_1[19]*variants_absolute_frequency_noun_2[19])))
criterion_of_uniformity_noun_fraction_21 = (variants_absolute_frequency_noun_2[0]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[0]*variants_absolute_frequency_noun_2[0])))
criterion_of_uniformity_noun_fraction_22 = (variants_absolute_frequency_noun_2[1]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[1]*variants_absolute_frequency_noun_2[1])))
criterion_of_uniformity_noun_fraction_23 = (variants_absolute_frequency_noun_2[2]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[2]*variants_absolute_frequency_noun_2[2])))
criterion_of_uniformity_noun_fraction_24 = (variants_absolute_frequency_noun_2[3]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[3]*variants_absolute_frequency_noun_2[3])))
criterion_of_uniformity_noun_fraction_25 = (variants_absolute_frequency_noun_2[4]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[4]*variants_absolute_frequency_noun_2[4])))
criterion_of_uniformity_noun_fraction_26 = (variants_absolute_frequency_noun_2[5]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[5]*variants_absolute_frequency_noun_2[5])))
criterion_of_uniformity_noun_fraction_27 = (variants_absolute_frequency_noun_2[6]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[6]*variants_absolute_frequency_noun_2[6])))
criterion_of_uniformity_noun_fraction_28 = (variants_absolute_frequency_noun_2[7]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[7]*variants_absolute_frequency_noun_2[7])))
criterion_of_uniformity_noun_fraction_29 = (variants_absolute_frequency_noun_2[8]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[8]*variants_absolute_frequency_noun_2[8])))
criterion_of_uniformity_noun_fraction_30 = (variants_absolute_frequency_noun_2[9]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[9]*variants_absolute_frequency_noun_2[9])))
criterion_of_uniformity_noun_fraction_31 = (variants_absolute_frequency_noun_2[10]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[10]*variants_absolute_frequency_noun_2[10])))
criterion_of_uniformity_noun_fraction_32 = (variants_absolute_frequency_noun_2[11]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[11]*variants_absolute_frequency_noun_2[11])))
criterion_of_uniformity_noun_fraction_33 = (variants_absolute_frequency_noun_2[12]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[12]*variants_absolute_frequency_noun_2[12])))
criterion_of_uniformity_noun_fraction_34 = (variants_absolute_frequency_noun_2[13]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[13]*variants_absolute_frequency_noun_2[13])))
criterion_of_uniformity_noun_fraction_35 = (variants_absolute_frequency_noun_2[14]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[14]*variants_absolute_frequency_noun_2[14])))
criterion_of_uniformity_noun_fraction_36 = (variants_absolute_frequency_noun_2[15]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[15]*variants_absolute_frequency_noun_2[15])))
criterion_of_uniformity_noun_fraction_37 = (variants_absolute_frequency_noun_2[16]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[16]*variants_absolute_frequency_noun_2[16])))
criterion_of_uniformity_noun_fraction_38 = (variants_absolute_frequency_noun_2[17]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[17]*variants_absolute_frequency_noun_2[17])))
criterion_of_uniformity_noun_fraction_39 = (variants_absolute_frequency_noun_2[18]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[18]*variants_absolute_frequency_noun_2[18])))
criterion_of_uniformity_noun_fraction_40 = (variants_absolute_frequency_noun_2[19]**2 / (sum(variants_absolute_frequency_noun_2)*(variants_absolute_frequency_noun_1[19]*variants_absolute_frequency_noun_2[19])))
criterion_of_uniformity_noun = (sum_ni_noun_1+sum_ni_noun_2)*((criterion_of_uniformity_noun_fraction_1 + criterion_of_uniformity_noun_fraction_2
                                                            + criterion_of_uniformity_noun_fraction_3 + criterion_of_uniformity_noun_fraction_4
                                                            + criterion_of_uniformity_noun_fraction_5 + criterion_of_uniformity_noun_fraction_6
                                                            + criterion_of_uniformity_noun_fraction_7 + criterion_of_uniformity_noun_fraction_8
                                                            + criterion_of_uniformity_noun_fraction_9 + criterion_of_uniformity_noun_fraction_10
                                                            + criterion_of_uniformity_noun_fraction_11 + criterion_of_uniformity_noun_fraction_12
                                                            + criterion_of_uniformity_noun_fraction_13 + criterion_of_uniformity_noun_fraction_14
                                                            + criterion_of_uniformity_noun_fraction_15 + criterion_of_uniformity_noun_fraction_16
                                                            + criterion_of_uniformity_noun_fraction_17 + criterion_of_uniformity_noun_fraction_18
                                                            + criterion_of_uniformity_noun_fraction_19 + criterion_of_uniformity_noun_fraction_20
                                                            + criterion_of_uniformity_noun_fraction_21 + criterion_of_uniformity_noun_fraction_22
                                                            + criterion_of_uniformity_noun_fraction_23 + criterion_of_uniformity_noun_fraction_24
                                                            + criterion_of_uniformity_noun_fraction_25 + criterion_of_uniformity_noun_fraction_26
                                                            + criterion_of_uniformity_noun_fraction_27 + criterion_of_uniformity_noun_fraction_28
                                                            + criterion_of_uniformity_noun_fraction_29 + criterion_of_uniformity_noun_fraction_30
                                                            + criterion_of_uniformity_noun_fraction_31 + criterion_of_uniformity_noun_fraction_32
                                                            + criterion_of_uniformity_noun_fraction_33 + criterion_of_uniformity_noun_fraction_34
                                                            + criterion_of_uniformity_noun_fraction_35 + criterion_of_uniformity_noun_fraction_36
                                                            + criterion_of_uniformity_noun_fraction_37 + criterion_of_uniformity_noun_fraction_38
                                                            + criterion_of_uniformity_noun_fraction_39 + criterion_of_uniformity_noun_fraction_40) - 1)
##########################################################################################################################################
# print("КРИТЕРІЙ ОДНОРІДНОСТИ ІМЕННИКИ: ", abs(criterion_of_uniformity_noun))
##########################################################################################################################################

criterion_of_uniformity_verb_fraction_1 = (variants_absolute_frequency_verb_1[0]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[0]*variants_absolute_frequency_verb_2[0])))
criterion_of_uniformity_verb_fraction_2 = (variants_absolute_frequency_verb_1[1]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[1]*variants_absolute_frequency_verb_2[1])))
criterion_of_uniformity_verb_fraction_3 = (variants_absolute_frequency_verb_1[2]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[2]*variants_absolute_frequency_verb_2[2])))
criterion_of_uniformity_verb_fraction_4 = (variants_absolute_frequency_verb_1[3]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[3]*variants_absolute_frequency_verb_2[3])))
criterion_of_uniformity_verb_fraction_5 = (variants_absolute_frequency_verb_1[4]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[4]*variants_absolute_frequency_verb_2[4])))
criterion_of_uniformity_verb_fraction_6 = (variants_absolute_frequency_verb_1[5]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[5]*variants_absolute_frequency_verb_2[5])))
criterion_of_uniformity_verb_fraction_7 = (variants_absolute_frequency_verb_1[6]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[6]*variants_absolute_frequency_verb_2[6])))
criterion_of_uniformity_verb_fraction_8 = (variants_absolute_frequency_verb_1[7]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[7]*variants_absolute_frequency_verb_2[7])))
criterion_of_uniformity_verb_fraction_9 = (variants_absolute_frequency_verb_1[8]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[8]*variants_absolute_frequency_verb_2[8])))
criterion_of_uniformity_verb_fraction_10 = (variants_absolute_frequency_verb_1[9]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[9]*variants_absolute_frequency_verb_2[9])))
criterion_of_uniformity_verb_fraction_11 = (variants_absolute_frequency_verb_1[10]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[10]*variants_absolute_frequency_verb_2[10])))
criterion_of_uniformity_verb_fraction_12 = (variants_absolute_frequency_verb_1[11]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[11]*variants_absolute_frequency_verb_2[11])))
criterion_of_uniformity_verb_fraction_13 = (variants_absolute_frequency_verb_1[12]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[12]*variants_absolute_frequency_verb_2[12])))
criterion_of_uniformity_verb_fraction_14 = (variants_absolute_frequency_verb_1[13]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[13]*variants_absolute_frequency_verb_2[13])))
criterion_of_uniformity_verb_fraction_15 = (variants_absolute_frequency_verb_1[14]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[14]*variants_absolute_frequency_verb_2[14])))
criterion_of_uniformity_verb_fraction_16 = (variants_absolute_frequency_verb_1[15]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[15]*variants_absolute_frequency_verb_2[15])))
criterion_of_uniformity_verb_fraction_17 = (variants_absolute_frequency_verb_1[16]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[16]*variants_absolute_frequency_verb_2[16])))
criterion_of_uniformity_verb_fraction_18 = (variants_absolute_frequency_verb_1[17]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[17]*variants_absolute_frequency_verb_2[17])))
criterion_of_uniformity_verb_fraction_19 = (variants_absolute_frequency_verb_1[18]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[18]*variants_absolute_frequency_verb_2[18])))
criterion_of_uniformity_verb_fraction_20 = (variants_absolute_frequency_verb_1[19]**2 / (sum(variants_absolute_frequency_verb_1)*(variants_absolute_frequency_verb_1[19]*variants_absolute_frequency_verb_2[19])))
criterion_of_uniformity_verb_fraction_21 = (variants_absolute_frequency_verb_2[0]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[0]*variants_absolute_frequency_verb_2[0])))
criterion_of_uniformity_verb_fraction_22 = (variants_absolute_frequency_verb_2[1]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[1]*variants_absolute_frequency_verb_2[1])))
criterion_of_uniformity_verb_fraction_23 = (variants_absolute_frequency_verb_2[2]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[2]*variants_absolute_frequency_verb_2[2])))
criterion_of_uniformity_verb_fraction_24 = (variants_absolute_frequency_verb_2[3]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[3]*variants_absolute_frequency_verb_2[3])))
criterion_of_uniformity_verb_fraction_25 = (variants_absolute_frequency_verb_2[4]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[4]*variants_absolute_frequency_verb_2[4])))
criterion_of_uniformity_verb_fraction_26 = (variants_absolute_frequency_verb_2[5]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[5]*variants_absolute_frequency_verb_2[5])))
criterion_of_uniformity_verb_fraction_27 = (variants_absolute_frequency_verb_2[6]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[6]*variants_absolute_frequency_verb_2[6])))
criterion_of_uniformity_verb_fraction_28 = (variants_absolute_frequency_verb_2[7]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[7]*variants_absolute_frequency_verb_2[7])))
criterion_of_uniformity_verb_fraction_29 = (variants_absolute_frequency_verb_2[8]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[8]*variants_absolute_frequency_verb_2[8])))
criterion_of_uniformity_verb_fraction_30 = (variants_absolute_frequency_verb_2[9]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[9]*variants_absolute_frequency_verb_2[9])))
criterion_of_uniformity_verb_fraction_31 = (variants_absolute_frequency_verb_2[10]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[10]*variants_absolute_frequency_verb_2[10])))
criterion_of_uniformity_verb_fraction_32 = (variants_absolute_frequency_verb_2[11]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[11]*variants_absolute_frequency_verb_2[11])))
criterion_of_uniformity_verb_fraction_33 = (variants_absolute_frequency_verb_2[12]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[12]*variants_absolute_frequency_verb_2[12])))
criterion_of_uniformity_verb_fraction_34 = (variants_absolute_frequency_verb_2[13]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[13]*variants_absolute_frequency_verb_2[13])))
criterion_of_uniformity_verb_fraction_35 = (variants_absolute_frequency_verb_2[14]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[14]*variants_absolute_frequency_verb_2[14])))
criterion_of_uniformity_verb_fraction_36 = (variants_absolute_frequency_verb_2[15]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[15]*variants_absolute_frequency_verb_2[15])))
criterion_of_uniformity_verb_fraction_37 = (variants_absolute_frequency_verb_2[16]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[16]*variants_absolute_frequency_verb_2[16])))
criterion_of_uniformity_verb_fraction_38 = (variants_absolute_frequency_verb_2[17]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[17]*variants_absolute_frequency_verb_2[17])))
criterion_of_uniformity_verb_fraction_39 = (variants_absolute_frequency_verb_2[18]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[18]*variants_absolute_frequency_verb_2[18])))
criterion_of_uniformity_verb_fraction_40 = (variants_absolute_frequency_verb_2[19]**2 / (sum(variants_absolute_frequency_verb_2)*(variants_absolute_frequency_verb_1[19]*variants_absolute_frequency_verb_2[19])))
criterion_of_uniformity_verb = (sum_ni_verb_1+sum_ni_verb_2)*((criterion_of_uniformity_verb_fraction_1 + criterion_of_uniformity_verb_fraction_2
                                                            + criterion_of_uniformity_verb_fraction_3 + criterion_of_uniformity_verb_fraction_4
                                                            + criterion_of_uniformity_verb_fraction_5 + criterion_of_uniformity_verb_fraction_6
                                                            + criterion_of_uniformity_verb_fraction_7 + criterion_of_uniformity_verb_fraction_8
                                                            + criterion_of_uniformity_verb_fraction_9 + criterion_of_uniformity_verb_fraction_10
                                                            + criterion_of_uniformity_verb_fraction_11 + criterion_of_uniformity_verb_fraction_12
                                                            + criterion_of_uniformity_verb_fraction_13 + criterion_of_uniformity_verb_fraction_14
                                                            + criterion_of_uniformity_verb_fraction_15 + criterion_of_uniformity_verb_fraction_16
                                                            + criterion_of_uniformity_verb_fraction_17 + criterion_of_uniformity_verb_fraction_18
                                                            + criterion_of_uniformity_verb_fraction_19 + criterion_of_uniformity_verb_fraction_20
                                                            + criterion_of_uniformity_verb_fraction_21 + criterion_of_uniformity_verb_fraction_22
                                                            + criterion_of_uniformity_verb_fraction_23 + criterion_of_uniformity_verb_fraction_24
                                                            + criterion_of_uniformity_verb_fraction_25 + criterion_of_uniformity_verb_fraction_26
                                                            + criterion_of_uniformity_verb_fraction_27 + criterion_of_uniformity_verb_fraction_28
                                                            + criterion_of_uniformity_verb_fraction_29 + criterion_of_uniformity_verb_fraction_30
                                                            + criterion_of_uniformity_verb_fraction_31 + criterion_of_uniformity_verb_fraction_32
                                                            + criterion_of_uniformity_verb_fraction_33 + criterion_of_uniformity_verb_fraction_34
                                                            + criterion_of_uniformity_verb_fraction_35 + criterion_of_uniformity_verb_fraction_36
                                                            + criterion_of_uniformity_verb_fraction_37 + criterion_of_uniformity_verb_fraction_38
                                                            + criterion_of_uniformity_verb_fraction_39 + criterion_of_uniformity_verb_fraction_40) - 1)
##########################################################################################################################################
# print("КРИТЕРІЙ ОДНОРІДНОСТИ ДІЄСЛОВА: ", abs(criterion_of_uniformity_verb))
##########################################################################################################################################

criterion_of_uniformity_conjunction_fraction_1 = (variants_absolute_frequency_conjunction_1[0]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[0]*variants_absolute_frequency_conjunction_2[0])))
criterion_of_uniformity_conjunction_fraction_2 = (variants_absolute_frequency_conjunction_1[1]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[1]*variants_absolute_frequency_conjunction_2[1])))
criterion_of_uniformity_conjunction_fraction_3 = (variants_absolute_frequency_conjunction_1[2]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[2]*variants_absolute_frequency_conjunction_2[2])))
criterion_of_uniformity_conjunction_fraction_4 = (variants_absolute_frequency_conjunction_1[3]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[3]*variants_absolute_frequency_conjunction_2[3])))
criterion_of_uniformity_conjunction_fraction_5 = (variants_absolute_frequency_conjunction_1[4]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[4]*variants_absolute_frequency_conjunction_2[4])))
criterion_of_uniformity_conjunction_fraction_6 = (variants_absolute_frequency_conjunction_1[5]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[5]*variants_absolute_frequency_conjunction_2[5])))
criterion_of_uniformity_conjunction_fraction_7 = (variants_absolute_frequency_conjunction_1[6]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[6]*variants_absolute_frequency_conjunction_2[6])))
criterion_of_uniformity_conjunction_fraction_8 = (variants_absolute_frequency_conjunction_1[7]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[7]*variants_absolute_frequency_conjunction_2[7])))
criterion_of_uniformity_conjunction_fraction_9 = (variants_absolute_frequency_conjunction_1[8]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[8]*variants_absolute_frequency_conjunction_2[8])))
criterion_of_uniformity_conjunction_fraction_10 = (variants_absolute_frequency_conjunction_1[9]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[9]*variants_absolute_frequency_conjunction_2[9])))
criterion_of_uniformity_conjunction_fraction_11 = (variants_absolute_frequency_conjunction_1[10]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[10]*variants_absolute_frequency_conjunction_2[10])))
criterion_of_uniformity_conjunction_fraction_12 = (variants_absolute_frequency_conjunction_1[11]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[11]*variants_absolute_frequency_conjunction_2[11])))
criterion_of_uniformity_conjunction_fraction_13 = (variants_absolute_frequency_conjunction_1[12]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[12]*variants_absolute_frequency_conjunction_2[12])))
criterion_of_uniformity_conjunction_fraction_14 = (variants_absolute_frequency_conjunction_1[13]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[13]*variants_absolute_frequency_conjunction_2[13])))
criterion_of_uniformity_conjunction_fraction_15 = (variants_absolute_frequency_conjunction_1[14]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[14]*variants_absolute_frequency_conjunction_2[14])))
criterion_of_uniformity_conjunction_fraction_16 = (variants_absolute_frequency_conjunction_1[15]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[15]*variants_absolute_frequency_conjunction_2[15])))
criterion_of_uniformity_conjunction_fraction_17 = (variants_absolute_frequency_conjunction_1[16]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[16]*variants_absolute_frequency_conjunction_2[16])))
criterion_of_uniformity_conjunction_fraction_18 = (variants_absolute_frequency_conjunction_1[17]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[17]*variants_absolute_frequency_conjunction_2[17])))
criterion_of_uniformity_conjunction_fraction_19 = (variants_absolute_frequency_conjunction_1[18]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[18]*variants_absolute_frequency_conjunction_2[18])))
criterion_of_uniformity_conjunction_fraction_20 = (variants_absolute_frequency_conjunction_1[19]**2 / (sum(variants_absolute_frequency_conjunction_1)*(variants_absolute_frequency_conjunction_1[19]*variants_absolute_frequency_conjunction_2[19])))
criterion_of_uniformity_conjunction_fraction_21 = (variants_absolute_frequency_conjunction_2[0]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[0]*variants_absolute_frequency_conjunction_2[0])))
criterion_of_uniformity_conjunction_fraction_22 = (variants_absolute_frequency_conjunction_2[1]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[1]*variants_absolute_frequency_conjunction_2[1])))
criterion_of_uniformity_conjunction_fraction_23 = (variants_absolute_frequency_conjunction_2[2]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[2]*variants_absolute_frequency_conjunction_2[2])))
criterion_of_uniformity_conjunction_fraction_24 = (variants_absolute_frequency_conjunction_2[3]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[3]*variants_absolute_frequency_conjunction_2[3])))
criterion_of_uniformity_conjunction_fraction_25 = (variants_absolute_frequency_conjunction_2[4]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[4]*variants_absolute_frequency_conjunction_2[4])))
criterion_of_uniformity_conjunction_fraction_26 = (variants_absolute_frequency_conjunction_2[5]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[5]*variants_absolute_frequency_conjunction_2[5])))
criterion_of_uniformity_conjunction_fraction_27 = (variants_absolute_frequency_conjunction_2[6]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[6]*variants_absolute_frequency_conjunction_2[6])))
criterion_of_uniformity_conjunction_fraction_28 = (variants_absolute_frequency_conjunction_2[7]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[7]*variants_absolute_frequency_conjunction_2[7])))
criterion_of_uniformity_conjunction_fraction_29 = (variants_absolute_frequency_conjunction_2[8]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[8]*variants_absolute_frequency_conjunction_2[8])))
criterion_of_uniformity_conjunction_fraction_30 = (variants_absolute_frequency_conjunction_2[9]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[9]*variants_absolute_frequency_conjunction_2[9])))
criterion_of_uniformity_conjunction_fraction_31 = (variants_absolute_frequency_conjunction_2[10]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[10]*variants_absolute_frequency_conjunction_2[10])))
criterion_of_uniformity_conjunction_fraction_32 = (variants_absolute_frequency_conjunction_2[11]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[11]*variants_absolute_frequency_conjunction_2[11])))
criterion_of_uniformity_conjunction_fraction_33 = (variants_absolute_frequency_conjunction_2[12]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[12]*variants_absolute_frequency_conjunction_2[12])))
criterion_of_uniformity_conjunction_fraction_34 = (variants_absolute_frequency_conjunction_2[13]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[13]*variants_absolute_frequency_conjunction_2[13])))
criterion_of_uniformity_conjunction_fraction_35 = (variants_absolute_frequency_conjunction_2[14]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[14]*variants_absolute_frequency_conjunction_2[14])))
criterion_of_uniformity_conjunction_fraction_36 = (variants_absolute_frequency_conjunction_2[15]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[15]*variants_absolute_frequency_conjunction_2[15])))
criterion_of_uniformity_conjunction_fraction_37 = (variants_absolute_frequency_conjunction_2[16]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[16]*variants_absolute_frequency_conjunction_2[16])))
criterion_of_uniformity_conjunction_fraction_38 = (variants_absolute_frequency_conjunction_2[17]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[17]*variants_absolute_frequency_conjunction_2[17])))
criterion_of_uniformity_conjunction_fraction_39 = (variants_absolute_frequency_conjunction_2[18]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[18]*variants_absolute_frequency_conjunction_2[18])))
criterion_of_uniformity_conjunction_fraction_40 = (variants_absolute_frequency_conjunction_2[19]**2 / (sum(variants_absolute_frequency_conjunction_2)*(variants_absolute_frequency_conjunction_1[19]*variants_absolute_frequency_conjunction_2[19])))
criterion_of_uniformity_conjunction = (sum_ni_conjunction_1+sum_ni_conjunction_2)*((criterion_of_uniformity_conjunction_fraction_1 + criterion_of_uniformity_conjunction_fraction_2
                                                            + criterion_of_uniformity_conjunction_fraction_3 + criterion_of_uniformity_conjunction_fraction_4
                                                            + criterion_of_uniformity_conjunction_fraction_5 + criterion_of_uniformity_conjunction_fraction_6
                                                            + criterion_of_uniformity_conjunction_fraction_7 + criterion_of_uniformity_conjunction_fraction_8
                                                            + criterion_of_uniformity_conjunction_fraction_9 + criterion_of_uniformity_conjunction_fraction_10
                                                            + criterion_of_uniformity_conjunction_fraction_11 + criterion_of_uniformity_conjunction_fraction_12
                                                            + criterion_of_uniformity_conjunction_fraction_13 + criterion_of_uniformity_conjunction_fraction_14
                                                            + criterion_of_uniformity_conjunction_fraction_15 + criterion_of_uniformity_conjunction_fraction_16
                                                            + criterion_of_uniformity_conjunction_fraction_17 + criterion_of_uniformity_conjunction_fraction_18
                                                            + criterion_of_uniformity_conjunction_fraction_19 + criterion_of_uniformity_conjunction_fraction_20
                                                            + criterion_of_uniformity_conjunction_fraction_21 + criterion_of_uniformity_conjunction_fraction_22
                                                            + criterion_of_uniformity_conjunction_fraction_23 + criterion_of_uniformity_conjunction_fraction_24
                                                            + criterion_of_uniformity_conjunction_fraction_25 + criterion_of_uniformity_conjunction_fraction_26
                                                            + criterion_of_uniformity_conjunction_fraction_27 + criterion_of_uniformity_conjunction_fraction_28
                                                            + criterion_of_uniformity_conjunction_fraction_29 + criterion_of_uniformity_conjunction_fraction_30
                                                            + criterion_of_uniformity_conjunction_fraction_31 + criterion_of_uniformity_conjunction_fraction_32
                                                            + criterion_of_uniformity_conjunction_fraction_33 + criterion_of_uniformity_conjunction_fraction_34
                                                            + criterion_of_uniformity_conjunction_fraction_35 + criterion_of_uniformity_conjunction_fraction_36
                                                            + criterion_of_uniformity_conjunction_fraction_37 + criterion_of_uniformity_conjunction_fraction_38
                                                            + criterion_of_uniformity_conjunction_fraction_39 + criterion_of_uniformity_conjunction_fraction_40) - 1)
##########################################################################################################################################
# print("КРИТЕРІЙ ОДНОРІДНОСТИ СПОЛУЧНИКИ: ", abs(criterion_of_uniformity_conjunction))
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# знаходження критерію Стьюдента для прикметника, прислівника та прийменника
# щоб не писати дуже довгу формулу в один рядок,
# створено змінну для чисельника дробу
# а оскільки у знаменнику дробу ще два дроби,
# з яикх треба знайти квадратний корінь,
# то для чисельників і знаменників цих дробів
# також створено окремі змінні
# після вирахування чисельників і знаменників дробів із знаменника
# для дробів із знаменника створено змінні,
# значеннями яких є чисельники, поділені на знаменники,
# і тільки потім створено змінну для знаменника дробу,
# значенням якої є корінь квадратний з добутку першого дроба зі знаменника на другий дріб зі знаменника
# застосовано знайомий метод sqrt() з модуля math для знаходження квадратного кореня,
# а також метод abs(), який знаходить модуль числа
# (за формулою критерію Стьюдента з чисельника потрібно знайти модуль)
##########################################################################################################################################
##########################################################################################################################################
numerator_t_student_criterion_adjective = abs(medium_x_adjective_1 - medium_x_adjective_2)
denominator_numerator_t_student_criterion_fraction_1_adjective = sum_xi_minus_medium_x_power_two_multiply_ni_adjective_1 + sum_xi_minus_medium_x_power_two_multiply_ni_adjective_2
denominator_denominator_t_student_criterion_fraction_1_adjective = sum_ni_adjective_1 + sum_ni_adjective_2 - 2
denominator_numerator_t_student_criterion_fraction_2_adjective = sum_ni_adjective_1 + sum_ni_adjective_2
denominator_denominator_t_student_criterion_fraction_2_adjective = sum_ni_adjective_1 * sum_ni_adjective_2
denominator_t_student_criterion_fraction_1_adjective = denominator_numerator_t_student_criterion_fraction_1_adjective / denominator_denominator_t_student_criterion_fraction_1_adjective
denominator_t_student_criterion_fraction_2_adjective = denominator_numerator_t_student_criterion_fraction_2_adjective / denominator_denominator_t_student_criterion_fraction_2_adjective
denominator_t_student_criterion_adjective = math.sqrt(denominator_t_student_criterion_fraction_1_adjective * denominator_t_student_criterion_fraction_2_adjective)
t_student_criterion_adjective = numerator_t_student_criterion_adjective / denominator_t_student_criterion_adjective

##########################################################################################################################################
# print("КРИТЕРІЙ СТЬЮДЕНТА ПРИКМЕТНИКИ: ", t_student_criterion_adjective)
##########################################################################################################################################

numerator_t_student_criterion_adverb = abs(medium_x_adverb_1 - medium_x_adverb_2)
denominator_numerator_t_student_criterion_fraction_1_adverb = sum_xi_minus_medium_x_power_two_multiply_ni_adverb_1 + sum_xi_minus_medium_x_power_two_multiply_ni_adverb_2
denominator_denominator_t_student_criterion_fraction_1_adverb = sum_ni_adverb_1 + sum_ni_adverb_2 - 2
denominator_numerator_t_student_criterion_fraction_2_adverb = sum_ni_adverb_1 + sum_ni_adverb_2
denominator_denominator_t_student_criterion_fraction_2_adverb = sum_ni_adverb_1 * sum_ni_adverb_2
denominator_t_student_criterion_fraction_1_adverb = denominator_numerator_t_student_criterion_fraction_1_adverb / denominator_denominator_t_student_criterion_fraction_1_adverb
denominator_t_student_criterion_fraction_2_adverb = denominator_numerator_t_student_criterion_fraction_2_adverb / denominator_denominator_t_student_criterion_fraction_2_adverb
denominator_t_student_criterion_adverb = math.sqrt(denominator_t_student_criterion_fraction_1_adverb * denominator_t_student_criterion_fraction_2_adverb)
t_student_criterion_adverb = numerator_t_student_criterion_adverb / denominator_t_student_criterion_adverb

##########################################################################################################################################
# print("КРИТЕРІЙ СТЬЮДЕНТА ПРИСЛІВНИКИ: ", t_student_criterion_adverb)
##########################################################################################################################################

numerator_t_student_criterion_preposition = abs(medium_x_preposition_1 - medium_x_preposition_2)
denominator_numerator_t_student_criterion_fraction_1_preposition = sum_xi_minus_medium_x_power_two_multiply_ni_preposition_1 + sum_xi_minus_medium_x_power_two_multiply_ni_preposition_2
denominator_denominator_t_student_criterion_fraction_1_preposition = sum_ni_preposition_1 + sum_ni_preposition_2 - 2
denominator_numerator_t_student_criterion_fraction_2_preposition = sum_ni_preposition_1 + sum_ni_preposition_2
denominator_denominator_t_student_criterion_fraction_2_preposition = sum_ni_preposition_1 * sum_ni_preposition_2
denominator_t_student_criterion_fraction_1_preposition = denominator_numerator_t_student_criterion_fraction_1_preposition / denominator_denominator_t_student_criterion_fraction_1_preposition
denominator_t_student_criterion_fraction_2_preposition = denominator_numerator_t_student_criterion_fraction_2_preposition / denominator_denominator_t_student_criterion_fraction_2_preposition
denominator_t_student_criterion_preposition = math.sqrt(denominator_t_student_criterion_fraction_1_preposition * denominator_t_student_criterion_fraction_2_preposition)
t_student_criterion_preposition = numerator_t_student_criterion_preposition / denominator_t_student_criterion_preposition

##########################################################################################################################################
# print("КРИТЕРІЙ СТЬЮДЕНТА ПРИЙМЕННИКИ: ", t_student_criterion_preposition)
##########################################################################################################################################

##########################################################################################################################################
##########################################################################################################################################
# утворення рядків для додавання в таблицю бази даних (БД)
# оскільки для кожної вибірки буде по одній таблиці
# зі словоформою, АЧ словоформи у всій вибірці, її початковою формою, АЧ початкової форми та частиномовним тегом
# (ідеться про назви колонок),
# то потрібно зібрати всі ці дані в певний вигляд,
# щоб додати їх у таблицю
# у таблиці БД зручно додавати список кортежів (list of tuples),
# де кортеж є одним з елементів списку і, відповідно, одним рядком
# для реалізації цього потрібно згадати, що всі словоформи
# є у змінних text_ready_to_work_as_a_word_list_1 та text_ready_to_work_as_a_word_list_2,
# які є списками словоформ
# потрібно ще по 4 списки на кожну вибірку
# (з АЧ словоформ, з початковими формами словоформ, з АЧ початкових форм і з частиномовними тегами)
# для створення списку АЧ словоформ потрібно створити порожній список, куди буде додано АЧ,
# порожній словник, де ключами будуть словоформи, а значеннями -- частоти словоформ,
# потім написати цикл, який проходиться по кожній словоформі
# (пам'ятаємо, що всі словоформи у змінних text_ready_to_work_as_a_word_list_1 i text_ready_to_work_as_a_word_list_2)
# і за допомогою методу get () рахує частоту появи словоформи у списку словоформ
# результатом роботи циклу є частотний словник
# після цього пишемо ще один цикл, який проходиться по значеннях частотного словника
# і додає їх у створений раніше порожній список
# !!!УВАГА!!! важливо, щоб словоформи і частоти збігалися, тому
# на цьому моменті розуміємо, що краще перестрахуватись
# і написати порожній список для словоформ,
# потім цикл, який проходиться по ключах частотного словника
# і додає їх у порожній список
# !!!УВАГА!!! ось тепер ми точно впевнені,
# що перший елемент списку словоформ відповідає першому елементу списку частот,
# другий -- другому, третій -- третьому і т.д.
# переходимо до початкових форм словоформ і їхніх частот
# тут така сама логіка, як у ситуації зі словоформами і їхніми частотами
# для створення списку початкових форм словоформ потрібно
# створити змінну, значенням якої є порожній список,
# потім написати цикл, який проходиться по кожному елементу у списку словоформ,
# здійснює парсинг кожної словоформи,
# далі проходиться по списку, який є результатом парсингу
# (те, що я раніше писала про результат парсингу в pymorphy2,
# який дає на вихід список, елементами якого є різні ознаки словоформи),
# створює змінну, значенням якої є початкові форми,
# а потім додає кожну початкову форму в порожній список, створений раніше
# стосовно частиномовних тегів,
# також створюємо порожній список,
# пишемо цикл, який проходиться по кожній словоформі,
# проводить парсинг тільки першого елемента
# (можлива ситуація, коли pymorphy2 не знає, що за слово перед ним
# (наприклад, "його" -- це "йога", "йог", "він" або "воно"?),
# тоді просимо програму взяти до уваги частиномовний тег лише першого варіянта,
# який пропонує pymorphy2 (на жаль, це не завжди дає правильний тег,
# який справді відповідає змісту тексту, але поки я не знаю, як автоматично це поправити))
# і до порожнього списку методом append() додає частиномовний тег
# на цьому моменті маємо 5 списків, що відповідають 5-ом колонкам у майбутній таблиці,
# значить, можемо утворити список кортежів
# шляхом створення змінної, значенням якої буде цей список,
# у цьому ж рядку застосовуємо метод list (), який перетворює те, що в дужках, на список,
# і метод zip (), у якого в дужках 5 назв наших списків
# (цей метод бачить, що потрібно поєднати елементи списків саме в кортежі)
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

word_forms_1 = []
absolute_frequency_word_forms_1 = []
frequency_word_forms_1_dict = {}
for i in text_ready_to_work_as_a_word_list_1:
    frequency_word_forms_1_dict[i] = frequency_word_forms_1_dict.get(i, 0) + 1
for key in frequency_word_forms_1_dict.keys():
    word_forms_1.append(key)
for value in frequency_word_forms_1_dict.values():
    absolute_frequency_word_forms_1.append(value)

lexemes_1 = []
for item in word_forms_1:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    lexemes_1.append(lemma_variable)

absolute_frequency_lexemes_1 = []
frequency_lexemes_1_dict = {}
for i in lexemes_1:
    frequency_lexemes_1_dict[i] = frequency_lexemes_1_dict.get(i, 0) + 1
for value in frequency_lexemes_1_dict.values():
    absolute_frequency_lexemes_1.append(value)

pos_1 = []
for item in text_ready_to_work_as_a_word_list_1:
    language_variable = morph.parse(item)[0]
    pos_1.append(language_variable.tag.POS)

rows_word_forms_and_lexemes_usage_1 = list(zip(word_forms_1, absolute_frequency_word_forms_1, lexemes_1, absolute_frequency_lexemes_1, pos_1))
# print(rows_word_forms_and_lexemes_usage_1)

############################################################### ВИБІРКА 2 ###############################################################

word_forms_2 = []
absolute_frequency_word_forms_2 = []
frequency_word_forms_2_dict = {}
for i in text_ready_to_work_as_a_word_list_2:
    frequency_word_forms_2_dict[i] = frequency_word_forms_2_dict.get(i, 0) + 1
for key in frequency_word_forms_2_dict.keys():
    word_forms_2.append(key)
for value in frequency_word_forms_2_dict.values():
    absolute_frequency_word_forms_2.append(value)

lexemes_2 = []
for item in word_forms_2:
    language_variable = morph.parse(item)
    for element in language_variable:
        lemma_variable = element.normal_form
    lexemes_2.append(lemma_variable)

absolute_frequency_lexemes_2 = []
frequency_lexemes_2_dict = {}
for i in lexemes_2:
    frequency_lexemes_2_dict[i] = frequency_lexemes_2_dict.get(i, 0) + 1
for value in frequency_lexemes_2_dict.values():
    absolute_frequency_lexemes_2.append(value)

pos_2 = []
for item in text_ready_to_work_as_a_word_list_2:
    language_variable = morph.parse(item)[0]
    pos_2.append(language_variable.tag.POS)

rows_word_forms_and_lexemes_usage_2 = list(zip(word_forms_2, absolute_frequency_word_forms_2, lexemes_2, absolute_frequency_lexemes_2, pos_2))
# print(rows_word_forms_and_lexemes_usage_2)

##########################################################################################################################################
##########################################################################################################################################
# з'єднання з базою даних
# потрібно дати назву цьому з'єднанню
# (тут QuantitativeLinguisticsSAMPLE1.db і QuantitativeLinguisticsSAMPLE2.db)
# також можна зробити cursor, який буде робити те, що потрібно
# далі потрібно створити таблиці
# створюємо змінну, значенням, якої буде команда, яку виконає cursor
# команда записується в лапках,
# для створення таблиці пишемо службове слово CREATE TABLE IF NOT EXIST *назва таблиці*
# ця команда створює таблицю, якщо її ще немає,
# після назви таблиці в дужках пишемо назви колонок,
# після яких тут же вказуємо тип даних, який має бути в цій колонці,
# бачимо колонки під назвами Word_form (TEXT), Absolute_frequency_word_forms (INTEGER),
# Lexeme (TEXT), Absolute_frequency_lexemes (INTEGER), POS (TEXT)
# слово TEXT означає, що в колонці мають бути текстові дані,
# а слово INTEGER лзначає, що в колонці мають бути цілі числа
# !!!УВАГА!!! назви колонок відповідають назвам списків, які ми робили перед тим,
# тобто в колонках будуть словоформи, АЧ словоформ, лексеми, АЧ лексем, частиномовні теги
# команда cursor.execute(*назва команди*) виконує команду створення таблиці
# на цьому моменті таблиця існує, але вона порожня
# для наповнення її потрібна команда додавання рядків
# ця команда виглядає так: змінна, значенням якої є назва команди в лапках
# для додавання рядків у тексті команди пишемо INSERT INTO *назва таблиці*
# VALUES (*знаки питання (знаків питання стільки, скільки колонок у таблиці, тут їх п'ять*))
# знову виконаємо цю команду за допомогою cursor
# пишемо cursor.executemany(*назва команди*, *змінна, значенням якої є список кортежів (1 кортеж = 1 рядок*)
# наостанок потрібно прописати цикл, який проходиться по кожному рядку
# у таблиці (дивиться кожен рядок і запобігає додаванню однакових рядків)
# усе, описане тут, відбувається з обома вибірками
# бачимо, що способи створення таблиць трохи різні
# у першому випадку 1) створення змінної, значенням якої є назва команди
# --> 2) виконання команди за допомогою курсора
# у другому випадку 1) виконання команди за допомогою курсора
# (сама назва команди в дужках)
# іще одне, чому при виконанні курсором команд різні методи (execute, executemany),
# так це тому, що перший заастосовується до створення ОДНІЄЇ таблиці,
# а другий -- для додавання БАГАТЬОХ рядків у таблицю
# (у прикладах, які знайшла в Інтернеті, багато рядків можна було вставити
# і за допомогою просто execute, але в моєму коді це не пішло)
# оскільки кожна таблиця стосується різних connection,
# то щоразу, після виконання дій з таблицею,
# потрібно писати connection.commit() і connection.close()
# (перше виконує все, що ми зробили після підключення до бази даних,
# а друге перериває зв'язок з базою даних
# після завершення всіх запланованих операцій)
##########################################################################################################################################
##########################################################################################################################################

############################################################### ВИБІРКА 1 ###############################################################

# connection = sqlite3.connect('QuantitativeLinguisticsSAMPLE1.db')
# cursor = connection.cursor()

# creation_of_table_sample_1_word_forms_lexemes_pos = """CREATE TABLE IF NOT EXISTS Sample_1_word_forms_and_lexemes_usage (
#                                                     Word_form TEXT,
#                                                     Absolute_frequency_word_forms INTEGER,
#                                                     Lexeme TEXT,
#                                                     Absolute_frequency_lexemes INTEGER,
#                                                     POS TEXT
#                                                     )"""
# cursor.execute(creation_of_table_sample_1_word_forms_lexemes_pos)
# inserting_rows_to_table_sample_1_word_forms_lexemes_pos = """INSERT INTO Sample_1_word_forms_and_lexemes_usage
#                                                           VALUES (?, ?, ?, ?, ?)"""
# cursor.executemany(inserting_rows_to_table_sample_1_word_forms_lexemes_pos, rows_word_forms_and_lexemes_usage_1)
# for row in cursor.execute("""SELECT * FROM Sample_1_word_forms_and_lexemes_usage"""):
#     print(row)

# connection.commit()
# connection.close()

# ############################################################### ВИБІРКА 2 ###############################################################

# connection = sqlite3.connect('QuantitativeLinguisticsSAMPLE2.db')
# cursor = connection.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS Sample_2_word_forms_and_lexemes_usage (
#                                                     Word_form TEXT,
#                                                     Absolute_frequency_word_forms INTEGER,
#                                                     Lexeme TEXT,
#                                                     Absolute_frequency_lexemes INTEGER,
#                                                     POS TEXT
#                                                     )""")
# inserting_rows_to_table_sample_2_word_forms_lexemes_pos = """INSERT INTO Sample_2_word_forms_and_lexemes_usage
#                                                           VALUES (?, ?, ?, ?, ?)"""
# cursor.executemany(inserting_rows_to_table_sample_2_word_forms_lexemes_pos, rows_word_forms_and_lexemes_usage_2)
# for row in cursor.execute("""SELECT * FROM Sample_2_word_forms_and_lexemes_usage"""):
#     print(row)

# connection.commit()
# connection.close()

##########################################################################################################################################
##########################################################################################################################################
# закриваємо файли, з якими працювали
##########################################################################################################################################
##########################################################################################################################################
file_1.close()
file_2.close()
