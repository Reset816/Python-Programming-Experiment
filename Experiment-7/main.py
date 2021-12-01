import argparse
import os
from datetime import datetime


class File:
    def __init__(self, root, name):
        self.root = root
        self.name = name
        self.modified_time = datetime.fromtimestamp(
            os.path.getmtime(os.path.join(root, name))
        )
        self.size = os.path.getsize(os.path.join(root, name))


class Folder:
    def __init__(self, root, name):
        self.root = root
        self.name = name


# sort the list with parameter in args:
def sort_list(list, args):
    if args.order == "name" or args.order == "n":
        list.sort(key=lambda x: x.name)
    elif args.order == "modified" or args.order == "m":
        list.sort(key=lambda x: x.modified_time)
    elif args.order == "size" or args.order == "s":
        list.sort(key=lambda x: x.size)
    return list


def get_list(args):
    files_list = []
    folders_list = []
    for dir in args.dir:
        if args.recursive:
            # os.walk 会依次遍历 dirs
            for root, dirs, files in os.walk(
                dir
            ):  # Topdown parameter will affect output
                if not args.hidden:  # if do not show hidden files
                    # code below won't change dirs pointer, so it will affect the traverse of files
                    dirs[:] = [
                        item for item in dirs if not item.startswith(".")
                    ]  # remove hidden folders
                    files[:] = [
                        item for item in files if not item.startswith(".")
                    ]  # remove hidden files
                for item in dirs:
                    folders_list.append(Folder(root, item))
                for item in files:
                    files_list.append(File(root, item))

        else:
            list_dir = os.listdir(dir)
            if not args.hidden:
                list_dir[:] = [
                    item for item in list_dir if not item.startswith(".")
                ]  # remove hidden item
            for item in list_dir:
                if os.path.isfile(os.path.join(dir, item)):
                    files_list.append(File(dir, item))
                else:
                    folders_list.append(Folder(dir, item))

    return files_list, folders_list


def print_list(args, files_list, folders_list):
    count = 0
    if args.modified and len(files_list) != 0:
        count += (
            int(len(files_list[0].modified_time.isoformat(" ", timespec="seconds")) / 8)
            + 1
        )  # \t是补全8个字符
    if args.size and len(files_list) != 0:
        maxsize = max(files_list, key=lambda x: x.size).size
        count += int(len(str(maxsize)) / 8) + 1

    for item in files_list:
        if args.modified:
            print(item.modified_time.isoformat(" ", timespec="seconds"), end="\t")
        if args.size:
            print(item.size, end="\t")
        print(os.path.join(item.root, item.name))

    for item in folders_list:
        print("\t" * count, end="")
        print(os.path.join(item.root, item.name))
    print("{} file(s) {} directory(s)".format(len(files_list), len(folders_list)))


# use argparse to get options
def argument_parser():
    parser = argparse.ArgumentParser(
        description="The paths are optional; if not given . is used."
    )
    parser.add_argument(
        "dir",
        nargs="*",
        default=["."],
    )
    parser.add_argument(
        "-H",
        "--hidden",
        action="store_true",
        help="show hidden files [default: off]",
    )
    parser.add_argument(
        "-m",
        "--modified",
        action="store_true",
        help="show last modified date/time [default: off]",
    )
    parser.add_argument(
        "-o",
        "--order",
        choices=["name", "n", "modified", "m", "size", "s"],
        default="name",
        help="order by ('name', 'n', 'modified', 'm', 'size', 's') default: name",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="recursive into subdirectories [default: off]",
    )
    parser.add_argument(
        "-s",
        "--size",
        action="store_true",
        help="show size [default: off]",
    )

    return parser.parse_args()


def main():
    args = argument_parser()

    files_list, folders_list = get_list(args)

    files_list = sort_list(files_list, args)

    print_list(args, files_list, folders_list)


main()
