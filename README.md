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
