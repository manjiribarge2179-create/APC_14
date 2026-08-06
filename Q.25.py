string = input("Enter a string: ")

freq = {}

# Count frequency of each character
for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

first_char = ""
second_char = ""
first_count = 0
second_count = 0

# Find first and second highest frequencies
for ch in freq:
    if freq[ch] > first_count:
        second_count = first_count
        second_char = first_char

        first_count = freq[ch]
        first_char = ch

    elif freq[ch] > second_count and freq[ch] != first_count:
        second_count = freq[ch]
        second_char = ch

if second_char != "":
    print("Second most frequent character:", second_char)
    print("Frequency:", second_count)
else:
    print("No second most frequent character found.")