import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display Square of any given argument", type=int)
args=parser.parse_args()

print args.square**2

