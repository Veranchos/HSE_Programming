text = input("Please write a small text in arabic (word roots = 3 letters, no extra).")
words = []
words.append(text.split(' '))
if text:
    for word in words:
        if word.startswith("ي" or "ت" or "ا" or "ن"):
            print("It's a verb in imperfect!")
        elif word.startswith("ا") and word.endswith("ي" or "و" or "ا"):
            print("It's a verb in imperative!")
        elif word.endswith("تما" or "ت" or "نا" or "تن" or "تم" or "ن" or "وا"):
            print("It's a verb in perfect!")
        elif word.startswith("م"):
            if word[3] == 'و':
                print("It's passive participle!")
            elif word[1] == 'ا':
                print("It's active participle!")
        elif word.endswith('ي' or 'ة'):
            print("It's an adjective!ّ")
        elif word.startswith("ال"):
            print("It's a Noun!")
        elif word == 'انا'or 'هو' or 'هي' or 'انت'or 'انتم' or 'نحن' or 'انتما':
            print("It's a pronoun!")









