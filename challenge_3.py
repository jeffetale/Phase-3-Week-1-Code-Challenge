'''
Challenge 3: Consonant value
Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. 
Consonants are any letters of the alphabet except "aeiou".We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
'''

'''
def solve(s):
    # Define a function to calculate the value of a consonant substring
    def calculate_consonant_value(substring):
        value = 0
        for char in substring:
            value += ord(char) - ord('a') + 1
        return value
    
    consonant_substrings = []
    current_substring = ""
    
    for char in s:
        if char not in "aeiou":
            current_substring += char
        else:
            if current_substring:
                consonant_substrings.append(current_substring)
                current_substring = ""
    
    # Add the last substring if it's not empty
    if current_substring:
        consonant_substrings.append(current_substring)
    
    # Calculate the value of each consonant substring and return the maximum
    max_value = 0
    for substring in consonant_substrings:
        value = calculate_consonant_value(substring)
        if value > max_value:
            max_value = value
    
    return max_value

# Test cases
print(solve("zodiacs"))  # Output: 26
print(solve("strength")) # Output: 57
'''

def solve(s):
    vowels = set("aeiou")
    s = ''.join([c if c not in vowels else ' ' for c in s]).lower()
    substrings = s.split()
    values = [sum(ord(c) - ord('a') + 1 for c in sub) for sub in substrings]
    return max(values)

print(solve("The most difficult problem I have yet faced"))