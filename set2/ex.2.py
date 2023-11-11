import re

text = 'siema elo ./ . . s . 8, hiuhi ,809, 8 . 8.8 2321'
text = text.lower()

alphanumeric_text = re.sub(r'[^a-zA-Z0-9\s,]', '', text)
words = alphanumeric_text.split()

word_count = len(words)

alphanumeric_count = 0

for char in text:
    if char.isalpha() or char.isdigit():
        alphanumeric_count += 1

print("Number of words:", word_count)

sign_count = {}

for char in text:
    if char.isalpha() or char.isdigit():
        sign_count[char] = sign_count.get(char, 0) + 1
    
for sign, count in sign_count.items():
    print(f"Character '{sign}' occurs {count} times. Statistic: {(count/alphanumeric_count)*100} %")
