def wordPattern(pattern: str, s: str) -> bool:
    # Split the string s into words using space as the delimiter
    words = s.split(" ")
    
    # If the number of characters in the pattern does not match the number of words, return False
    if len(pattern) != len(words):
        return False
    
    # Dictionaries to map characters to words and words to characters
    charToWord = {}
    wordToChar = {}
    
    # Iterate through the characters in the pattern and the words simultaneously
    for c, w in zip(pattern, words):
        # Check if the character has already been mapped to a different word
        if c in charToWord and charToWord[c] != w:
            return False
        
        # Check if the word has already been mapped to a different character
        if w in wordToChar and wordToChar[w] != c:
            return False
        
        # Create the mapping from character to word and word to character
        charToWord[c] = w
        wordToChar[w] = c
    
    # If all characters and words are consistently mapped, return True
    return True
