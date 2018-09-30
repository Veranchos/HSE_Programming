sentence = input()

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
encrypted_sentence = ''
result = ''

for ch in sentence:
    new_letter = ch
    number = alphabet.find(ch)
    NUMBER = ALPHABET.find(ch)
    if number != -1:
        number = (number + 1) % len(alphabet)
        new_letter = alphabet[number]
    elif NUMBER != -1:
        NUMBER = (NUMBER + 1) % len(ALPHABET)
        new_letter = ALPHABET[NUMBER]
    encrypted_sentence += new_letter
words = encrypted_sentence.split()
swapped_words = words[:-2] + [words[-1]] + [words[-2]]
result = ' '.join(swapped_words)
print(result)

