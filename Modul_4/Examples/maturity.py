import sys

def print_maturity(age):
    if age >= 18:
        print("You are adult")
    else:
        print("You are kiddo")
        
if __name__ == "__main__":
    age = int(sys.argv[1])
    print_maturity(age)
    print("This program was called with parameters %s" % sys.argv[1:])
#    print("The first parameter is %s" % sys.argv[1])