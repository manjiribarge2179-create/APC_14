text = input("Enter a string: ")
old_char = input("Enter the character to be replaced: ")
new_char = input("Enter the new character: ")

result = ""

for ch in text:
    if ch == old_char:
        result += new_char
    else:
        result += ch

print("Modified string:", result)