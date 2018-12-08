import string
from spacy.lang.pl import STOP_WORDS as stop_words


class Word:
    def __init__(self, text, lemma):
        self.text = text
        self.lemma = lemma


    @classmethod
    def from_text(cls, text):
        if len(text) == 0:
            return None
        lemma = text.strip(string.punctuation)
        if len(lemma.strip(string.digits)) == 0:
            lemma = '#NUMERIC'
        return cls(text, lemma)


    def is_stop(self):
        return self.text in stop_words or self.lemma in stop_words


    def __str__(self):
        return self.text
