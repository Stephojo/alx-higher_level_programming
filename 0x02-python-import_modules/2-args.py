#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    counts= len(sys.argv) - 1
    if counts== 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(counts))
    for count in range(counts):
        print("{}: {}".format(count + 1, sys.argv[count + 1]))
