from text_processing.sentence import Sentence
from text_processing.lemma_count import LemmaCount
from functools import reduce


class Document:
    def __init__(self, sentences):
        self.sentences = sentences
        self.lemma_count = self.lemma_count()
        self.underlined_sentences = self.underlined_sentences()


    @classmethod
    def from_text(cls, text):
        sentences = [Sentence.from_text(sentence_text) for sentence_text in text.split('.')]
        sentences = [sentence for sentence in sentences if sentence is not None]
        return cls(sentences)


    def lemma_count(self):
        sentence_lemma_counts = [sentence.lemma_count for sentence in self.sentences]
        return reduce(lambda a, b: a + b, sentence_lemma_counts, LemmaCount())


    def underlined_sentences(self, num_underlines=None):
        if num_underlines is None:
            num_underlines = len(self.sentences) // 4
        score = lambda sentence: self.lemma_count.dot(sentence.lemma_count)
        result = sorted(self.sentences, key=score, reverse=True)[:num_underlines]
        return result


    def __str__(self):
        return ' '.join(str(sentence) for sentence in self.sentences)
