#Read a file, split its content into words, and store them in a list.
#Print the total number of words
with open("text.txt", "r") as f:
    content = f.read()
    words = content.split()
    print(f"Total number of words: {len(words)}")
    
#Print all unique words.
unique_words = set(words)
print("Unique words:")
for word in unique_words:
    print(word)