import argparse
import sys
import os
import opennre





parser = argparse.ArgumentParser(description="Predict a relation between 2 subjects in a sentence")
parser.add_argument('--text', help='Sentence to extract relation from.', type=str, default='Sergio lives in Paris and is quite content with his life of a royal heir')
parser.add_argument('--subj1', help='Subject 1', type=str, default='Sergio')
parser.add_argument('--subj2', help='Subject 2', type=str, default='Paris')




#print('input text here')
#text = input()
#print('input key word 1 for RE here')
#word = input()
#print('input key word 2 for RE here')
#word2 = input()




#def getRes():
#    args = parser.parse_args()
#    model = opennre.get_model('wiki80_bertentity_softmax')
#
#    h1 = args.text.find(args.subj1)
#    h2 = h1+len(args.subj1)
#    t1 = args.text.find(args.subj2)
#    t2 = t1+len(args.subj2)
#
#    res = model.infer({
#    'text': text, 
#    'h': {'pos': (h1, h2)}, 
#    't': {'pos': (t1, t2)}
#    })
#    a = (args.subj1, res[0], args.subj2, 'confidence = ',res[1])
#    return(a)
#
#def main():
#    old_stdout = sys.stdout # backup current stdout
#    sys.stdout = open(os.devnull, "w")
#    a = getRes()
#    print(a[0],a[1],a[2],a[3],a[4])
#    sys.stdout = old_stdout # reset old stdout
#    return 0


def main():
    args = parser.parse_args()
    model = opennre.get_model('wiki80_bertentity_softmax')
    h1 = args.text.find(args.subj1)
    h2 = h1+len(args.subj1)
    t1 = args.text.find(args.subj2)
    t2 = t1+len(args.subj2)
    res = model.infer({
    'text': text, 
    'h': {'pos': (h1, h2)}, 
    't': {'pos': (t1, t2)}
    })
    print()
    print(args.subj1, res[0], args.subj2, 'confidence = ',res[1])
    return(0)

if __name__ == "__main__":
    print('exit')
    sys.exit(main())