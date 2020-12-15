'''
A palindrome is a word that is spelled the same backward and forward, like “noon”
and “redivider”. Recursively, a word is a palindrome if the first and last letters are the
same and the middle is a palindrome.
##Write a function called is_palindrome that takes a string argument and returns
True if it is a palindrome and False otherwise. Remember that you can use
the built-in function len to check the length of a string.

'''

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1 : -1]

word = input("ENTER A WORD: ").strip(" ")
first_lettter = first(word)
last_letter = last(word)
middle_letter = middle(word)
reverse_word = word[::-1]

def is_palindrome(first_lettter, last_letter, middle_letter, reverse_word ):
    if first_lettter == last_letter and middle_letter == reverse_word[1 : -1]:
        return True
    else:
        return False


print(is_palindrome(first_lettter, last_letter, middle_letter, reverse_word))
