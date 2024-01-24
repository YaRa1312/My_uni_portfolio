print("Плешивцева Ірина, Прикладна лінгвістика, Лабораторна робота №2")


import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn


import operator
from operator import itemgetter


animal = wn.synset('animal.n.01')
mammal = wn.synset('mammal.n.01')


for synset in wn.synsets('animal', wn.NOUN):
  print("Завдання 2 (1): " + synset.name() + ':', synset.definition())
for synset in wn.synsets('mammal', wn.NOUN):
  print("Завдання 2 (2): " + synset.name() + ':', synset.definition())


print("Завдання 3 (1.1): ", animal.hyponyms())
print("Завдання 3 (1.2): ", mammal.hyponyms())
print("Завдання 3 (2.1): ", animal.hypernyms())
print("Завдання 3 (2.2): ", mammal.hypernyms())


print("Завдання 4: ", wn.synset('animal.n.01').lowest_common_hypernyms(wn.synset('mammal.n.01')))


print("Завдання 5 (1): ", animal.path_similarity(mammal))
print("Завдання 5 (2): ", animal.wup_similarity(mammal))
print("Завдання 5 (3): ", animal.lch_similarity(mammal))


def levenshtein (s1, s2):
  d = {}
  s1_length = len(s1)
  s2_length = len(s2)
  for i in range(-1, s1_length + 1):
    d[(i, -1)] = i + 1
  for j in range(-1, s2_length + 1):
    d[(-1, j)] = j + 1
  
  for i in range(s1_length):
    for j in range(s2_length):
      if s1[i] == s2[j]:
        cost = 0
      else:
        cost = 1
      d[(i, j)] = min(
          d[(i - 1, j)] + 1,
          d[(i, j - 1)] + 1,
          d[(i - 1, j - 1)] + cost,
      )
  return d[s1_length - 1, s2_length - 1]


word1 = 'animal'
word2 = 'mammal'
d1 = levenshtein(word1, word2)
print("Завдання 6: ", f"Result for '{word1}' & '{word2}': ", d1)


def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1


    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                            d[(i-1,j)] + 1, # deletion
                            d[(i,j-1)] + 1, # insertion
                            d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost)
    return d[lenstr1-1,lenstr2-1]


d2 = damerau_levenshtein_distance(word1, word2)
print("Завдання 7: ", f"Result for '{word1}' & '{word2}': ", d2)


def dict_distance(word, num_words):
  file = open(r'1-1000.txt', 'r')
  lines = file.readlines()
  file.close()


  distances = {}
  for line in lines:
    word_distance = levenshtein(word,line.strip())
    distances[line.strip()] = word_distance
  sorted_dict = sorted(distances.items(), key = itemgetter(1))


  closest_words = []
  for i in range(num_words):
    closest_words.append(sorted_dict[i])
  return closest_words


word = input("Введіть довільне слово англійською мовою: ")
print("Завдання 8: ", word, ": ", dict_distance(word, 8))


f1 = open("chesterton-thursday.txt", "r")
word_dict = dict()
f1.close()


with open("chesterton-thursday.txt",'r') as f:
    for line in f:
        for word in line.split():
            word = word.lower()
            for el in '.,"-?!;:[]':
                word = word.replace(el, "")
            #print(word)
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1


    sorted_word_dict = dict(sorted(word_dict.items(), key=operator.itemgetter(1),reverse=True))
    with open("highscore.txt", 'w') as f:
        for key, value in sorted_word_dict.items():
            f.write('%s\n' % (key))
        f.close()


def dict_dist(word, num_words):
  file = open(r'highscore.txt', 'r')
  lines = file.readlines()
  file.close()


  distances = {}
  for line in lines:
    word_distance = levenshtein(word,line.strip())
    distances[line.strip()] = word_distance
  sorted_dict = sorted(distances.items(), key = itemgetter(1))


  closest_words = []
  for i in range(num_words):
    closest_words.append(sorted_dict[i])
  return closest_words


word = input("Введіть довільне слово англійською мовою: ")
print("Завдання 9: ", word, ": ", dict_dist(word, 8))
