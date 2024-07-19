def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "The key for this contact does not exist"
        except ValueError:
            return "Enter the argument for the command"
        except IndexError: 
            return "The index is not correct"
        except TypeError: 
            return "The type is not correct"


    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
    

@input_error
def add_username_phone(args, contacts):
    username, phone = args
    contacts[username] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    username, phone = args
    contacts[username] = phone
    return "Contact changed."


@input_error
def main():
    try:      
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
                print(add_username_phone(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                if args:
                    print(f"The phone number: {contacts.get(args[0], 'No phone number found')}")
                else:
                    print("Enter the argument for the command") 
            elif command == "all":
                print(contacts)
            else:
                print("Invalid command.")
    except ValueError as ve:
        print(f"You should enter only or at least 2 values: {ve}")
    
        


if __name__ == "__main__":
    main()