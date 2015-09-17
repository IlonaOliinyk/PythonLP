# -*- coding: utf-8 -*-

import nltk
from nltk.book import *


#Використовуючи конкорданси поясніть відмінності у вживанні
#слова however на початку речення
#("in whatever way", "to whatever extent", або "nevertheless”).
print "\n4)\n"

emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
print emma.concordance("However")


#Проаналізуйте таблицю частот модальних дієслів для різних жанрів.
#Спробуйте її пояснити. Знайдіть інші класи слів
#вживання яких також відрізняються в різних жанрах.

from nltk.corpus import brown


#cfd = nltk.ConditionalFreqDist(
 #   (genre, word)
  #  for genre in brown.categories()
  #      for word in brown.words(categories=genre))

#genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
#words = ['under', 'above', 'upon']
#cfd.tabulate(conditions=genres, samples=words)




#Напишіть програму для знаходження всіх слів в корпусі Brown,
#які зустрічаються не менш ніж три рази.


#from nltk.corpus import brown
#text = brown.words(categories='news')
#fdist = nltk.FreqDist([w.lower() for w in text])
#for m in text:
#    if fdist[m] > 3 and len(m) > 3: 
#        print m + ':', fdist[m]



#Напишіть програму генерації таблиці відношень  кількість
#слів/кількість оригінальних слів для всіх жанрів корпуса Brown.
#Проаналізуйте отримані результати та поясніть їх.

print "we are here 1"


#print "=========================================="
#for genre in brown.categories():
#    num_words = len(brown.words(categories=genre))
#    num_vocab = len(set([w.lower() for w in brown.words(categories=genre)]))
#    print "|num_words %s\tnum_vocab %s\t\tVal. %s\t\tGenre: %s\t|" % (num_words, num_vocab, int(num_words/num_vocab), genre)
#print "=========================================="


      
print "we are here 2"


#Напишіть програму для створення таблиці частот слів для різних жанрів.
#Знайдіть слова чия присутність або відсутність є характерною для певних жанрів
#(подібно до модальних дієслів).
#modals = ['can', 'could', 'may', 'might', 'must', 'will']

#for genre in brown.categories():
 #   text = brown.words(categories=genre)
 #   fdist = nltk.FreqDist([w.lower() for w in text])
 #   for m in modals:
 #       print m + ':', fdist[m], genre,"\n"


#Визначити функцію hedge(text),
#яка обробляє текст і створює нову версію цього тексc
#додаючи слово ‘like’ перед кожним третім словом.

 
def hedge(text):
    count = 0
    textRes = ""
    for w in text:
        if count == 1:
            count = 0
            textRes += "[like] " + w + " "
        else:
            textRes += w + " "
            count += 1
    return textRes

#text1 = "hello2 helo2 helo3 helo4 helo5 helo6 helo7"
new_text = hedge(text1[100:130])
print new_text


