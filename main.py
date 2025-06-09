def eliminate_words(words, guess):
    for i in range(5):
        char, status = guess[i]
        print(guess[i])
        if status == "0":
            words = [word for word in words if char not in word]
        if status == "1":
            words = [word for word in words if (word[i] != char and char in word)]
        if status == "2":
            words = [word for word in words if word[i] == char]
    return words


def process_word_list(filename):
    file = open(filename, "r")
    content = file.read()
    return str.splitlines(content)


if __name__ == "__main__":
    possible_words = process_word_list("allowed_words.txt")
    user_word = input("Enter your guess:\n")
    while user_word != "exit":
        guess_result = input("Enter the result of your guess: 0 = ⬛ 1 = 🟨, 2 = 🟩\n")
        guess = {}
        for i in range(len(user_word)):
            guess[i] = (user_word[i], guess_result[i])
        possible_words = eliminate_words(possible_words, guess)
        print(possible_words)
        user_word = input("Enter your guess:\n")
