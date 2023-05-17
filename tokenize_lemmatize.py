import nltk
# nltk.download()
# install all
from nltk.tokenize import word_tokenize,sent_tokenize,MWETokenizer,TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer,PorterStemmer, WordNetLemmatizer
import spacy


tokenizer = TweetTokenizer()
text= "I'm happy that you're here."
words = tokenizer.tokenize(text)
print(words)


# Expanding clitic contractions
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
print("Expand Clitic :",expanded_text)



# # lemmatizing
def lemmatizing(text):
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]

    return lemmas

examplelemma = "am is are was were"
print(lemmatizing(examplelemma))

# lemmatizer=WordNetLemmatizer()
# tokens=["am","is","are","cats"]
# for t in tokens:
#     print(lemmatizer.lemmatize(t, pos='v'))

# tokenizing multiword
def tokenizing_multiword(text):

    tokenizer = MWETokenizer([('New', 'York'),('Alice', 'Springs')], separator=' ')
    tokens = tokenizer.tokenize(text.split())
    return tokens

sentence = " I'm going to New York tomorrow. Alice Springs , can't "
text=tokenizing_multiword(sentence)
print(expand_contractions_clitic(str(text)))


# stemming
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

exampls=["python","pythoned","pythoning","pythoned","pythonly"]
SnowballStemmerlist,PorterStemmerlist=stemming(exampls)
print(" SnowballStemmerlist: ",SnowballStemmerlist)
print("PorterStemmerlist: ",PorterStemmerlist)

# stop words
def tokenize_and_stop_word_filteration(text):
    stop_words = set(stopwords.words("english"))
    tokenize_words = word_tokenize(text)
    filterd_sentence = [w for w in tokenize_words if not w in stop_words]
    return tokenize_words,filterd_sentence

stptext="This is an example of showing off stop word filteration"
tokenz,filterations=tokenize_and_stop_word_filteration(stptext)
print(" wordTokenization " ,tokenz)
print(" stop filteration :",filterations)





'''
If you want to treat multi-word entities like "New York" as a single token, 
you can use a different tokenization approach called phrase tokenization. 
Phrase tokenization allows you to define specific phrases or multi-word 
expressions that should be treated as a single token. One popular library that 
supports phrase tokenization is spaCy.
we use spaCy's English language model (en_core_web_sm) to process the sentence

In this updated code, we import the TweetTokenizer class from NLTK and use it for tokenization. 
This tokenizer is specifically designed to handle informal text, including contractions. By utilizing 
the TweetTokenizer, we ensure that contractions like "I'm" are treated as a single token.
'''
'''
need to work:
     import nltk 
     nltk.download()
     install all
     
     pip install spacy
    python -m spacy download en_core_web_sm

'''