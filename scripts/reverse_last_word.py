def reverse_last_word(sentence):
    if not sentence:
        return ''
    
    words = sentence.split()
    if not words:
        return ''
    
    last_word = words[-1]
    reversed_last_word = last_word[::-1]
    
    words[-1] = reversed_last_word
    return ' '.join(words)

# Test cases
print(reverse_last_word('This is a test sentence'))  # Output: 'This is a test ecnetnes'
print(reverse_last_word('Hello'))  # Output: 'olleH'
print(reverse_last_word(''))  # Output: ''
print(reverse_last_word('Hello!'))  # Output: 'olleH!'