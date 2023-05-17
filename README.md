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
```
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
```
## Lemmatization

Lemmatization reduces words to their base or dictionary form. The `lemmatizing` function uses spaCy's English language model to lemmatize a given text.

```python
import spacy

def lemmatizing(text):
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]

    return lemmas

examplelemma = "am is are was were"
print(lemmatizing(examplelemma))
```
## Multi-Word Tokenization

If you want to treat multi-word entities like "New York" as a single token, you can use phrase tokenization. One way to achieve this is by using the `MWETokenizer` class from NLTK.

```python
from nltk.tokenize import MWETokenizer

def tokenizing_multiword(text):
    tokenizer = MWETokenizer([('New', 'York'), ('Alice', 'Springs')], separator=' ')
    tokens = tokenizer.tokenize(text.split())
    return tokens

sentence = "I'm going to New York tomorrow. Alice Springs, can't"
text = tokenizing_multiword(sentence)
print("Multi-word Tokenization:", expand_contractions_clitic(str(text)))
```

## Stemming

Stemming is the process of reducing words to their root or stem form. In this code snippet, stemming is demonstrated using the Snowball stemmer and Porter stemmer from NLTK.

```python
from nltk.stem import SnowballStemmer, PorterStemmer

def stemming(text):
    ps = PorterStemmer()
    ss = SnowballStemmer("english")
    SnowballStemmerlist = []
    PorterStemmerlist = []
    for w in text:
        word = ss.stem(w)
        SnowballStemmerlist.append(word)
        word2 = ps.stem(w)
        PorterStemmerlist.append(word2)

    return SnowballStemmerlist, PorterStemmerlist

examplewords = ["python", "pythoned", "pythoning", "pythoned", "pythonly"]
SnowballStemmerlist, PorterStemmerlist = stemming(examplewords)
print("SnowballStemmerlist:", SnowballStemmerlist)
print("PorterStemmerlist:", PorterStemmerlist)
```

## Stop Word Filtering

Stop word filtering involves removing commonly used words, known as stop words, from the text. NLTK provides a list of stop words for various languages. Here's an example of how to perform stop word filtering using NLTK.

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def tokenize_and_stop_word_filteration(text):
    stop_words = set(stopwords.words("english"))
    tokenize_words = word_tokenize(text)
    filtered_sentence = [w for w in tokenize_words if not w in stop_words]
    return tokenize_words, filtered_sentence

stopword_text = "This is an example of showing off stop word filtering"
tokenz, filterations = tokenize_and_stop_word_filteration(stopword_text)
print("Word Tokenization:", tokenz)
print("Stop Word Filtering:", filterations)

