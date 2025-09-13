import os

from git import Repo


def main() -> int:
    repo = Repo(os.getcwd())
    # get staged changes
    staged_diff = repo.index.diff("HEAD")

    files_to_commit = [item.a_path for item in staged_diff]
    docs_just_build = any(file.endswith(".html") for file in files_to_commit)

    if not docs_just_build:
        os.chdir(os.getcwd() + os.sep + "src" + os.sep + "docs")
        # for windows
        # ret = os.system(".\\make.bat html")
        # for linux
        ret = os.system(".\\make html")
        return 0 if ret == 0 else 1
    else:
        return 0


if __name__ == "__main__":
    main()
