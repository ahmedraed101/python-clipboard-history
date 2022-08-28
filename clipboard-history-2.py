# pip install pyperclip
from pyperclip import waitForNewPaste


def store_data(data):
    with open("data_2.txt", "a+") as file:
        file.write(
            str(data).strip() + "\n\n------------------------------------------------------\n\n")


def main():
    while True:
        try:
            data = waitForNewPaste()
            if data.strip() != "":
                store_data(data)
        except KeyboardInterrupt:
            exit(0)


if __name__ == "__main__":
    main()
