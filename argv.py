import sys

def main():
    n = 10

#argv is a list of command line arguments given when running th eprogram
#ex. when running with $python argv.py 24, argv.py is the first arguement and 24 is the second argument

    if len(sys.argv) > 1: 

        #access element 1 of the list of command line arguemnts
        n = int(sys.argv[1])

    print(n)


if __name__ == "__main__":
    main()
