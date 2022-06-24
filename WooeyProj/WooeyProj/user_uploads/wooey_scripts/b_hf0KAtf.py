import argparse
import sys
import os
import opennre
import logging




parser = argparse.ArgumentParser(description="Predict a relation between 2 subjects in a sentence")
parser.add_argument('--text', help='Sentence to extract relation from.', type=str, default='Sergio lives in Paris and is quite content with his life of a royal heir')
parser.add_argument('--subj1', help='Subject 1', type=str, default='Sergio')
parser.add_argument('--subj2', help='Subject 2', type=str, default='Paris')

def main():
    print('exit')
    return 0

if __name__ == "__main__":  
    print('exit')
    logging.basicConfig(filename='N:/__ВАЖНОЕ/_Универ/магистратура 2 Семестр/Нейронки/курс/asd.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)  
    old_stdout = sys.stdout # backup current stdout
    print('exit')
    sys.stdout = open('N:/__ВАЖНОЕ/_Универ/магистратура 2 Семестр/Нейронки/курс/asd.txt', "a")
    args = parser.parse_args()
    model = opennre.get_model('wiki80_bert_softmax')
    sys.stdout = old_stdout # reset old stdout
    h1 = args.text.find(args.subj1)
    h2 = h1+len(args.subj1)
    t1 = args.text.find(args.subj2)
    t2 = t1+len(args.subj2)
    print('exit')

    res = model.infer({
    'text': text, 
    'h': {'pos': (h1, h2)}, 
    't': {'pos': (t1, t2)}
    })
    print(args.subj1, ' -> ' , args.subj2, " : ", res[0],  '(confidence = ',res[1],")")
    print('exit')
    print('exit')
    print('exit')
    print('exit')
    sys.exit(main())