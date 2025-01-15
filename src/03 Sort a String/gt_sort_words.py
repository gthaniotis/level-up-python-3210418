def sort_words(words):
    return ' '.join(sorted(words.split(), key=str.lower))

print(sort_words("Hello World!"))  # Hello World!
print(sort_words("Go hang a salami, I’m a lasagna hog."))  # Go a hog hang I’m lasagna salami
print(sort_words("The quick brown fox jumps over the lazy dog."))  # brown dog. fox jumps lazy over quick The

