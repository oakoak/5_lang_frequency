import string
from collections import Counter
import sys


def load_data(filepath):
    with open(filepath, "r") as file:
        return file.read()


def get_most_frequent_words(text, number_of_words):
    all_words = filter(None, [word.strip(string.punctuation)
                          for word in text.lower().split()])
    most_frequent_words = Counter(all_words).most_common(number_of_words)
    return most_frequent_words


def pprint_words(most_frequent_words):
    for word, count in most_frequent_words:
        print(word, ":", count)


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        text = load_data(file_path)
        count = int(input("Enter the number of the most frequent words: "))
    except IndexError:
        exit("Error: No filename for reading!")
    except FileNotFoundError:
        exit("Error: file or path '{0}' not found!\n".format(file_path))
    except ValueError:
        exit("You entered an incorrect value")

    most_frequent_words = get_most_frequent_words(text, count)
    pprint_words(most_frequent_words)