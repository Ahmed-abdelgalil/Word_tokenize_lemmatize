# Tokenization, Text Processing, and Stemming/lemmatization

This code demonstrates various text processing techniques using the NLTK and spaCy libraries in Python. It includes tokenization, clitic contraction expansion, lemmatization, multi-word tokenization, stemming, and stop word filtering.

## Dependencies

Before running the code, make sure to install the necessary dependencies:

- NLTK: `import nltk` and then run `nltk.download()` to open the NLTK downloader. Install all the required resources.
- spaCy: `pip install spacy` followed by `python -m spacy download en_core_web_sm` to download the English language model for spaCy.

## Tokenization

Tokenization is the process of splitting a text into individual words or tokens. The code uses the `TweetTokenizer` class from NLTK to tokenize the text. This tokenizer is suitable for informal text and handles contractions properly.

```python
from nltk.tokenize import TweetTokenizer

tokenizer = TweetTokenizer()
text = "I'm happy that you're here."
words = tokenizer.tokenize(text)
print(words)

## Clitic Contraction Expansion

Clitic contractions like "I'm" or "you're" are expanded into their full forms, such as "I am" or "you are". The `expand_contractions_clitic` function takes a text as input and returns the expanded text.

```python
def expand_contractions_clitic(text):
    contractions = {
        "I'm": "I am",
        "you're": "you are",
        "he's": "he is",
        "she's": "she is",
        "it's": "it is",
        "we're": "we are",
        "they're": "they are",
        "can't": "can not",
        "don't": "do not",
        "won't": "will not"
        # Add more contractions as needed
    }
    tokenizer = TweetTokenizer()
    words = tokenizer.tokenize(text)
    expanded_words = []

    for word in words:
        if word in contractions:
            expanded_words.extend(tokenizer.tokenize(contractions[word]))
        else:
            expanded_words.append(word)

    expanded_text = ' '.join(expanded_words)
    return expanded_text

# Example usage
text = "I'm happy that you're here. can't and you're he's she's "
expanded_text = expand_contractions_clitic(text)
print("Expand Clitic:", expanded_text)
