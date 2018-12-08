import string


class Word:
    def __init__(self, text):
        pass


    @classmethod
    def from_text(cls, text):
        word_text = text.strip(string.punctuation)
        if len(word_text) == 0:
            return None
        return cls(text)
