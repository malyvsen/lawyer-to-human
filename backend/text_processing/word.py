import string
from spacy.lang.pl import STOP_WORDS as stop_words


class Word:
    def __init__(self, text):
        self.text = text
        self.lemma = self.lemma()
        self.is_stop = self.is_stop()


    @classmethod
    def from_text(cls, text):
        if len(text) == 0:
            return None
        return cls(text)


    def lemma(self):
        result = self.text.strip(string.punctuation)
        if len(result.strip(string.digits)) == 0:
            result = '#NUMERIC'
        return result


    def is_stop(self):
        return self.text in stop_words or self.lemma in stop_words


    def __str__(self):
        return self.text
