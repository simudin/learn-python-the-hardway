pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    
    new_word = word + first + pyg
    print new_word[1:]
else:
    print 'empty'