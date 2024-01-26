# =============================================================================
# Developed by Craig Hanenberg
# on 2024/04/26

# Software that can help eccentric Scrabble playing client train for 
# their Scrabble matches
# =============================================================================

import random # used for random choice amongst words which meet criteria.

def load_word_list(file_path):
    """
    Load a list of words from a text file 'Words_alpha'.
    
    Parameters:
    - file_path (str): The path to the text file.

    Returns:
    list: A list containing words from the text file.
    """
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def replace_words(sentence, word_list):
    """
    Replace each word in the sentence with another word that starts with the same letter
    and has the same length. If no suitable replacement is found, keep the original word.
    
    Parameters:
    - sentence (str): The input sentence.
    - word_list (list): List of words for replacement.
    
    Returns:
    str: The new sentence with replaced words.
    """
# =============================================================================
#     Two lists are initialized with the first 'words' containing the individual 
#     words from the clients sentence. The second is a list 'new_sentence' which 
#     will be returned with the new Scrabble sentence. 
# =============================================================================
    words = sentence.split()
    new_sentence = []

    # Iterate through each of the clients words for a replacement in the word_list.
    for word in words:
        # Check: variable is not a single character & is alphabetic(letters)
        if len(word) > 1 and word.isalpha():
            # find a list of words which meet the criteria from the word_list.
            potential_words = [w for w in word_list 
                                      if len(w) == len(word) and w[0].lower() == word[0].lower()]
            # Randomized slection and return original word if criteria is not met.
            replacement = random.choice(potential_words) if potential_words else word
            new_sentence.append(replacement)
        else: new_sentence.append(word)
    return ' '.join(new_sentence)

if __name__ == "__main__":
    
    word_list = load_word_list("words_alpha.txt")
    # The client is promoted to 'Enter a sentence' which is easily understood when operating in a command terminal.
    client_sentence = input("Enter a sentence: ")
 
    output = replace_words(client_sentence, word_list)
    # The results are printed into the command terminal for easy inspection.  
    print("New Scrabble Sentence:", output)
