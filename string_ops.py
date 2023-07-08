original_string = "Python"

// : start at the end of the string
// move at -1

reversed_string = original_string[::-1]

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

input_string = "Hello"
vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count) 

