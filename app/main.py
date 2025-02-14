from telnetlib import DO
import sys


def main():
    while (True):
        sys.stdout.write("$ ")
        command = input()
        if command:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
