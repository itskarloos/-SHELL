import sys
import os


def main():

    sys_path = os.environ["PATH"].split(":")

    path_file = {

    }
    for paths in sys_path:
        path_file[paths.split("/")[1]] = paths
        path_file["cat"] = "/bin/cat"
        path_file["ls"] = "/usr/bin/ls"
        path_file["cp"] = "/bin/cp"
        path_file["mkdir"] = "/bin/mkdir"
        path_file["my_exe"] = "/tmp/baz/my_exe"

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
                continue
            else:
                print(f"{commandFrag[1]}: not found")
                continue
        if command == "exit 0":
            return
        if command:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
