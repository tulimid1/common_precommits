import os


def main() -> int:
    # change to src folder
    os.chdir(os.getcwd() + os.sep + "src")
    # call sphinx to force build docs
    # if want to exlucde something, put name between . and --force
    ret = os.system("sphinx-apidoc -o docs . --force")
    return 0 if ret == 0 else 1


if __name__ == "__main__":
    main()
