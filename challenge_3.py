def solve():
    str = input("Enter a word or sentence: ")
    vowels = set("aeiou")
    str = ''.join([char if char not in vowels else ' ' for char in str]).lower()
    substrings = str.split()
    values = [sum(ord(char) - ord('a') + 1 for char in sub) for sub in substrings]
    return max(values)

highest_val = solve()
print(f"The highest value of the consonant substrings is: {highest_val} ")