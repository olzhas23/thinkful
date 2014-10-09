import logging
import csv

logging.basicConfig(filename="output.log", level=logging.DEBUG)

def put(name,filename,snippet):
	    logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
    	logging.debug("Opening file")
    	with open(filename, "a") as f:
        	writer = csv.writer(f)

