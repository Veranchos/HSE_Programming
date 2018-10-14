import random
import os


def random_word_from_file(path):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, path)
    f = open(filename,'r', encoding = 'UTF-8')
    words = f.read()
    return random.choice(words.split('\t'))


def noun():
    return random_word_from_file('nouns.tsv')


def transitive_verb():
    return random_word_from_file('transitive_verbs.tsv')


def adjective():
    return random_word_from_file('adjectives.tsv')


def adverb():
    return random_word_from_file('adverbs.tsv')


def question_word():
    return random_word_from_file('question_words.tsv')


def pronoun():
    return random_word_from_file('./pronouns.tsv')


def random_statement():
    statement = ' '.join([adjective().capitalize(), noun(), adverb(), transitive_verb()+'s', adjective(), noun()]) + '.'
    return statement


def random_question():
    question = ' '.join([question_word().capitalize(), 'did', adjective(), noun(),  transitive_verb(), 'a', noun()]) + '?'
    return question


def random_imperative():
    imperative = ' '.join([transitive_verb().capitalize(), pronoun() + ',', adjective(), noun()]) + '!'
    return imperative


def random_negative():
    negative = ' '.join([adjective().capitalize(), noun(), 'doesn\'t', transitive_verb(), adjective(), noun()]) + '.'
    return negative


def random_conditional():
    conditional = ' '.join(['if'.capitalize(), adjective(), noun(), transitive_verb()+'s,', adjective(), noun(), 'will', transitive_verb()]) + '.'
    return conditional


def random_text():
    sentences = [random_statement(), random_question(), random_imperative(), random_negative(), random_conditional()]
    random.shuffle(sentences)
    return '\n'.join(sentences)


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'result.txt')

    file = open(filename, 'w+', encoding = 'UTF-8')
    file.write(random_text())
    file.close()
    return 0


if __name__ == '__main__':
    main()
