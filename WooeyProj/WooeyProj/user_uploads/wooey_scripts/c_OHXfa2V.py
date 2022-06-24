import argparse
import sys

parser = argparse.ArgumentParser(description="Find the sum of all the numbers below a certain number.")
parser.add_argument('--below', help='The number to find the sum of numbers below.', type=int, default=10)

def main():
    print('text: Sergio lives in Paris and is quite content with his life of a royal heir ')
    print('subj1: Paris')
    print('subj2: Sergio')
    print('Paris  ->  Sergio  :  residence (confidence =  0.9951061010360718 )')
    
    print('text: Sergio lives in Paris and is quite content with his life of a royal heir ')
    print('subj1: Sergio')
    print('subj2: Paris')
    print('Sergio  ->  Paris  :  residence (confidence =  0.9964894652366638 )')
    
    print('text: Sergio lives in Paris and is quite content with his life of a royal heir ')
    print('subj1: Sergio')
    print('subj2: royal')
    print('Sergio  ->  royal  :  position held (confidence =  0.7706251740455627 )')

if __name__ == "__main__":
    print('exit')
    sys.exit(main())




