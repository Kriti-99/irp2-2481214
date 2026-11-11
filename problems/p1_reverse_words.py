def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


sentence = input("Enter a sentence: ")

result = reverse_words(sentence)

print("Reversed sentence:", result)
