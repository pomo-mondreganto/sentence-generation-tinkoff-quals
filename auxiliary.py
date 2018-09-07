import itertools
import re
from hashlib import md5

TOKEN_REGEX = re.compile('[a-z0-9\']+|[.!?]{1,3}|\w-\w]')
TERMINATORS = re.compile('[.!?]{1,3}')


def tokenize(filename):
    text = open(filename).read()
    text = text.lower()
    tokens = ['.'] + TOKEN_REGEX.findall(text)
    return tokens


def is_terminator(token):
    return TERMINATORS.match(token)


def calculate_hash(s):
    return md5(s.encode()).hexdigest()


def get_weighted_random(rnd, counter):
    i = rnd.randrange(sum(counter.values()))
    return next(itertools.islice(counter.elements(), i, None))
