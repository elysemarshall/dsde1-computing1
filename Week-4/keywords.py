'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>

def welcome_message(user_name='', place=''):
    '''returns a string dependant on variables of user_name and place'''
    returned_message = 'Hello{} and welcome{}'
    user_name2 = ', ' + user_name + ','
    place2 = ' to ' + place
    if user_name and place != '':
        return returned_message.format(user_name2, place2)
    elif user_name != '':
        return returned_message.format(user_name2, place)
    elif place != '':
        return returned_message.format(user_name, place2)
    else:
        return 'Hello and welcome'

# Create a function called list_average()
# without using any libraries to do the maths for you
# (the point of this exercise is to practice interacting
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list

def list_average(list_of_numbers, avg_type='mean'):
    '''returns the average value depending on the list input
    and which average type the user wants to find'''
    if avg_type == 'mean':
        if len(list_of_numbers) == 0:
            return 0
        else:
            mean = sum(list_of_numbers) / len(list_of_numbers)
            return mean
    elif avg_type == 'median':
        if len(list_of_numbers) == 0:
            return None
        else:
            list_of_numbers.sort()
            index_median = int((len(list_of_numbers) / 2))
            median = list_of_numbers[index_median]
            return median
    elif avg_type == 'mode':
        if len(list_of_numbers) == 0:
            return []
        else:
            mode = max(list_of_numbers, key=list_of_numbers.count)
            return [mode]
