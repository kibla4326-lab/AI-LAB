# Lab 4 Tasks:

#  Task 1: 
def luhn_algorithm(card_number):
    """
    This function checks if a credit/debit card number is valid using LUHN algorithm.
    """
    digits = [int(d) for d in str(card_number)]
    
    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled
    
    total = sum(digits)
    
    return total % 10 == 0

card_num = 4532015112830366
print("Task 1 - LUHN Algorithm Check:")
print(f"Card Number {card_num} is valid? -> {luhn_algorithm(card_num)}\n")


#  Task 2: Remove Punctuations 
import string

def remove_punctuations(text):
    """
    This function removes all punctuations from the given string.
    """
    return text.translate(str.maketrans('', '', string.punctuation))

sample_text = "Hello! Welcome to AI Lab, Python programming."
print("Task 2 - Remove Punctuations:")
print("Original Text:", sample_text)
print("Without Punctuations:", remove_punctuations(sample_text), "\n")


#  Task 3: Sort Sentence Alphabetically 
def sort_sentence(sentence):
    """
    This function sorts words of the sentence in alphabetical order.
    """
    words = sentence.split()
    words.sort()  
    return ' '.join(words)

sentence = "python programming is fun and interesting"
print("Task 3 - Sort Sentence Alphabetically:")
print("Original Sentence:", sentence)
print("Sorted Sentence:", sort_sentence(sentence))