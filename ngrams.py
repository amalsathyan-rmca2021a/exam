import nltk
nltk.download()
from nltk import ngrams
Sampletext = "welcome to Amaljyothi college of engineering"
NGRAMS = ngrams(sequence=nltk.word_tokenize(Sampletext), n=3)
for grams in NGRAMS():
    print(grams)
