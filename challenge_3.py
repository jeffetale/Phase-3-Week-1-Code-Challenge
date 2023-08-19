def solve():
    while True:
        str = input("Enter a word or sentence: ")
        if not any(char.isdigit() for char in str) and all(char.isalpha() or char.isspace() for char in str)  and not all(char in "aeiou" for char in str.lower()) and str and not str.isspace():
            break
        print("Error: Input should only contain letters, not only vowels, and not be empty or contain only spaces. Please try again!")
    vowels = set("aeiou")
    str = ''.join([char if char not in vowels else ' ' for char in str]).lower()
    substrings = str.split()
    values = [sum(ord(char) - ord('a') + 1 for char in sub) for sub in substrings]
    return max(values)

highest_val = solve()
print(f"The highest value of the consonant substrings is: {highest_val} ")