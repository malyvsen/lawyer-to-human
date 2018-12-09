from text_processing.word import Word
from text_processing.lemma_count import LemmaCount


class Sentence:
    def __init__(self, words, ending):
        self.words = words
        self.ending = ending
        self.lemma_count = self.lemma_count()
        self.text = self.text()


    @classmethod
    def from_text(cls, text, ending='.'):
        words = list(Word.generator(text))
        if len(words) == 0:
            return None
        return cls(words, ending)


    @classmethod
    def generator(cls, text):
        separators = '.?!'
        while len(text) > 0:
            positions = {separator: text.find(separator) for separator in separators}
            positions = {separator: positions[separator] for separator in separators if positions[separator] > -1}
            position_extractor = lambda separator: positions[separator]
            next_separator = min(positions, key=position_extractor) if len(positions) > 0 else None
            if next_separator is None:
                result = cls.from_text(text)
                if result is not None:
                    yield result
                return
            result = cls.from_text(text[:positions[next_separator]], next_separator)
            if result is not None:
                yield result
            text = text[positions[next_separator] + 1:]


    def lemma_count(self):
        result = LemmaCount()
        for word in self.words:
            result.register_word(word)
        return result


    def text(self):
        return ' '.join(word.text for word in self.words) + self.ending


    def __str__(self):
        return f'Sentence with {len(self.words)} words, {len(self.lemma_count.count)} unique words:\n{self.text}'
