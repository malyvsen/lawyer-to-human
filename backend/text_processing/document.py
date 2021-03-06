from text_processing.sentence import Sentence
from text_processing.lemma_count import LemmaCount
from functools import reduce


class Document:
    def __init__(self, sentences, generate_summary=True):
        self.sentences = sentences
        self.lemma_count = self.lemma_count()
        self.underlined_sentences = self.underlined_sentences()
        self.summary = self.summary() if generate_summary else None
        self.text = self.text()


    @classmethod
    def from_text(cls, text):
        sentences = list(Sentence.generator(text))
        if len(sentences) == 0:
            return None
        return cls(sentences)


    def lemma_count(self):
        sentence_lemma_counts = [sentence.lemma_count for sentence in self.sentences]
        return reduce(lambda a, b: a + b, sentence_lemma_counts, LemmaCount())


    def underlined_sentences(self, num_underlines=None):
        longer_sentences = [sentence for sentence in self.sentences if len(sentence.words) > 5]
        if num_underlines is None:
            num_underlines = int(len(longer_sentences) ** .5)

        score = lambda sentence: self.lemma_count.cosine(sentence.lemma_count)
        sorted_sentences = sorted(longer_sentences, key=score, reverse=True)

        order = lambda sentence: self.sentences.index(sentence)
        result = sorted(sorted_sentences[:num_underlines], key=order)
        return result


    def summary(self):
        if len(self.underlined_sentences) == 0:
            return None
        return Document(self.underlined_sentences, generate_summary=False)


    def text(self):
        return ' '.join(sentence.text for sentence in self.sentences)


    def __str__(self):
        return f'Document with {len(self.sentences)} sentences, {len(self.lemma_count.count)} unique words:\n{self.text}'
