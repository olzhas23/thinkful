__author__ = 'Olzhas'
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("echo")
args=parser.parse_args()
print (args.echo)
