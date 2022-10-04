text = input("Text: ")
print(text)
words = 1
sentences = 0
letters = 0
for i in range(len(text)):
    # word count
    if text[i] == " ":
        words = words + 1

    # sentences count
    if text[i] == "." or text[i] == "!" or text[i] == "?":
        sentences = sentences + 1

# letters in text
letters = len(text) - words - sentences

# print(str(words)+" Words")
# print(str(sentences)+" Frases!")
# print(str(letters)+" Letters")

# Average letter and sentences per 100 words in the text
averageLetters = round((letters * 100) / words)
averageSentences = round((sentences * 100) / words)

# 0.0588 * L - 0.296 * S - 15.8  => Coleman-Liau formula
readability = round((0.0588 * averageLetters) - (0.296 * averageSentences) - 15.8)

if readability >= 16:
    print("Grade 16+")
elif readability < 1:
    print("Before Grade 1 ")
else:
    print("Grade " + str(readability))
