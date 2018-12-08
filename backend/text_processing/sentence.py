from word import Words


class Sentence:
    def __init__(self, words):
        self.words = words


    @classmethod
    def from_text(cls, text):
        words = [Word.from_text(word_text) for word_text in text.split(' ')]
        words = [word for word in words if word is not None] # remove parsing failures
        if len(words) == 0:
            return None
        return cls(words)
