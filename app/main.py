import sys


def main():
    path_file = {
        "ls": "/usr/bin/ls",
        "valid_command": "/usr/local/bin/valid_command",
    }
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
            if commandFrag[1] == "echo" or commandFrag[1] == "exit" or commandFrag[1] == "type":
                print(f"{commandFrag[1]} is a shell builtin ")
                continue
            elif commandFrag[1] in path_file:
                print(f"{commandFrag[1]} is {path_file[commandFrag[1]]}")
            else:
                print(f"{commandFrag[1]}: not found")
                continue
        if command == "exit 0":
            return
        if command:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
