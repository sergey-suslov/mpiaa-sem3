import random


months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def read_file(file):
    with open(file, "r") as f:
        return f.read().splitlines()


def write_file(file, data):
    with open(file, "w") as f:
        f.write("\n".join(data))


def generate_date():
    year = 1900 + random.randint(0, 100)
    month_num = random.randint(1, 12) - 1
    day = random.randint(1, days_in_month[month_num])
    return "{0} {1} {2}".format(day, months[month_num], year)


def generate_record(names, surnames):
    name = names[random.randint(0, len(names) - 1)]
    surname = surnames[random.randint(0, len(surnames) - 1)]
    date = generate_date()
    return "{0} {1} {2}".format(name, surname, date)


def generate_records(names, surnames, num):
    random.seed()
    return [generate_record(names, surnames) for i in range(num)]


def main():
    names = read_file("names.txt")
    surnames = read_file("surnames.txt")
    for p in range(2, 7):
        num = 10**p
        output_file = "records_1e{0}.txt".format(p)
        print("Generating {0} records into {1}...".format(num, output_file))
        records = generate_records(names, surnames, num)
        write_file(output_file, records)
    print("Done")


if __name__ == "__main__":
    main()
