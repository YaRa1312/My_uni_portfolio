import pymorphy2

file = open("C:\\project\\ira+vira\\danilov\\old\\sep_23.1.txt", "r", encoding="utf-8")
content = file.read()
file.close()

punctuations = '''.,<>?/~`!@'#№$"%^&*()_–+=:;/][}{'''

content_without_punctuation = ""

for char in content:
    if char not in punctuations:
        content_without_punctuation = content_without_punctuation + char

content_without_punctuation_lowered = content_without_punctuation.lower()

content_without_punctuation_lowered_as_a_list = content_without_punctuation_lowered.split()

vocabulary_of_inclusion_adverbs = ["разом", "спільно", "гуртом", "заодно", "згуртовано", "спільними зусиллями"]
vocabulary_of_we = ["ми", "нас", "нам", "нами"]

index_of_inclusion_adverbs = 0
index_of_inclusion_we = 0

for i in content_without_punctuation_lowered_as_a_list:
    if i in vocabulary_of_inclusion_adverbs:
        index_of_inclusion_adverbs += 1
    elif i in vocabulary_of_we:
        index_of_inclusion_we += 1

morph = pymorphy2.MorphAnalyzer(lang="uk")

for item in content_without_punctuation_lowered_as_a_list:
    language_variable = morph.parse(item)
    for elem in language_variable:
        if elem.tag.POS == "VERB":
            if elem.word[-3:] == "имо" or elem.word[-3:] == "їмо" or elem.word[-3:] == "емо" or elem.word[-3:] == "ємо":
                index_of_inclusion_we += 1

print(f"""{{"Індекс інклюзивности (прислівники)": {index_of_inclusion_adverbs}, "Індекс інклюзивности (ми)": {index_of_inclusion_we}}}""")
