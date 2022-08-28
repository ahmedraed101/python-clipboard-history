from pyperclip import waitForNewPaste
from sys import argv
from time import strftime


def store_data(data, filename):
    with open(filename + ".txt", "a+") as file:
        file.write(
            str(data).strip() + "\n\n------------------------------------------------------\n\n")


def start(filename="data_3"):
    while True:
        try:
            data = waitForNewPaste()
            if data.strip() != "":
                store_data(data, filename)
        except KeyboardInterrupt:
            exit(0)


def main():
    if len(argv) < 2:
        start()
    command = argv[1]
    if command == "--name" and len(argv) > 2:
        start("-".join(argv[2:]))
    if command == "--time":
        start(f"data-3-{strftime('%Y-%m-%d %H-%M-%S')}")


if __name__ == "__main__":
    main()
