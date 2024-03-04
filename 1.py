def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No found."
        except IndexError:
            return "Index error"

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def upd_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."


@input_error
def get_contact(args, contacts):
    name = "".join(args)
    phone = contacts[name]
    return f"Phone is: {phone}"


def all_contact(contacts):
    res = ""
    for u, p in contacts.items():
        res += f"{u} {p}\n"
    return res


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(upd_contact(args, contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "all":
            print(all_contact(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
