import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    contents = dict()

    for file in os.listdir(directory):
        filePath = os.path.join(directory, file)
        with open(filePath, 'r') as f:
            text = f.read()
            contents[file] = text

    return contents



def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """

    # Convert to lowercase
    document = document.lower()

    # Tokenization
    words = nltk.word_tokenize(document)

    # Filtering stoprwords and punctuation
    filteredWords = []
    for word in words:
        if word not in nltk.corpus.stopwords.words("english") and word not in string.punctuation:
            filteredWords.append(word)
    
    return filteredWords



def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    freq = dict()
    for doc in documents:
        for word in set(documents[doc]):
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

    idfs = dict()
    for word in freq:
        idfs[word] = math.log(len(documents)/freq[word])

    return idfs



def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """

    # Calculate the sum of tf-idf for each file
    tfidf = dict()
    for file in files:
        tfidf[file] = 0
        for word in query:
            tfidf[file] += files[file].count(word) * idfs[word]

    # Sort the files in decending order
    allRankedFiles = dict(sorted(tfidf.items(), key = lambda item: item[1], reverse = True))

    # Return the top n files
    nRankedFiles = list(allRankedFiles.keys())[:n]
    return nRankedFiles


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """

    # Filter out sentences that do Not contain any word in the query to make it more efficient
    qsentences = {sentence: tokens for sentence, tokens in sentences.items() if any(word in tokens for word in query)}

    # Matching Word Measure
    mwm = dict() 
    for sentence in qsentences:
        # mwm[sentence][0] represents the sum of idf.
        # mwm[sentence][1] represents the count of the word to calculate its qtd later.
        mwm[sentence] = [0,0]
        for word in query:
            if word in qsentences[sentence]:
                mwm[sentence][0] += idfs[word]
                mwm[sentence][1] += qsentences[sentence].count(word)

    # Calculating "Query Term Density" 
    for sentence in qsentences:
        mwm[sentence][1] = mwm[sentence][1] / len(qsentences[sentence])

    # Sort the sentences in decending order
    allRankedSentences = dict(sorted(mwm.items(), key = lambda item: (item[1][0], item[1][1]), reverse = True))

    # Return the top n sentences
    nRankedSentences = list(allRankedSentences.keys())[:n]
    return nRankedSentences


if __name__ == "__main__":
    main()
