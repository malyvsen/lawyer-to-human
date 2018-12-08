from sentence import Sentence


class Document:
    def __init__(self, sentences, metadata):
        self.sentences = sentences
        self.metadata = metadata


    @classmethod
    def from_text(text):
        sentences = [Sentence.from_text(sentence_text) for sentence_text in text.split('.')]
        sentences = [sentence for sentence in sentences if sentence is not None]
        return cls(sentences, [])
