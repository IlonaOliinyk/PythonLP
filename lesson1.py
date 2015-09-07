# -*- coding: cp1251 -*-

#1)
#Визначити нову стрічку hello.
#Здійснити операцію hello+ msg.
#Змінити стрічку hello додавши в її кінці символ пробілу
#і знову виконати операцію hello+ msg.
print "\n1)"
msg = "Ilona Oliinyk"
str1 = 'Hello'
print "str1 = " + str1
print "str1 + msg = " + str1 + msg
str1 += " "     
print "str1 + msg = " + str1 + msg


#2) Поясніть результат виконання msg[::-1].
print "\n2)"
print msg[::-1]
print msg[-1:-14:-1]

#3)
#Використовуючи зрізи видаліть афікси у наступних словоформах:
#dish-es, run-ning, nation-ality, un-do, pre-heat.
print "\n3)"
word1 = 'dish-es'
word2 = 'run-ning'
word3 = 'nation-ality'
word4 = 'un-do'
word5 = 'pre-heat'
print word1[:-3]
print word1[0:4]

print word2[0:3]
print word2[:-5]

print word3[0:6]
print word3[:-6]

print word4[3:5]
print word4[-2:]

print word5[4:]
print word5[-4:]

#4)
#Напишіть for цикл,
#який виведе на екран символи стрічки msg по одному на рядок
print "\n4)"

for char in msg:
    print char
    

#5)
#Напишіть for цикл, який обробить phrase1
#визначивши довжину кожного елементу і результати збереже в новому списку lengths.
#(Створіть пустий список lengths = [].
#Далі використовуйте метод append() в тілі циклу для додавання довжин до списку).
print "\n5)"
phrase1 = ["Red","Green","Blue","Black"]
print "Phrase: "
print phrase1

lengths = []
for word in phrase1:
    lengths.append(len(word))

print lengths

#6
#Використайте функцію index() наступним чином ’inexpressible’.index(’e’).
#Що станеться якщо виконати ’inexpressible’.index(’re’)
print "\n6)"
str2 = 'inexpressible'
str3 = 'press'
print 'Symbol \'e\' has index - ' + str(str2.index('e'))
print 'Symbol \'re\' has index - ' + str(str2.index('re'))
print 'Symbol \'' + str3 + '\' has index - ' + str(str2.index(str3))

#3.25 Визначіть позиції всіх слів в списку phrase1 використовуючи метод index().
for word in phrase1:
    print "[%d] %s" % (phrase1.index(word), word)





