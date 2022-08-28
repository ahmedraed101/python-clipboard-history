# the win32clipboard is part of the pywin32 module install it using `pip install pywin32``
import win32clipboard as wincb
from time import sleep


def get_clipboard():
    try:
        wincb.OpenClipboard()
        data = wincb.GetClipboardData()
        wincb.CloseClipboard()
        return data.strip()
    except Exception as e:
        print(e)
        raise Exception("unable to access clipboard")


def store_data(data):
    with open("data.txt", "a+") as file:
        file.write(
            str(data) + "\n\n___________________________________________\n\n")


def main():
    old = ""
    while True:
        try:
            data = get_clipboard()
            if data == old:
                continue
            old = data
            store_data(data)
        except KeyboardInterrupt:
            print("Closing Clipboard script...")
            exit(0)
        except Exception as e:
            print(e)
            exit(1)
        sleep(1)


if __name__ == "__main__":
    main()
