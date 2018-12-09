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
        words = [Word.from_text(word_text) for word_text in text.split(' ')]
        words = [word for word in words if word is not None] # remove parsing failures
        if len(words) == 0:
            return None
        return cls(words, ending)


    def lemma_count(self):
        result = LemmaCount()
        for word in self.words:
            result.register_word(word)
        return result


    def text(self):
        return ' '.join(word.text for word in self.words) + self.ending


    def find_ending(text):
        endings = '.?!\n'
        positions = [text.find(ending) for ending in endings]
        positions = [position for position in positions if position > -1]
        return min(positions) if len(positions) > 0 else -1


    def __str__(self):
        return f'''Sentence with {len(self.words)} words, {len(self.lemma_count.count)} unique words:
        {self.text}'''
