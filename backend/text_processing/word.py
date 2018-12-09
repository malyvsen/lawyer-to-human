import string
from spacy.lang.pl import STOP_WORDS as stop_words
try:
    import morfeusz2
    morph = morfeusz2.Morfeusz()
except ImportError:
    print('Warning: Morfeusz couldn\'t be imported')
    morph = None

letters = string.ascii_letters + 'ąćęłńóśźż'


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


    @classmethod
    def generator(cls, text):
        separators = string.whitespace
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
            result = cls.from_text(text[:positions[next_separator] + 1])
            if result is not None:
                yield result
            text = text[positions[next_separator] + 1:]


    def lemma(self):
        if self.text.find(string.digits) > -1:
            return '#NUMERIC'
        main_text = ''.join(char for char in self.text if char in letters)
        if morph is None:
            return main_text
        morph_analysis = morph.analyse(main_text)
        if len(morph_analysis) == 0:
        	return main_text
        return morph_analysis[0][2][1].split(':')[0]


    def is_stop(self):
        return self.text in stop_words or self.lemma in stop_words


    def __str__(self):
        return self.text
