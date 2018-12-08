from word import Words
from lemma_count import LemmaCount


class Sentence:
    def __init__(self, words):
        self.words = words
        self.lemma_count = self.lemma_count()


    @classmethod
    def from_text(cls, text):
        words = [Word.from_text(word_text) for word_text in text.split(' ')]
        words = [word for word in words if word is not None] # remove parsing failures
        if len(words) == 0:
            return None
        return cls(words)


    def lemma_count(self):
        result = LemmaCount()
        for word in self.words:
            result.register_word(word)
        return result


    def __str__(self):
        return ' '.join(str(word) for word in self.words) + '.'
