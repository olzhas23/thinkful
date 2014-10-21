import logging
import csv
import argparse
import sys

logging.basicConfig(filename="output.log", level=logging.DEBUG)


def put(name, snippet, filename):
    logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))


    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file")
        writer.writerow([name, snippet])
    logging.debug("Write sucessful")
    return name, snippet

def make_parser():
    logging.info("construcitn parser")
    description = "store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)
    return  parser

def main():
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument("filename", default="snippets.csv", nargs="?",
                            help="The snippet filename")

    return parser

if __name__=="__main__":
    main()