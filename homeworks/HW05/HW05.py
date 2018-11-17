import os
import re


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
        elif value == maxValue:
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
        elif value == maxValue:
            first_letters.append(key)

    return first_letters


def get_different_file_names(path):
    diff_names = set()
    for root, dirs, files in os.walk(path):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            diff_names.add(filename)

    return len(diff_names)


def find_similar_extensions(path):
    counter = 0
    for root, dirs, files in os.walk(path):
        extensions = set()
        for file in files:
            filename, file_extension = os.path.splitext(file)
            extensions.add(file_extension)
        if len(files) != len(extensions):
            counter += 1

    return counter


def find_rich_folder(path):
    max_files = 0
    rich_folder = path
    for root, dirs, files in os.walk(path):
        if len(files) > max_files:
            max_files = len(files)
            rich_folder = root

    return rich_folder


def main():
    print(get_depth('.'))
    print(find_cyrillic('.'))
    print(get_popular_extensions('.'))
    print(get_popular_first_letter('.'))
    print(get_different_file_names('.'))
    print(find_similar_extensions('.'))
    print(find_rich_folder('.'))

    return


if __name__ == '__main__':
    main()
