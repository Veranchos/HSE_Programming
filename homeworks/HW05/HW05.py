import os
import re


def walk(path):
    print(path)
    root = ''
    dirs = []
    files = []
    for root, dirs, files in os.walk(path):
        print(root, dirs, files)
        root = root
        dirs = dirs
        files = files

    return root, dirs, files

def get_depth(path):
    counter = 0
    for root, dirs, files in os.walk(path):
        counter = max(counter, len(root.split(os.sep)))

    return counter - 1

def find_cyrillic(path):
    counter = 0
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if re.search(r'^[А-Яа-я]*$', dir):
                counter += 1

    return counter

def get_popular_extensions(path):
    dict = {}
    maxValue = 0
    file_extensions = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filename, file_extension = os.path.splitext(file)

            if file_extension in dict:
                dict[file_extension] = dict[file_extension] + 1

            else:
                dict[file_extension] = 1

    for key, value in dict.items():
        if value > maxValue:
            maxValue = value
            file_extensions = [key]
        elif (value == maxValue):
            file_extensions.append(key)

    return file_extensions


def get_popular_first_letter(path):
    dict = {}
    maxValue = 0
    first_letters = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            first_letter = dir[0]

            if first_letter in dict:
                dict[first_letter] = dict[first_letter] + 1

            else:
                dict[first_letter] = 1

    for key, value in dict.items():
        if value > maxValue:
            maxValue = value
            first_letters = [key]
        elif (value == maxValue):
            first_letters.append(key)

    return first_letters


def main():
    print(get_depth('.'))
    print(find_cyrillic('.'))
    print(get_popular_extensions('.'))
    print(get_popular_first_letter('.'))

    pass


if __name__ == '__main__':
    main()
