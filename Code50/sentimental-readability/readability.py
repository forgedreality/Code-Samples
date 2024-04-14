import cs50
import math


def main():
    # Get text input from user
    text = input("Text: ")
    letters = 0
    words = 0
    sentences = 0

    # Iterate over text
    for idx, i in enumerate(text):
        # Is this character a letter?
        if i.isalpha():
            letters += 1

        # Is it punctuation?
        elif (i == ".") or (i == "?") or (i == "!"):
            # Let's remember to count this as a word if we're at the end of a sentence
            if (idx == len(text) - 1):
                words += 1

            # Punctuation signifies the end of a sentence, so increment our sentences by 1
            sentences += 1

        # Did we encounter a space, and the previous character wasn't also a space?
        elif (i == " ") and (text[idx - 1] != " "):
            # Count the words as we go
            words += 1

    # Calculate the average letters per 100 words
    letters = letters / words * 100
    # Calculate the average sentence length
    sentences = sentences / words * 100

    # Calculate our language level score
    # L = letters per 100 words S = sentences per 100 words
    score = round(0.0588 * letters - 0.296 * sentences - 15.8)

    # Output our results
    print("Before Grade 1" if score < 1 else "Grade 16+" if score >= 16 else f"Grade {score}")


if __name__ == "__main__":
    main()
