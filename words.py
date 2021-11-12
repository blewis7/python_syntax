# Question 1

def print_upper_words(words):
    """Input list of words, return them all uppercase"""

    for word in words:
        print(str.upper(word))

print_upper_words(['bob', 'john', 'living', 'hello'])

# Question 2

def print_words_starting_with(words):
    """Print words starting with 'e'"""

    for word in words:
        if word.startswith('e' or 'E') or word.startswith('E'):
            print(str.upper(word))

print_words_starting_with(['ever', 'john', 'Everest', 'running'])

# Question 3

def print_upper_words_with(words, must_start_with):
    """Print words that start letter1 or letter2 in uppercase"""
    
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(str.upper(word))

print_upper_words_with(['hello', 'hey', 'goodbye', 'yo'], ['h', 'y'])
print_upper_words_with(['hello', 'hey', 'goodbye', 'yo'], ['h'])
