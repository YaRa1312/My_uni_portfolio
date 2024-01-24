import nltk
nltk.download('rte')
from nltk import punkt
nltk.download('punkt')
from nltk import word_tokenize
nltk.download('word_tokenize')
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.corpus import wordnet as wn
nltk.download('wordnet')
from nltk.stem import PorterStemmer
nltk.download('PorterStemmer')
from nltk import sent_tokenize
nltk.download('sent_tokenize')


print("Плешивцева Ірина, Прикладна лінгвістика, Лабораторна робота №5")


file = open(r"Lab5.txt", "r")


text = file.read()


def freq_table(text) -> dict:
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    ps = PorterStemmer()
    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    return freqTable
print(freq_table(text))


print(sent_tokenize(text))


def score_sentences(sentences, freqTable) -> dict:
    sent_value = dict()
    for sent in sentences:
        word_count_in_sentence = (len(word_tokenize(sent)))
        for wordValue in freqTable:
            if wordValue in sent.lower():
               if sent[:15] in sent_value:
                  sent_value[sent[:15]] += freqTable[wordValue]
               else:
                  sent_value[sent[:15]] = freqTable[wordValue]
        sent_value[sent[:15]] = sent_value[sent[:15]] / word_count_in_sentence


    return sent_value
ft = freq_table(text)
s = sent_tokenize(text)
sv = score_sentences(s, ft)
print(sv)


def avg_score(sentValue) -> float:
    sumValues = 0
    for entry in sentValue:
        sumValues += sentValue[entry]
    average = sumValues / len(sentValue)
    return average


avg = avg_score(sv)
print(avg)


def summary(sentences, sentValue, threshold):
    sentence_count = 0
    summary = ''
    for sent in sentences:
        if sent[:15] in sentValue and sentValue[sent[:15]] > (threshold):
            summary += " " + sent
            sentence_count += 1
    return summary


summ = summary(s, sv, avg)
print(summ)


def avg_score(sentValue) -> float:
    sumValues = 0
    for entry in sentValue:
        sumValues += sentValue[entry]
    average = sumValues / 10
    return average


avg = avg_score(sv)
print(avg)


def summary(sentences, sentValue, threshold):
    sentence_count = 0
    summary = ''
    for sent in sentences:
        if sent[:15] in sentValue and sentValue[sent[:15]] > (threshold):
            summary += " " + sent
            sentence_count += 1
    return summary


summ = summary(s, sv, avg)
print(summ)


print("fight-1 entailments:")
print(wn.synset('fight.v.01').entailments())


def rte_features(rtepair):
    extractor = nltk.RTEFeatureExtractor(rtepair)
    features = {}
    features['word_overlap'] = len(extractor.overlap('word'))
    features['word_hyp_extra'] = len(extractor.hyp_extra('word'))
    features['ne_overlap'] = len(extractor.overlap('ne'))
    features['ne_hyp_extra'] = len(extractor.hyp_extra('ne'))
    return features
rtepair = nltk.corpus.rte.pairs(['rte3_dev.xml'])[14]
extractor = nltk.RTEFeatureExtractor(rtepair)
print("Ключові слова з тексту: ")
print(extractor.text_words)
print("Ключові слова з гіпотези: ")
print(extractor.hyp_words)
print("Перекриття між текстом і гіпотезою серед звичайних слів: ")
print(extractor.overlap('word'))
print("Перекриття між текстом і гіпотезою серед іменованих сутностей: " )
print(extractor.overlap('ne'))
print("Звичайні слова, які містяться лише в гіпотезі: ")
print(extractor.hyp_extra('word'))
print("Іменовані сутності, які містяться лише в гіпотезі: ")
print(extractor.hyp_extra('ne'))


file.close()
