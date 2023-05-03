import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def print_maturity(age):
    if age >= 18:
        print("You are adult")
    else:
        print("You are kiddo")
        
if __name__ == "__main__":
    logging.debug("This program was called with this parameter %s" % sys.argv[1:])
    logging.debug("The first parameter is %s" % sys.argv[1])
    age = int(sys.argv[1])
    print_maturity(age)