# ************************** Author: Dimitrios Mamakas for www.aueb.gr **************************

# Import random
import random

# Removes useless characters from a single word.
def beautifyWord(word):
    # Apply a format of rules. Remove useless characters
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace('\n', '')
    word = word.replace(' ', '')
    word = word.replace("''", '')
    
    # Return the updated word
    return word

# Function which shuffles the words of a certain text and re-orders them randomly, removing any useless characters existing.
def textShuffler(text):
    # Split the words into a list
    list_of_words = text.split(' ')
    
    # List containing the updated words
    updated_list_of_words = []

    # Iterate the list and remove useless characters if any
    for word in list_of_words:
        word = beautifyWord(word)
        updated_list_of_words.append(word)
    
    # Randomly shuffle the updated list of words
    random.shuffle(updated_list_of_words)
    
    # New text
    newText = ""

    # Append the updated list of words into a new text
    for word in updated_list_of_words:
        newText += word + " "
    
    # Return the shuffled text
    return newText

# Mapper function which updates the dataset based on new, shuffled data.
# Note: This function accepts and returs a dictionary.
def updateDatasetTextField(field):
    # Apply the mapping function
    field['text'] = textShuffler(field['text'])
    
    # Return the updated dictionary
    return field

# Mapper function which updates the dataset based on new, shuffled data without containing duplicates.
# Note: This function accepts and returs a dictionary.
def updateDatasetTextFieldAndRemoveDuplicates(field):
     # Apply the mapping function
    temp = textShuffler(field['text'])
    
    # Remove the duplicates
    field['text'] = findUniqueWords(temp.split(' '))
    
    # Return the updated dictionary
    return field

# Sets the word frequency equal to 1 (per word) in a range of given words.
# Note: This function accepts a list and returns a String of the truncated text.
def findUniqueWords(wordList):
    # List containing the words - Their frequency is going to be 1
    uniqueWordsList = []
    
    # Set the frequency equal to 1
    for word in wordList:
        if word not in uniqueWordsList:
            uniqueWordsList.append(word)
    
    # String containing the updated text
    updatedText = ""
    
    # Unify the updated word list into a new text
    for word in uniqueWordsList:
        updatedText += word + " "
    
    # Return the updated text
    return updatedText