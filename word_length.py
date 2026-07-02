# Print length of each word

def word_lengths(words):

    for word in words:
        print(word, "=", len(word))

words = ["Python", "Java", "HTML", "Programming"]

word_lengths(words)
