#!/usr/bin/python

import libxml2
import argparse
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def printEntry(entry):
  idx = entry.xpathEval('.//no').pop( ).content
  print "Item", idx
  params = entry.xpathEval('.//para')
  for param in params:
    print "  ", param.content
    admonishments = param.xpathEval("./parent::*/child::eqnotavail")
    for admonish in admonishments:
      print "    (w) ", admonish.content
      
def main(args):
  logger.info("Hello World")
  name = args.input
  logger.info(name)
  root = libxml2.parseFile(name)
  for entry in root.xpathEval('//entry'):
    printEntry(entry)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='fun with xml')
  parser.add_argument('-i', '--input')
  args = parser.parse_args( )
  main(args)
  

#####
# EOF
