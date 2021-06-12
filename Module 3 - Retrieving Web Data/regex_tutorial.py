## regex cheat sheet
## https://cheatography.com/mutanclan/cheat-sheets/python-regular-expression-regex/

## using ctrl+f to find in VSC then ALT+R to search using regex

text = 'something'

numbers = 1234

sentence = 'This is a sentence'

import re

#email validation

pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.+(com|edu|net)'
print('Enter email:')

user_input = input()
if(re.search(pattern, user_input)):
   print('valid email')
else:
   print('invalid email')


#replace part of a string

