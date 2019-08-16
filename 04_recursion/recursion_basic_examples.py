def rec_sum(n):
    # Base Case
    if n == 0:
        return 0

    # Recursion
    else:
        return n + rec_sum(n - 1)


def sum_func(n):
    # Base case
    if len(str(n)) == 1:
        return n

    # Recursion
    else:
        return n % 10 + sum_func(n / 10)


def word_split(phrase, list_of_words, output=None):

    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []

    # For every word in list
    for word in list_of_words:

        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):
            # Add the word to the output
            output.append(word)

            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split(phrase[len(word):], list_of_words, output)

    # Finally return output if no phrase.startswith(word) returns True
    return output
