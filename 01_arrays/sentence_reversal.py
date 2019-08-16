# def rev_word(sentence):
#     # return the join of the reversed list
#     return ' '.join(reversed(sentence.split()))


def rev_word2(sentence):
    words = []
    length = len(sentence)

    # Index Tracker
    i = 0

    # While index is less than length of string
    while i < length:

        # If element isn't a space
        if not sentence[i].isspace():

            # The word starts at this index
            word_start = i

            while i < length and not sentence[i].isspace():
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(sentence[word_start:i])
        # Add to index
        i += 1

    # Join the reversed words
    return " ".join(reversed(words))


print(rev_word2('Hi John,   are you ready to go?'))
