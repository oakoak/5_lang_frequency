import string
import collections
import operator
import sys


def load_data(filepath):
    with open(filepath, "r") as file:
        return file.read()


def get_most_frequent_words(text):
    words = filter(None, [word.strip(string.punctuation).lower()
                          for word in text.split()])
    frequency_words = collections.Counter(words)
    sorted_words = sorted(frequency_words.items(),
                          key=operator.itemgetter(1), reverse=True)
    for i in sorted_words[:10]:
        print(i[0])


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        text = load_data(file_path)
    except IndexError:
        exit("Error: No filename for reading!")
    except FileNotFoundError:
        exit("Error: file or path '{0}' not found!\n".format(file_path))

    get_most_frequent_words(text)
