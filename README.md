# Sentence generation for Tinkoff quals
Repository for sentence generation project. 


### Usage: 

##### [training.py](training.py)

```
Fit the model

arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input text filename
  -m MODEL, --model MODEL
                        Model dump filename. New model will be created if file
                        is missing or doesn't contain valid model
  -s SEED, --seed SEED  Seed for model generation. 0 by default, optional

```

##### [generation.py](generation.py)

```
Generate text with given token amount using pre-trained model.

arguments:
  -h, --help            show this help message and exit
  -m MODEL, --model MODEL
                        Model dump filename. Trained model dump
  -s SEED, --seed SEED  Seed for model generation. model's seed by default, optional
  -l LENGTH, --length LENGTH
                        Length of output (in tokens)

```
