import os
import sys


def get_filename():
    def input_filename(display_text):
        filename = input(display_text)
        if not filename.endswith(".lst"):
            filename += ".lst"
        return filename

    lst_list = []
    for filename in os.listdir("."):
        if filename.endswith(".lst"):
            lst_list.append(filename)

    try:
        if len(lst_list) == 0:
            filename = input_filename(
                display_text="No .lst files found. Please input a filename:"
            )
        elif len(lst_list) != 0:
            for i in enumerate(lst_list, start=1):
                print(i[0], ": ", i[1])
            number = input(
                "Please input the number of file to be loaded, 0 to give a file name for a new file: "
            )
            if number == "0":
                filename = input_filename(display_text="Please input a filename: ")
            elif int(number) < 0:
                raise ValueError()
            else:
                filename = lst_list[int(number) - 1]
        print("Choose filename: ", filename)
        return filename
    except:
        print(number, " is not vaild index")
        sys.exit()


def save_lines(filename, lines):
    with open(filename, "w") as f:
        f.writelines(lines)
    print("Saved {} items to {}".format(len(lines), filename))


append_newline = lambda str: str if str.endswith("\n") else str + "\n"


def get_lines(filename):
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            lines = f.readlines()
            if lines != []:
                lines[-1] = append_newline(lines[-1])
    else:
        lines = []
    return sorted(lines, key=str.lower)


def options(len_of_lines, is_dirty):
    list_of_options = ["A", "Q"]

    while True:

        print("[A]dd  ", end="")
        if len_of_lines != 0:
            print("[D]elete  ", end="")
            list_of_options.append("D")
        if is_dirty == True:
            print("[S]ave  ", end="")
            list_of_options.append("S")
        print("[Q]uit  [a]: ", end="")

        x = input()
        if (x.upper() not in list_of_options) and x != "":
            print("ERROR: invalid choice")
            input("Press Enter to continue...")
            continue
        else:
            return x


def print_lines(lines):
    if len(lines) == 0:
        print("\nno items are in the list")

    else:
        print()
        width = len(str(len(lines)))
        for i in enumerate(lines, start=1):
            print(f"{i[0]:>{width}d}: {i[1]}", end="")


def main():

    filename = get_filename()

    lines = get_lines(filename)

    while True:

        print_lines(lines)
        is_dirty = lines != get_lines(filename)
        x = options(len_of_lines=len(lines), is_dirty=is_dirty)

        if x.upper() == "A" or x == "":
            lines.append(append_newline(input("Add item: ")))
            lines = sorted(lines, key=str.lower)
        elif x.upper() == "D":
            number = input("Delete item number (or 0 to cancel): ")
            if number == "0":
                continue
            lines.pop(int(number) - 1)
        elif x.upper() == "S":
            save_lines(filename, lines)
        elif x.upper() == "Q":
            if is_dirty == True:
                confirm = input("Save unsaved changes (y/n) [y]: ")
                if confirm.lower() == "y" or confirm == "":
                    save_lines(filename, lines)
                else:
                    continue
            break


main()
