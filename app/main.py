import sys


def main():
    while (True):
        sys.stdout.write("$ ")
        command = input()
        commandFrag = command.split(" ")

        if commandFrag[0] == "echo":
            output = commandFrag[1:].join(" ")
            print(f"{output}")
            continue

        if command == "exit 0":
            return
        if command:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
