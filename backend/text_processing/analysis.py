import re
from text_processing.document import Document
from text_processing.difficult import definitions


def analysis(text):
    doc = Document.from_text(text)
    if doc is None:
        return {
        'text': 'Nie udało się przeanalizować dokumentu.',
        'selections': [],
        'metadata': []
        }

    selections = []
    for underlined_sentence in doc.underlined_sentences:
        start = doc.text.find(underlined_sentence.text)
        end = start + len(underlined_sentence.text)
        selection = {'type': 'underline', 'position': (start, end)}
        selections.append(selection)
    for difficult_word in definitions:
        for occurence in re.finditer(difficult_word, doc.text):
            selection = {
            'type': 'definition',
            'position': (occurence.start(), occurence.end()),
            'description': definitions[difficult_word]
            }
            selections.append(selection)
    metadata = [{'type': 'summary', 'text': doc.summary.text}]
    return {
        'text': doc.text,
        'selections': selections,
        'metadata': metadata
    }
