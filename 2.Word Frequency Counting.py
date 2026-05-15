# ════════════════════════════════════════
#   Word Frequency Counter
#   Exercise: dictionary / if-elif-else /
#             try-except-pass / Error Handling
# ════════════════════════════════════════

# Accept a block of text from the user and count the frequency of each word.
try:
    text = input("Please enter a block of English text: ")

    if text == "":
        print("⚠ You haven't entered any content, the program will exit.")
        exit()

except ValueError:
    print("⚠ Invalid input. Please run the program again.")
    exit()

# Ignore case sensitivity by converting the text to lowercase.
try:
    text_lower = text.lower()

except NameError:
    print("⚠ Invalid input. Please run the program again.")
    exit()

# Split the text into words and count the total number of words (including duplicates).
words = text_lower.split()
print("Total words found (including duplicates):", len(words))

# Use a dictionary to count the frequency of each word.
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    elif word == "":
        pass
    else:
        word_count[word] = 1

# Sort the dictionary by frequency and print the results in a readable format.
try:
    sorted_words = sorted(word_count.items(),
                          key=lambda item: item[1],
                          reverse=True)

    print("\n── Word Frequency Results ──────────────────")
    print(f"{'Word':<15} Frequency ")
    print("─" * 25)

    for word, count in sorted_words:
        if count >= 3:
            print(f"{word:<15} {count} times  ← High-frequency word")
        elif count == 2:
            print(f"{word:<15} {count} times  ← Medium-frequency word")
        else:
            print(f"{word:<15} {count} times  ← Low-frequency word")

except NameError:
    print("⚠ Statistical data lost, please run the program again.")