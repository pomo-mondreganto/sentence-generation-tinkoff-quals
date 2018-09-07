import pickle
import random
from collections import Counter

import auxiliary


class Model:
    def __init__(self, seed=0):
        self.seed = seed
        self.data = dict()
        self.after_terminators = dict()

    def dump(self, filename):
        pickle.dump(self, file=open(filename, 'wb'))

    def fit(self, tokens):
        for i in range(len(tokens) - 2):
            key = '\1'.join([tokens[i], tokens[i + 1]])
            next_word = tokens[i + 2]
            key_hash = auxiliary.calculate_hash(key)
            if self.data.get(key_hash) is None:
                self.data[key_hash] = Counter()

            self.data[key_hash][next_word] += 1

        for i in range(len(tokens) - 1):
            if auxiliary.is_terminator(tokens[i]):
                next_word = tokens[i + 1]
                if self.after_terminators.get(tokens[i]) is None:
                    self.after_terminators[tokens[i]] = Counter()

                self.after_terminators[tokens[i]][next_word] += 1

    def generate(self, length, seed=None):
        rnd = random.Random()
        if seed is None:
            rnd.seed(self.seed)
        else:
            rnd.seed(seed)
        result = ['.', auxiliary.get_weighted_random(rnd, self.after_terminators['.'])]
        for i in range(length - 1):
            key = '\1'.join([result[-2], result[-1]])
            key_hash = auxiliary.calculate_hash(key)
            next_word = auxiliary.get_weighted_random(rnd, self.data[key_hash])
            result.append(next_word)

        return ' '.join(result)
