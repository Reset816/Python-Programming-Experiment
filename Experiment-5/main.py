import datetime


def get_date():

    try:
        date = input("please input date in format YYYY-MM-DD:")
        date = date.split("-")
        if len(date) != 3:
            raise ValueError()
        date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        return date
    except ValueError:
        print("Invalid date")
        exit()


def get_index(date):
    return int(date.strftime("%Y") + date.strftime("%m") + date.strftime("%d"))


def get_gender():

    try:
        gender = input("please input gender, male or female:")
        if gender != "male" and gender != "female":
            raise ValueError()
        else:
            return gender
    except ValueError:
        print("Invalid gender")
        exit()


# read Chinese from a file
def get_name(gender, index):
    if gender == "male":
        filename = "boy.txt"
    else:
        filename = "girl.txt"

    with open(filename, "r", encoding="UTF-8") as f:
        database = f.readlines()
        return database[index % len(database)].split("\n")[0]


def main():
    name = get_name(gender=get_gender(), index=get_index(get_date()))
    print(name)


main()
