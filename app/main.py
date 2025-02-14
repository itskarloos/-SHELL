import sys


def main():
    while (True):
        sys.stdout.write("$ ")
        command = input()
        commandFrag = command.split(" ")

        if commandFrag[0] == "echo":
            output = commandFrag[1:]
            result = " ".join(output)
            print(f"{result}")
            continue
        if commandFrag[0] == "type":
            if commandFrag[1] == "echo" or commandFrag[1] == "exit":
                print(f"{commandFrag[1]} is a shell builtin ")
            else:
                print(f"{commandFrag[1]}: not found")
        if command == "exit 0":
            return
        if command:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
