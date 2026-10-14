#Take a sentence from the user, split it into words, and store them in a list of the file. Print the longest word.
s = input("Enter sentence: ")

f = open("words.txt", "w")
f.write(s)
f.close()

f = open("words.txt", "r")
words = f.read().split()
f.close()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)