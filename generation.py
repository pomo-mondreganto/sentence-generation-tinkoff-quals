import argparse
import pickle

from model import Model

parser = argparse.ArgumentParser(description='Generate text with given token amount using pre-trained model.')

parser.add_argument('-m',
                    '--model',
                    help='Model dump filename.'
                         'Trained model dump',
                    required=True
                    )

parser.add_argument('-s', '--seed', type=int,
                    help='Seed for model generation. model\'s seed by default',
                    default=0)

parser.add_argument('-l', '--length', type=int,
                    help='Length of output (in tokens)',
                    default=0)

args = parser.parse_args()

model = pickle.load(file=open(args.model, 'rb'))
assert isinstance(model, Model)

result = model.generate(args.length, args.seed)

print(result)
