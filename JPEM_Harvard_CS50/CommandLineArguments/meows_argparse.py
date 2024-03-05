import argparse

parser = argparse.ArgumentParser(description="meow like a cat")  #constructor or class that comes with argparse

parser.add_argument("-n", default=1, help = "number of times to meow", type=int)
args = parser.parse_args()  #automatically looks at sys.arv automatically

for _ in range(int(args.n)):
    print("meow")
