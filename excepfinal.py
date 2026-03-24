# custom exceptions
class EmptyFileError(Exception):
    pass

class InvalidFileError(Exception):
    pass


def read_file(name):
    try:
        if not name.endswith(".txt"):
            raise InvalidFileError("Only .txt file allowed")

        with open(name, "r") as f:
            data = f.read()

            if data.strip() == "":
                raise EmptyFileError("File is empty")

            print(data)

    except FileNotFoundError:
        print("File not found")

    except EmptyFileError as e:
        print(e)

    except InvalidFileError as e:
        print(e)

file = input("Enter file name: ")
read_file(file)