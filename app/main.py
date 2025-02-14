import sys


def main():
    while (True):
        sys.stdout.write("$ ")
        command = input()
        commandFrag = command.split(" ")

        if commandFrag[0] == "echo":
            print(f"{commandFrag[1:].join(" ")}")
            continue

        if command == "exit 0":
            return
        if command:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
