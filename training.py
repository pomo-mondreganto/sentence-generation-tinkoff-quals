import argparse
import pickle

import auxiliary
from model import Model

parser = argparse.ArgumentParser(description='Fit the model')
parser.add_argument('-i', '--input', help='Input text filename', required=True)

parser.add_argument('-m',
                    '--model',
                    help='Model dump filename.'
                         'New model will be created if file is missing or doesn\'t contain valid model',
                    required=True
                    )

parser.add_argument('-s', '--seed', type=int,
                    help='Seed for model generation. 0 by default',
                    default=0)

args = parser.parse_args()

tokens = auxiliary.tokenize(args.input)

try:
    model = pickle.load(file=open(args.model, 'rb'))
    assert isinstance(model, Model)
except:
    model = Model()

model.fit(tokens=tokens)

model.dump(args.model)
