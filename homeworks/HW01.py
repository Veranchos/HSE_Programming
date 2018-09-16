#1
word1 = input('Пожалуйста, введите слово.')
new_word1 = ''
for i in range(len(word1)):
    if i % 2 != 0 and word1[i] != "а" and word1[i] != "к":
        new_word1 += word1[i]
print(new_word1)

#2
number = int(input('Пожалуйста, введите число.'))
for i in range(number):
    word2 = input('Пожалуйста, введите слово.')
    if word2 == 'программирование':
        break
    print(word2)

#3
word3 = input('Пожалуйста, введите слово.')
middle = len(word3)//2
new_word3 = word3[:middle] + word3[:middle-1:-1]
print(new_word3)


