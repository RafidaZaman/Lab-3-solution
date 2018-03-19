import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import ngrams

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('words')


def wordFrequency(inf):
    infile = open(inf,'r')
    file = infile.readline()
    file = str(file).rstrip()

    while(file != ""):
        tokens = word_tokenize(file)

        print("Text file:")

        print(file)
        print("\n")


        # Lemmatization
        print(" Lemmatization")
        lemmatiser = WordNetLemmatizer()
        for token in tokens:
            print(lemmatiser.lemmatize(token))

        # Bigram
        print("Bigrams:")
        n = 3
        bigrams = ngrams(file.split(), n)
        fdist = nltk.FreqDist(bigrams)
        for k, v in fdist.items():
            print(k, v)

        #Most repeated 5 bigrams
        print("Repeated 5 Bigrams")
        print(fdist.most_common(5))


        file = infile.readline()
        file = str(file).rstrip()



wordFrequency("input.txt")