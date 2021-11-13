import  argparse

import os
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument ('--id', type=str, default='anonymous', help='id')
    parser.add_argument ('--file', type=str, default='file.txt', help='file')
    args = parser.parse_args()

print(args.id+args.file)
#print(args.file)