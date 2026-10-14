with open("abc.txt", "r") as file:
    content = file.read()
    print(content)
    
#count vowels in the content
vowels = "aeiouAEIOU"
vowel_count = 0
for char in content:
    if char in vowels:
        vowel_count += 1
        #print(f"Vowel found: {char}")
print(f"Total vowels in the file: {vowel_count}")