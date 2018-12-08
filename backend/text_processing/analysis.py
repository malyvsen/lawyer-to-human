from text_processing.document import Document


class Analysis:
    def __init__(self, text):
        doc = Document.from_text(text)
        if doc is None:
            self.text = 'Nie udało się przeanalizować dokumentu.'
            self.selections = []
            self.metadata = []
            return

        self.text = doc.text
        self.selections = []
        for underlined_sentence in doc.underlined_sentences:
            start = self.text.find(underlined_sentence.text)
            end = start + len(underlined_sentence.text)
            selection = Selection('underline', start, end)
            self.selections.append(selection)
        self.metadata = [Metadatum('summary', text=doc.summary.text)]


class Selection:
    def __init__(self, type, start, end, **kwargs):
        self.type = type
        self.position = (start, end)
        for key in kwargs:
            setattr(self, key, kwargs[key])


class Metadatum:
    def __init__(self, type, **kwargs):
        self.type = type
        for key in kwargs:
            setattr(self, key, kwargs[key])
