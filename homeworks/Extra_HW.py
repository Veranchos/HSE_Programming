text = input("Введите текст")
words = text.split()
d = {}
for word in words:
    word = word.lower()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for word in d:
    print(word)
    print(d[word])
