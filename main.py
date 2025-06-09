import itertools
import math


def generate_result_combinations():
    combination_tuples = itertools.product(["0", "1", "2"], repeat=5)
    combination_strings = []
    for combo_tuple in combination_tuples:
        combination_strings.append("".join(combo_tuple))
    return combination_strings


# p(x) * log₂(1/p(x))
def calculate_bits(p):
    return p if p == 0 else p * math.log2(1 / p)


def get_word_expected_value(words, word):
    total_words_length = len(words)
    total_bits = 0
    for combo in RESULT_COMBINATIONS:
        guess = generate_guess(word, combo)
        matched_words_length = len(eliminate_words(words, guess))
        p = matched_words_length / total_words_length
        total_bits += calculate_bits(p)
    return total_bits


def get_word_bits_list(words):
    word_bits_list = {}
    for word in words:
        word_bits_list[word] = get_word_expected_value(words, word)
        print(f"{word}:{word_bits_list[word]}")
    return word_bits_list


def eliminate_words(words, guess):
    for i in range(5):
        char, status = guess[i]
        if status == "0":
            words = [word for word in words if char not in word]
        if status == "1":
            words = [word for word in words if (word[i] != char and char in word)]
        if status == "2":
            words = [word for word in words if word[i] == char]
    return words


def generate_guess(word, result):
    guess = {}
    for i in range(len(word)):
        guess[i] = (word[i], result[i])
    return guess


def process_word_list(filename):
    file = open(filename, "r")
    content = file.read()
    return str.splitlines(content)


if __name__ == "__main__":
    RESULT_COMBINATIONS = generate_result_combinations()
    possible_words = process_word_list("allowed_words.txt")
    user_word = ""
    while user_word != "exit":
        word_bits_list = get_word_bits_list(possible_words)
        sorted_word_bits_list = sorted(
            word_bits_list.items(), key=lambda item: item[1], reverse=True
        )
        suggestions = list(sorted_word_bits_list)[:5]
        print(f"suggested words:\n {suggestions}")
        user_word = input("Enter your guess:\n")
        guess_result = input("Enter the result of your guess: 0 = ⬛ 1 = 🟨, 2 = 🟩\n")
        guess = generate_guess(user_word, guess_result)
        possible_words = eliminate_words(possible_words, guess)
        print(possible_words)
