# This program will query a user for a paragraph
# it then reads the paragraph and scans it to find what sentences are in the paragraph
# it calculates how many sentences and list them sequentially
# it displays the total count, and includes paragraphs that start with numbers.

# Imports the regular-expressions package for use
import re

# asks user for a paragraph and assigns it to paragraph variable
def ask_paragraph():
    paragraph = input('Enter a paragraph to see sentence count: ')

    # Returns the input.
    return paragraph

# takes paragraph and uses regular-expression to return list of sentences.
def export_sentences(paragraph):

    # positive lookahead regular-expression that scans ahead to find sentences.
    pat = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    # assigns the matches found to a list called sentence
    sentences = re.findall(pat, paragraph, flags=re.DOTALL | re.MULTILINE)

    # Returns the sentence matches
    return sentences

# takes sentence list, displays them numbered sequentially and reads back the total count.
def display_sentences(sentences):

    # Displays the sentences found, numbered sequentially
    for i, sentence in enumerate(sentences, 1):
        print(f'  Sentence {i}: {sentence}')

    # Calculates and displays total count of sentences
    count = len(sentences)
    print(f'\nSentence count: {count}')

# defines main function that will run the program, calling other functions sequentially.
def main():
    paragraph = ask_paragraph()
    sentences = export_sentences(paragraph)
    display_sentences(sentences)


# Runs the function
main()