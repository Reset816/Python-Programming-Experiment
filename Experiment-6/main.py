import os


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
            filename = input_filename(display_text="Please input a filename:")
        else:
            filename = lst_list[int(number) - 1]
        return filename


def save_lines(filename, lines):
    with open(filename, "w") as f:
        f.writelines(lines)
    print("Saved {} items to {}".format(len(lines), filename))


append_newline = lambda str: str if str.endswith("\n") else str + "\n"


def get_lines(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            lines = f.readlines()
            lines[-1] = append_newline(lines[-1])
    else:
        lines = []
    return lines


def main():

    filename = get_filename()

    lines = get_lines(filename)

    while True:

        if len(lines) == 0:
            print("no items are in the list")

            x = input("[A]dd  [Q]uit  [a]: ")
            if x.upper() not in ["A", "Q"]:
                print("ERROR: invalid choice--enter one of 'AaQq'")
                input("Press Enter to continue...")
                continue
        else:
            print()
            for i in enumerate(lines, start=1):
                print(i[0], ": ", i[1], end="")

            x = input("[A]dd  [D]elete  [S]ave  [Q]uit  [a]: ")
            if x.upper() not in ["A", "D", "S", "Q"]:
                print("ERROR: invalid choice--enter one of 'AaDdSsQq'")
                input("Press Enter to continue...")
                continue

        if x.upper() == "A" or x == "":
            lines.append(append_newline(input("Add item: ")))
        elif x.upper() == "D":
            number = input("Delete item number (or 0 to cancel): ")
            if number == "0":
                continue
            lines.pop(int(number) - 1)
        elif x.upper() == "S":
            save_lines(filename, lines)
            pass
        elif x.upper() == "Q":
            confirm = input("Save unsaved changes (y/n) [y]: ")
            if confirm.lower() == "y" or x == "":
                save_lines(filename, lines)
            break


main()
