import sys
import os
import shutil
import subprocess


def main():

    sys_path = os.environ["PATH"].split(os.pathsep)

    path_file = {
        "cat": "/bin/cat",
        "ls": "/usr/bin/ls",
        "cp": "/bin/cp",
        "mkdir": "/bin/mkdir",
        "my_exe": "/tmp/quz/my_exe",
    }

    for paths in sys_path:
        parts = paths.split("/")
        if len(parts) > 1:
            path_file[parts[1]] = paths

    while True:
        sys.stdout.write("$ ")
        command = input().strip()
        if not command:
            continue

        commandFrag = command.split(" ")

        program = commandFrag[0]

        # Check if it's a built-in command
        match program:
            case "echo":
                print(" ".join(commandFrag[1:]))

            case "type":
                if commandFrag[1] in ["echo", "exit", "type", "pwd"]:
                    print(f"{commandFrag[1]} is a shell builtin")
                elif shutil.which(commandFrag[1]):  # Check if it's in PATH
                    print(f"{commandFrag[1]} is {
                          shutil.which(commandFrag[1])}")

        if os.path.isfile(commandFrag[0]):
            os.system(command)
            continue

        match commandFrag[0]:
            case "echo":
                output = commandFrag[1:]
                print(" ".join(output))
            case "pwd":
                print(os.getcwd(command))
            case "type":
                if commandFrag[1] in ["echo", "exit", "type"]:
                    print(f"{commandFrag[1]} is a shell builtin")
                elif commandFrag[1] in path_file:
                    print(f"{commandFrag[1]} is {path_file[commandFrag[1]]}")

                else:
                    print(f"{commandFrag[1]}: not found")

            case "exit":
                exit_code = int(commandFrag[1]) if len(commandFrag) > 1 else 0
                sys.exit(exit_code)

            case _:
                executable_path = shutil.which(program)
                if executable_path:  # If found in PATH, execute it
                    try:
                        subprocess.run(commandFrag)  # Run with arguments
                    except Exception as e:
                        print(f"Error executing {program}: {e}")
                else:
                    print(f"{program}: command not found")


if __name__ == "__main__":
    main()
