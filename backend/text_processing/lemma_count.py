class LemmaCount:
    def __init__(self, count=None):
        if count is None:
            count = {}
        self.count = count


    def register_word(self, word):
        if word.is_stop:
            return
        if word.lemma not in self.count:
            self.count[word.lemma] = 1
            return
        self.count[word.lemma] += 1


    def dot(self, other):
        result = 0
        for lemma in self.count:
            if lemma in other.count:
                result += self.count[lemma] * other.count[lemma]
        return result


    def cosine(self, other):
        norm_product = self.norm() * other.norm()
        if norm_product == 0:
            return 0
        return self.dot(other) / norm_product


    def norm(self):
        return self.dot(self) ** .5


    def normalized(self):
        norm = self.norm()
        return LemmaCount({lemma: self.count[lemma] / norm for lemma in self.count})


    def __add__(self, other):
        count = {lemma: 0 for lemma in list(self.count) + list(other.count)}
        for lemma in self.count:
            count[lemma] += self.count[lemma]
        for lemma in other.count:
            count[lemma] += other.count[lemma]
        return LemmaCount(count)


    def __str__(self):
        return str(self.count)
