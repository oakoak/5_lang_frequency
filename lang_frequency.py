import string
from collections import Counter
import sys
import argparse


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


def get_parser_args():
    parser = argparse.ArgumentParser(description="Most frequent words in text")
    parser.add_argument(
        "path",
        help="path for .txt file",
    )
    parser.add_argument(
        "number",
        type=int,
        nargs="?",
        default=10,
        help="count of encountered words in text"
    )
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    arguments = get_parser_args()
    try:
        text = load_data(arguments.path)
    except FileNotFoundError:
        exit("ERROR : file '{}' not found\n".format(arguments.path))
    most_frequent_words = get_most_frequent_words(text, arguments.number)
    pprint_words(most_frequent_words)
