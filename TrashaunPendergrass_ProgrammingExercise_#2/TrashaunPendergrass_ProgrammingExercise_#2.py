# This program checks an email message for spam words and phrases
# The program uses 30 common spam words and phrases
# The program displays a spam score, the likelihood of it being spam, and the words found

def get_spam_words():
    # Stores the 30 spam words and phrases.
    return [
        "50% off",
        "a few bob",
        "accept cash cards",
        "accept credit cards",
        "affordable",
        "affordable deal",
        "avoid bankruptcy",
        "bad credit",
        "bank",
        "bankruptcy",
        "bargain",
        "billing",
        "billing address",
        "billion",
        "billion dollars",
        "billionaire",
        "card accepted",
        "cards accepted",
        "cash",
        "cash bonus",
        "cash out",
        "cash-out",
        "cashcashcash",
        "casino",
        "cents on the dollar",
        "check",
        "check or money order",
        "claim your discount",
        "cost",
        "credit"
    ]


def check_message(message, spam_words):
    # Starts the score at zero and creates a list for words found.
    spam_score = 0
    words_found = []

    # Makes the message lowercase so the search is not case sensitive.
    message = message.lower()

    # Checks each spam word in the message.
    for word in spam_words:
        word_count = message.count(word)

        # Adds the word count to the score if the word was found.
        if word_count > 0:
            spam_score = spam_score + word_count
            words_found.append((word, word_count))

    # Returns the score and words found to the main function.
    return spam_score, words_found


def get_spam_likelihood(spam_score):
    # Gives the spam likelihood based on the spam score.
    if spam_score == 0:
        likelihood = "Very unlikely to be spam"
    elif spam_score <= 3:
        likelihood = "Low chance of spam"
    elif spam_score <= 7:
        likelihood = "Moderate chance of spam"
    elif spam_score <= 12:
        likelihood = "High chance of spam"
    else:
        likelihood = "Very likely spam"

    # Returns the likelihood to the main function.
    return likelihood


def display_results(spam_score, likelihood, words_found):
    # Displays the spam score and likelihood.
    print(f"\nSpam Score: {spam_score}")
    print(f"Likelihood: {likelihood}")

    # Displays the words and phrases found.
    if len(words_found) > 0:
        print("\nSpam words/phrases detected:")

        for word, word_count in words_found:
            print(f"- '{word}' found {word_count} time(s)")
    else:
        print("\nNo spam keywords detected.")


def main():
    print("Spam Detection Program")
    print("----------------------")

    # Gets the email message from the user.
    message = input("Enter an email message:\n")

    # Gets the spam words and checks the message.
    spam_words = get_spam_words()
    spam_score, words_found = check_message(message, spam_words)
    likelihood = get_spam_likelihood(spam_score)

    # Displays the results.
    display_results(spam_score, likelihood, words_found)


# Starts the program.
main()