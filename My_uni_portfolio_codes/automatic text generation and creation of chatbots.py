print("Плешивцева Ірина, Прикладна лінгвістика, Лабораторна робота №3")
!pip install chatterbot
!pip install chatterbot_corpus
import nltk
import random
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import chatterbot_corpus
from collections import defaultdict


def markov_chain(text):
  words = text.split(' ')
  my_dict = defaultdict(list)
  for current_word, next_word in zip(words[0:-1], words[1:]):
    my_dict[current_word].append(next_word)
  my_dict = dict(my_dict)
  return my_dict


test_text = input("Enter a text in English: ")
test_dict = markov_chain(test_text)
for word in test_dict:
  print(word, test_dict[word])


def generate_sentence(chain, word_count):
  cur_word = random.choice(list(chain.keys()))
  sentence = cur_word.capitalize()
  for i in range(word_count-1):
    next_word = random.choice(chain[cur_word])
    sentence += " " + next_word
    cur_word = next_word
  sentence += "."
  return sentence


print(generate_sentence(test_dict, 19))


f = open("chesterton-thursday.txt", "r")
test_text_0 = f.read()
new_dict = dict()
f.close()


with open("chesterton-thursday.txt",'r') as f:
  for word in f:
    words = word.splitlines()
    def markov_chain(text):
      words = text.split(' ')
      my_dict = defaultdict(list)
      for current_word, next_word in zip(words[0:-1], words[1:]):
        my_dict[current_word].append(next_word)
      my_dict = dict(my_dict)
      return my_dict


new_dict = markov_chain(test_text_0)
for word in new_dict:
  print(word, new_dict[word])


  def generate_sentence(chain, word_count):
    cur_word = random.choice(list(chain.keys()))
    sentence = cur_word.capitalize()
    for i in range(word_count-1):
      next_word = random.choice(chain[cur_word])
      sentence += " " + next_word
      cur_word = next_word
    sentence += "."
    return sentence


print(generate_sentence(new_dict, 18))


my_bot = ChatBot(name="PyBot", read_only = True,\
logic_adapters = ["chatterbot.logic.MathematicalEvaluation",\
                  "chatterbot.logic.BestMatch"])


small_talk = ["Hi there!",
              "Hi",
              "Hello",
              "How do you do?",
              "How are you?",
              "I'm cool",
              "Fine, and you?",
              "Always cool",
              "I'm OK",
              "Glad to hear that",
              "I feel awesome",
              "Excellent, glad to hear that",
              "Not so good",
              "Sorry to hear that",
              "What's your name?",
              "I'm PyBot. Ask me a math question, please"
              ]


math_talk_1 = ["Pythagorean theorem",
               "a^2 + b^2 = c^2"]


math_talk_2 = ["Law of cosines",
               "c^2 = a^2 + b^2 - 2*a*b*cos(gamma)"]


list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk_1, math_talk_2):
  list_trainer.train(item)


name=input("Enter Your Name: ")
while True:
    request=input(name+':')
    if request=='Bye' or request=="Good bye":
        print('PyBot: Bye')
        break
    else:
        response=my_bot.get_response(request)
        print('PyBot:',response)


#код для шведськомовного бота, але тут я навчаю його сама, а не він навчається на основі вже вбудованого корпусу; цей уривок якраз і працює
exotisk_bot = ChatBot(name="SvenskaBot", read_only = True,\
logic_adapters = ["chatterbot.logic.MathematicalEvaluation",\
                  "chatterbot.logic.BestMatch"])


small_talk = ["Hallå där",
              "Hej",
              "Hallå!",
              "Hur mår du?",
              "Hur går det?",
              "Jag är cool",
              "Bra och du?",
              "Alltid cool",
              "Jag är okej",
              "Glad att höra det",
              "Jag känner mig fantastisk",
              "Utmärkt, kul att höra det",
              "Inte så bra",
              "Jag beklagarJag beklagar",
              "Vad heter du?",
              "Jag är SvenskaBot. Ställ en matematisk fråga till mig, tack"
              ]


math_talk_1 = ["Pythagoras sats",
               "a^2 + b^2 = c^2"]


math_talk_2 = ["Cosinuslagen",
               "c^2 = a^2 + b^2 - 2*a*b*cos(gamma)"]


list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk_1, math_talk_2):
  list_trainer.train(item)


name=input("Ange ditt namn: ")
while True:
    request=input(name+':')
    if request=='Hejdå' or request=="Adjö":
        print('SvenskaBot: Hejdå')
        break
    else:
        response=my_bot.get_response(request)
        print('SvenskaBot:',response)




#цей уривок коду мав би навчити бот розуміти шведську і відповідати шведською, але попри це він часом відповідає англійською
exotisk_bot = ChatBot("SvenskaBot")
corpus_trainer_0 = ChatterBotCorpusTrainer(exotisk_bot)
corpus_trainer_0.train('chatterbot.corpus.swedish.ai',
                       'chatterbot.corpus.swedish.food',
                       'chatterbot.corpus.swedish.greetings',
                       'chatterbot.corpus.swedish.sports')
user_name = input("Ange ditt namn: ")
print("Hej! jag är en SvenskaBot")
while True:
  user_input = input(user_name + ": ")
  if request == 'Hejdå' or request == "Adjö":
        print('SvenskaBot: Hejdå')
        break
  else:
    response=exotisk_bot.get_response(request)
    print('SvenskaBot: ', response)
