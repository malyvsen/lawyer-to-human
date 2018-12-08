from sentence import Sentence
from lemma_count import LemmaCount
from functools import reduce


class Document:
    def __init__(self, sentences, metadata):
        self.sentences = sentences
        self.metadata = metadata


    @classmethod
    def from_text(text):
        sentences = [Sentence.from_text(sentence_text) for sentence_text in text.split('.')]
        sentences = [sentence for sentence in sentences if sentence is not None]
        return cls(sentences, [])


    def lemma_count(self):
        sentence_lemma_counts = [sentence.lemma_count() for sentence in self.sentences]
        return reduce(lambda a, b: a + b, sentence_lemma_counts, initial=LemmaCount())


    def __str__(self):
        return ' '.join(str(sentence))
