def analyze_string(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    number_count = 0
    space_count = 0

    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
        elif char.isdigit():
            number_count += 1
        elif char.isspace():
            space_count += 1

    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Numbers:", number_count)
    print("Spaces:", space_count)

input_str = input("Enter a string: ")
analyze_string(input_str)
