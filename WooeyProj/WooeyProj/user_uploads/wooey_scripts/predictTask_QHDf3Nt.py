import argparse
import sys
import os
import opennre
import predict
from transformers import logging
logging.set_verbosity_error()

parser = argparse.ArgumentParser(description="Predict a relation between 2 subjects in a sentence")
parser.add_argument('--text', help='Sentence to extract relation from.', type=str, default='Sergio lives in Paris and is quite content with his life of a royal heir')
parser.add_argument('--subj1', help='Subject 1', type=str, default='Sergio')
parser.add_argument('--subj2', help='Subject 2', type=str, default='Paris')

def main():
    args = parser.parse_args()
    res = predict.predict(args.text, args.subj1, args.subj2)
    print(res)
    
if __name__ == "__main__":  
    sys.exit(main())