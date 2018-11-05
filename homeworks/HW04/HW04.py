import re


def read_old_text(filepath):
    text = open(filepath, 'r', encoding='UTF-8')
    text = text.read()
    text = text.replace(chr(769), '')
    return text


def write_new_text(filepath, text):
    new_text = open(filepath, 'w+', encoding = 'UTF-8')
    new_text.write(text)
    new_text.close()
    return new_text


def replace(text, regex, new_word):
    new_text = re.sub(regex, new_word, text)
    return new_text


def main():
    objects_list = [{
        'filepath_from': 'Linguistics.txt',
        'sub_pattern': r'[яЯ]зык([а-я]{0,3}\b)',
        'substitution': r'шашлык\1',
        'filepath_to': 'shashlystics.txt'
    },
    {
        'filepath_from': 'Philosophy.txt',
        'sub_pattern': r'[фФ]илософи([а-я]{0,3})',
        'substitution': r'астрологи\1',
        'filepath_to': 'astrology.txt'
    },
    {
        'filepath_from': 'Finland.txt',
        'sub_pattern': r'[Фф]инлянди([а-я]{0,3})',
        'substitution': r'Малайзи\1',
        'filepath_to': 'Malaysia.txt'
    }]
    for object in range (len(objects_list)):
        text = read_old_text(objects_list[object]['filepath_from'])
        regex = objects_list[object]['sub_pattern']
        substitution = replace(text, regex, objects_list[object]['substitution'])
        new_text = write_new_text(objects_list[object]['filepath_to'], substitution)
    return new_text



if __name__ == '__main__':
    main()


