import argparse

parser = argparse.ArgumentParser(description="Some function")

parser.add_argument("-a","--add", help="to add", type=int, metavar='')
args = parser.parse_args()

if __name__ == "__main__":
    print(args.add)