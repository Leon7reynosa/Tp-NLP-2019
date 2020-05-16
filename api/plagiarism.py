from nltk import bigrams, word_tokenize
from nltk.corpus import stopwords


def jaccard_similarity_coefficient(suspect_n_grams: set, original_n_grams: set):
    return len(suspect_n_grams.intersection(original_n_grams)) / len(suspect_n_grams.union(original_n_grams))


def get_text_bygrams(text):
    filtered_words = [word.lower() for word in word_tokenize(
        text) if word not in stopwords.words('spanish')]
    return set(bigrams(filtered_words))


def may_be_plagiarism_of(suspect, original, threshold=0.2):
    bigrams_original = get_text_bygrams(original)
    bigrams_suspect = get_text_bygrams(suspect)
    print(bigrams_original)
    print(bigrams_suspect)
    coefficient = jaccard_similarity_coefficient(
        bigrams_suspect, bigrams_original)
    return coefficient > threshold
