import re


def read_a_text(filename):
    f = open(filename, 'r', encoding='UTF-8')
    text = f.read()
    return text


def find_spacecrafts(text):
    regexp = '«[А-Я].+?[эун0-9]»'
    spacecrafts = re.findall(regexp, text)
    return spacecrafts


def main():
    a = read_a_text('chinese_space_program.txt')
    spacecrafts = find_spacecrafts(a)
    for name in spacecrafts:
        print(name)
    return spacecrafts


if __name__ == '__main__':
    main()