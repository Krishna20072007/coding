import itertools
import enchant

def generate_anagrams(word):
    # Create a list of all possible permutations of the letters in the word
    permutations = itertools.permutations(word)

    # Initialize an English dictionary
    english_dict = enchant.Dict("en_US")

    # Check each permutation to see if it forms a meaningful word
    meaningful_anagrams = []
    for permutation in permutations:
        current_word = ''.join(permutation)
        if english_dict.check(current_word):
            meaningful_anagrams.append(current_word)

    return meaningful_anagrams

# Example usage
word = input("Enter a word: ")
anagrams = generate_anagrams(word)

if len(anagrams) > 0:
    print(f"Meaningful anagrams for {word}:")
    for anagram in anagrams:
        print(anagram)
else:
    print("No meaningful anagrams found.")
