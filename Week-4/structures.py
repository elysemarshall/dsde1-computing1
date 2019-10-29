'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    return [the_list[0], the_list[-1]]

# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any of the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):        #user puts in their list, and parameters for beginning and end
    if end < beginning or beginning > len(the_list):
        raise ValueError
    else:
        reverse_list = the_list[beginning:end + 1] #make a variable where list is only parts specified by parameters
        reverse_list.reverse()                     #Reverse order of list
    return reverse_list                            #Call function


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    i = 0                                          #Created a loop so that it does it twice automatically but could also just manually do the code twice
    while i < 2:
        the_list.insert(index, the_list[index])
        i += 1
    return the_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    word_reverse = word[::-1]
    test = word == word_reverse
    return test

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    s = sentence
    s = s.replace(" ", "")
    print (s)
    s = s.lower()
    print(s)
    sentence_reverse = s[::-1]
    print(sentence_reverse)
    sentence_test = sentence_reverse == s
    return sentence_test

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentenece1, sentence2):
    s1 = sentenece1.strip() #removes whitespace
    s2 = sentence2.strip()  #removes whitespace
    first_letter1 = s1[0]
    first_letter2 = s2[0]
    last_letter1 = s1[-1]
    last_letter2 = s2[-1]

    punct = ['.','?','!']

    return



# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    dictionary1.update(dictionary2)
    return dictionary1
