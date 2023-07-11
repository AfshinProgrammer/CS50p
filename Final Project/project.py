# Afshin Masoudi
# CS50p/Final Project/Jarvis Phone Book

import re, os, sys, pickle, keyboard
from colorama import init, Fore, Style
from typing import Optional, List
from time import sleep
from tabulate import tabulate

# Initialize Colorama
init()

# Define global variables
APP_LOGO = Fore.CYAN + "J.A.R.V.I.S.🤖" + Style.RESET_ALL
APP_NAME = Fore.RED + "Jarvis" + Style.RESET_ALL
CONFIG_FILE = "./Repository/config_app.pkl"
CONTACTS_FILE = "./Repository/contacts.pkl"
USERNAME_PATTERN = re.compile("^[a-zA-Z0-9_-]{3,25}$")
PASSWORD_PATTERN = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}$")
NAME_PATTERN = re.compile("^[A-Za-z]{2,25}( [A-Za-z]{2,25})?$")
PHONE_PATTERN = re.compile(r"^(\+\d{1,3})?[\s-]?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}$")
OPTIONS = ["Add Contact", "Edit Contact", "Delete Contact", "Search Contact", "Display All Contacts", "Quit"]
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
max_attempts = 3

# Class to create user for using the app
class User:
    """Represents a user with a username and password."""
    def __init__(self) -> None:
        self._username: Optional[str] = None
        self._password: Optional[str] = None

    @property
    def username(self) -> Optional[str]:
        """Getter for the username."""
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        """Setter for the username."""
        if USERNAME_PATTERN.match(value):
            self._username = value
        else:
            raise ValueError(f" ❌  Invalid Username: {value}")

    @property
    def password(self) -> Optional[str]:
        """Getter for the password."""
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        if PASSWORD_PATTERN.match(value):
            """Setter for the password."""
            self._password = value
        else:
            raise ValueError(f" ❌  Invalid Password: {value}\nPassword must contain at least one lowercase letter, one uppercase letter, one digit, and be at least 8 characters long.")

# Class to create Contact for saving phone numbers
class Contact:
    """Represents a contact with a name and phone number."""
    def __init__(self) -> None:
        self._name: Optional[str] = None
        self._phone: Optional[str] = None

    def __str__(self) -> str:
        """String representation of the contact."""
        return f"🧑 {self.name} - ☎️  {self.phone}"

    @property
    def name(self) -> Optional[str]:
        """Getter for the contact's name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if NAME_PATTERN.match(value):
            """Setter for the contact's name."""
            self._name = value
        else:
            raise ValueError("❌ Invalid Full Name.")

    @property
    def phone(self) -> Optional[str]:
        """Getter for the contact's phone number."""
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        if PHONE_PATTERN.match(value):
            """Setter for the contact's phone number."""
            self._phone = value
        else:
            raise ValueError("❌ Invalid International Phone Number.")

# Function to sleep the app
def waiting(time= 5, itration = 2):
    emojis = "🕛🕧🕐🕜🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦"
    max_steps = len(emojis) * itration
    time_step = float(time / max_steps)

    for index in range(max_steps + 1):
        print(f"{emojis[index % len(emojis)]} %{int((index / max_steps) * 100)} " + "." * int((index * 10) / max_steps), end="\r")
        sleep(time_step)

    sleep(1)

# Function to check username
def is_valid_username(username: str) -> bool:
    """Check if a username is valid."""
    return bool(USERNAME_PATTERN.search(username))

# Function to check password
def is_valid_password(password: str) -> bool:
    """Check if a password is valid."""
    return bool(PASSWORD_PATTERN.search(password))

# Function to validate name
def is_valid_name(name: str) -> bool:
    """Check if a name is valid."""
    return bool(NAME_PATTERN.search(name))

# Function to validate phone numbers
def is_valid_number(phone: str) -> bool:
    """Check if a phone number is valid."""
    return bool(PHONE_PATTERN.search(phone))

# Function to save data to a pickle file
def save_data_to_file(data, path: str) -> bool:
    """Save data to a file using pickle."""
    folder = "./Repository"
    try:
        # check whether directory already exists
        if not os.path.exists(folder):
            os.mkdir(folder)

        with open(path, "wb") as file:
            pickle.dump(data, file)
        # print(f" ✔️  {Fore.GREEN}Data saved successfully.{Style.RESET_ALL}")
        return True
    except IOError:
        print(f" ❌ {Fore.RED}Failed to save data in file: {path}{Style.RESET_ALL}")
        return False

# Function to load data from a pickle file
def load_data_from_file(path: str):
    """Load data from a file using pickle."""
    try:
        with open(path, "rb") as file:
            data = pickle.load(file)
        # print(f" ✔️  {Fore.GREEN}Data loaded successfully.{Style.RESET_ALL}")
        return data
    except FileNotFoundError:
        print(f" ❌ {Fore.RED}Failed to load data from file: {path}{Style.RESET_ALL}")
        return None

# Function to login the app
def login(user: User):
    """Authenticate the user and allow them to log in."""
    try:
        for attempt in range(max_attempts):
            clear()
            print(f" {APP_LOGO} {Fore.GREEN}You must login to access the phone book.{Style.RESET_ALL}")
            print(f"{Fore.YELLOW} ⚠️  You can press Ctrl+C to exit the app.{Style.RESET_ALL}")
            # Get user input
            print(f"{Fore.RED} 🔔 Attempt : {attempt + 1}/{max_attempts}{Style.RESET_ALL}")
            entered_username = input(" 🧑 Enter Username : ").strip()
            entered_password = input(" 🔑 Enter Password : ").strip()
            # Authenticate user
            if entered_username == user.username and entered_password == user.password:
                print(f"{Fore.GREEN} ✔️  Welcome {Fore.YELLOW + entered_username + Fore.GREEN}, You logged in successfully.{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED} ❌ Invalid Username or Password. Try again.{Style.RESET_ALL}")
                input(f" {APP_LOGO} Press the Enter key to continue ...! 🔄 ")
                continue

        print(f"{Fore.RED} ❌ Maximum login attempts reached.{Style.RESET_ALL}")
        return False
    except KeyboardInterrupt:
        sys.exit(f"\n {APP_LOGO} It was great talking with you.\n {Fore.GREEN}Have a wonderful day!{Style.RESET_ALL} 🔚 ")

# Function to register the app
def register():
    """Register a new user."""
    try:
        for attempt in range(max_attempts):
            clear()
            print(f" {APP_LOGO} {Fore.GREEN}You must register to use the app.{Style.RESET_ALL}")
            print("=" * 56)
            print(" Username : ")
            print(f"{Fore.YELLOW} ⚠️  Only allow letters, numbers, underscores, and dashes.{Style.RESET_ALL}")
            print(f"{Fore.YELLOW} ⚠️  Must be between 3 and 25 characters.{Style.RESET_ALL}")
            print(" Password : ")
            print(f"{Fore.YELLOW} ⚠️  Has minimum 8 characters in length.{Style.RESET_ALL}")
            print(f"{Fore.YELLOW} ⚠️  At least one uppercase English letter.{Style.RESET_ALL}")
            print(f"{Fore.YELLOW} ⚠️  At least one lowercase English letter.{Style.RESET_ALL}")
            print(f"{Fore.YELLOW} ⚠️  At least one digit.{Style.RESET_ALL}")
            print("=" * 56)
            print(f"{Fore.YELLOW} ⚠️  You can press Ctrl+C to exit the app." + Style.RESET_ALL)
            # Get user input
            print(f"{Fore.RED} 🔔 Attempt : {attempt + 1}/{max_attempts}" + Style.RESET_ALL)
            entered_username = input(" 🧑 Enter your Username : ").strip()
            entered_password = input(" 🔑 Enter a Password    : ").strip()
            # Validate user input
            if is_valid_username(entered_username) and is_valid_password(entered_password):
                # Create user dictionary
                user = User()
                user.username = entered_username
                user.password = entered_password

                print(f" ✔️  {Fore.YELLOW + entered_username + Fore.GREEN}, You registered successfully.{Style.RESET_ALL}")
                return user
            else:
                print(f"{Fore.RED} ❌ Invalid Username or Password. Try again.{Style.RESET_ALL}")
                input(f" {APP_LOGO} Press the Enter key to continue ...! 🔄 ")
                continue

        print(f"{Fore.RED} ❌ Maximum Rergisteration attempts reached.{Style.RESET_ALL}")
        return None
    except KeyboardInterrupt:
        sys.exit(f" {APP_LOGO} It was great talking with you.\n {Fore.GREEN}Have a wonderful day!{Style.RESET_ALL} 🔚 ")

# Function to login the app
def choice(options : List[str] = OPTIONS, title : str = "Phone Book") -> int:
    """Choose an option."""
    try:
        index = 0
        while True:
            clear()
            number = index % len(options)
            # Show options
            print(f" {APP_LOGO} What can I do for you? ")
            print(f"={Fore.RED} {title} {Style.RESET_ALL}"+ "=" * 58)
            for i, item in enumerate(options):
                prefix = Fore.YELLOW + "> " if (i == number) else "  "
                print(prefix + item + Style.RESET_ALL + ".")
            print("=" * 72)
            # Choose an option
            print(f"{Fore.YELLOW} ⚠️  You can press Ctrl+C to exit the app.{Style.RESET_ALL}")
            print(f" {APP_LOGO} Choose an item (press 🔼 and 🔽) : {Fore.YELLOW + options[number] + Style.RESET_ALL}")
            sleep(0.25)
            key = keyboard.read_key()
            if key == "up":
                index -=1
            elif key == "down":
                index += 1
            elif key == "enter":
                return index % len(options)
            else:
                continue
    except KeyboardInterrupt:
        return -1

# Function to add a Contact
def add_contact(contacts : List[Contact]) -> bool:
    """Add and save a contact."""
    for attempt in range(max_attempts):
        sleep(0.25)
        clear()
        print(f" {APP_LOGO} {Fore.GREEN}You can add a contact to the phone book.{Style.RESET_ALL}")
        print("=" * 82)
        print(" Name : ")
        print(f" ⚠️  {Fore.YELLOW}Only only consist of characters.{Style.RESET_ALL}")
        print(f" ⚠️  {Fore.YELLOW}Must be one part or two parts (each part between 2 and 25 characters).{Style.RESET_ALL}")
        print(" Phone Number : ")
        print(f" ⚠️  {Fore.YELLOW}Must be between 10 and 18 characters long.{Style.RESET_ALL}")
        print(f" ⚠️  {Fore.YELLOW}Must contain numbers.{Style.RESET_ALL}")
        print(f" ⚠️  {Fore.YELLOW}Sample I  : +1-123-456-7890, +1 123 456 7890, 123-456-7890, and 123 456 7890.{Style.RESET_ALL}")
        print(f" ⚠️  {Fore.YELLOW}Sample II : +98-1234567890, +98 1234567890, +981234567890, and 1234567890.{Style.RESET_ALL}")
        print("=" * 82)
        print(f"{Fore.YELLOW} ⚠️  You can press Ctrl+C to back to the menu.{Style.RESET_ALL}")
        print(f"{Fore.RED} 🔔  Attempt : {attempt + 1}/{max_attempts}{Style.RESET_ALL}")
        #input(f"{Fore.RED} 🔔  Attempt : {attempt + 1}/{max_attempts}{Style.RESET_ALL} 🔄 ")
        try:
            # Check input Name
            name = input(f" {APP_LOGO} Enter Full Name : ").strip().title()
            if not is_valid_name(name):
                raise ValueError("Invalid Full Name.")

            # Check input Name in Contacts
            for item in contacts:
                if item.name.lower() == name.lower():
                    raise ValueError(F"{Fore.YELLOW + name + Style.RESET_ALL} exists in Contacts ...!")

            # Check input Phone Number
            phone = input(f" {APP_LOGO} Enter Phone Number : ").strip()
            if not is_valid_number(phone):
                raise ValueError("Invalid Phone Number.")

            # Create a Contact
            new_contact = Contact()
            new_contact.name = name
            new_contact.phone = phone

            # Add new Contact
            contacts.append(new_contact)

            # Save Changes
            if not save_data_to_file(contacts, CONTACTS_FILE):
                print(f" ❌ {Fore.RED}Failed to save changes ...!{Style.RESET_ALL}")
                return False

            print(f" ✔️  {Fore.YELLOW + name + Fore.GREEN}'s Contact added successfully.{Style.RESET_ALL}")
            return True
        except ValueError as e:
            print(f"{Fore.RED} ❌ {str(e)}" + Style.RESET_ALL)
            input(f" {APP_LOGO} Press the Enter key to continue ...! 🔄 ")
            continue
        except KeyboardInterrupt:
            print(f"{Fore.RED}\n ❌ Contact creation cancelled by user.{Style.RESET_ALL}")
            return False

    print(f"{Fore.RED} ❌ Maximum Add attempts reached.{Style.RESET_ALL}")
    return False

# Function to select a contact
def select_contact(contacts : List[Contact], title : str) -> int:
    """Select a contact."""
    try:
        index = 0
        while True:
            clear()
            number = index % len(contacts)
            # Show options
            print(f" {APP_LOGO} You can select to {title}.")
            print(f"={Fore.RED} {title} {Style.RESET_ALL}"+ "=" * 58)
            for i, item in enumerate(contacts):
                prefix = Fore.YELLOW + "> " if (i == number) else "  "
                print(prefix + item.__str__() + Style.RESET_ALL + ".")
            print("=" * 72)
            # Choose an option
            print(f"{Fore.YELLOW} ⚠️  You can press Ctrl+C to back to the menu.{Style.RESET_ALL}")
            print(f" {APP_LOGO} Choose a Contact (press 🔼 and 🔽) : {Fore.YELLOW + contacts[number].name + Style.RESET_ALL}")
            sleep(0.25)
            key = keyboard.read_key()
            if key == "up":
                index -=1
            elif key == "down":
                index += 1
            elif key == "enter":
                return index % len(contacts)
            else:
                continue
    except KeyboardInterrupt:
        return -1

# Function to edit a Contact
def edit_contact(contacts : List[Contact]) -> bool:
    """Edit a contact."""
    title = "Edit a contact"

    # Check Phone Book
    if len(contacts) == 0:
        print(f" ❌ {Fore.RED}Phone Book is empty ...!{Style.RESET_ALL}")
        return False

    # Choose a Contact to edit the phone number
    number = select_contact(contacts, title)
    if number == -1:
        print(f"\n ❌ {Fore.RED}Contact selection cancelled by user.{Style.RESET_ALL}")
        return False

    # Edit selected Contact
    for attempt in range(max_attempts):
        clear()
        print(f" {APP_LOGO} {Fore.GREEN}You can edit a contact in the phone book.{Style.RESET_ALL}")
        print("=" * 82)
        print(" Phone Number : ")
        print(f" ⚠️  {Fore.YELLOW}Must be between 10 and 18 characters long.{Style.RESET_ALL}")
        print(f" ⚠️  {Fore.YELLOW}Must contain numbers.{Style.RESET_ALL}")
        print(f" ⚠️  {Fore.YELLOW}Sample I  : +1-123-456-7890, +1 123 456 7890, 123-456-7890, and 123 456 7890.{Style.RESET_ALL}")
        print(f" ⚠️  {Fore.YELLOW}Sample II : +98-1234567890, +98 1234567890, +981234567890, and 1234567890.{Style.RESET_ALL}")
        print("=" * 82)
        print(f" ⚠️  {Fore.YELLOW}You can press Ctrl+C to back to the menu.{Style.RESET_ALL}")
        print(f" 🔔  {Fore.RED}Attempt : {attempt + 1}/{max_attempts}{Style.RESET_ALL}")
        print(f" ⚠️  {Fore.YELLOW + contacts[number].name + Style.RESET_ALL}'s phone number is {Fore.BLUE + contacts[number].phone + Style.RESET_ALL}.")
        #input(f" ⚠️  {Fore.YELLOW + contacts[number].name + Style.RESET_ALL}'s phone number is {Fore.BLUE + contacts[number].phone + Style.RESET_ALL}. 🔄 ")
        try:
            # Check Phone Number
            new_phone = input(f" {APP_LOGO} Enter {Fore.YELLOW + contacts[number].name + Style.RESET_ALL}'s new phone number : ").strip()
            if not is_valid_number(new_phone):
                raise ValueError("Invalid Phone Number")

            # Update the selected contact
            contacts[number].phone = new_phone

            # Save Changes
            if not save_data_to_file(contacts, CONTACTS_FILE):
                print(f" ❌ {Fore.RED}Failed to save changes ...!{Style.RESET_ALL}")
                return False

            input(f" ✔️  {Fore.YELLOW + contacts[number].name + Fore.GREEN}'s Contact edited successfully.{Style.RESET_ALL} 🔄 ")
            return True
        except ValueError as e:
            print(f" ❌ {Fore.RED}{str(e)}. Please try again.{Style.RESET_ALL}")
            input(f" {APP_LOGO} Press the Enter key to continue ...! 🔄 ")
            continue
        except KeyboardInterrupt:
            print(f"\n ❌ {Fore.RED}Contact Edition cancelled by user.{Style.RESET_ALL}")
            return False

    print(f" ❌ {Fore.RED}Maximum Edit attempts reached.{Style.RESET_ALL}")
    return False

# Function to delete a Contact
def delete_contact(contacts : List[Contact]) -> bool:
    """Delete a contact."""

    title = "Delete a contact"
    # Check Phone Book
    if len(contacts) == 0:
        print(f" ❌ {Fore.RED}Phone Book is empty ...!{Style.RESET_ALL}")
        return False

    # Choose a Contact to edit the phone number
    number = select_contact(contacts, title)
    if number == -1:
        print(f" ❌ {Fore.RED}Contact selection cancelled by user.{Style.RESET_ALL}")
        return False

    name = contacts[number].name
    # Delete selected contact
    contacts.remove(contacts[number])

    # Save changes
    if not save_data_to_file(contacts, CONTACTS_FILE):
        print(f"{Fore.RED} ❌ Failed to save changes...!{Style.RESET_ALL}")
        return False

    print(f" ✔️  {Fore.YELLOW + name + Fore.GREEN}'s Contact deleted successfully.{Style.RESET_ALL}")
    return True

# Functions to search Contacts
def search_contact(contacts : List[Contact]) -> List[Contact]:
    title = f"{Fore.RED}Searched{Style.RESET_ALL}"

    # Check Phone Book
    if len(contacts) == 0:
        print(f" ❌ {Fore.RED}Phone Book is empty ...!{Style.RESET_ALL}")
        return []

    key = ""
    try:
        while True:
            clear()

            result = []
            # Search Contacts by Key
            for item in contacts:
                if item.name.lower().startswith(key.lower()):
                    result.append(item)

            # Display results
            print(f" {APP_LOGO} {Fore.GREEN}You can search for a Contact in the phone book.{Style.RESET_ALL}")
            print(f" ⚠️  {Fore.YELLOW}You can press Ctrl+C to back to the menu.{Style.RESET_ALL}")
            print(f" 🔎 Search for {Fore.YELLOW + key + Style.RESET_ALL} : ")
            display_contacts(result, title)

            # Get Key from user
            print(f" {APP_LOGO} 🔍 Enter a key to search : {Fore.YELLOW + key + Style.RESET_ALL}")
            input = keyboard.read_key().lower()
            sleep(0.25)
            if input == "enter":
                break
            elif input == "backspace":
                key = key[:-1]
            elif len(input) == 1:
                key += input
            else:
                continue

    except KeyboardInterrupt:
        print(f" ❌ {Fore.RED}Contact Search cancelled by user.{Style.RESET_ALL}")
        return result

# Functions to display Contacts
def display_contacts(contacts : List[Contact], title = f"{Fore.RED}All{Style.RESET_ALL}") -> bool:
    print(f" {APP_LOGO} {Fore.GREEN}You can see 📋 {title} {Fore.GREEN}Contacts.{Style.RESET_ALL}")

    if len(contacts) == 0:
        print(f"{Fore.RED} This is empty ❓ {Style.RESET_ALL}")
        return False
    else:
        headers = ["Full Name","Phone Number"]
        result = []

        for contact in contacts:
            result.append([contact.name, contact.phone])

        # Display all contacts
        print(tabulate(result, headers, tablefmt="outline"))

        return True

# Function to exit the app
def exit_phone_book():
    clear()
    confirm = input(f" {APP_LOGO} Are you sure you want to exit the app? (Press y) ")
    if confirm == "y":
        sys.exit(f" {APP_LOGO} It was great talking with you.\n {Fore.GREEN}Have a wonderful day!{Style.RESET_ALL} 🔚 ")
    else:
        print(f" {Fore.MAGENTA}Back to the menu.{Style.RESET_ALL} 🔙 ")

def main():
    """Main function."""
    # Greeting with user
    clear()
    print(f" {APP_LOGO} {Fore.YELLOW}Hi! I'm excited to assist you today. This is {Fore.RED +APP_NAME + Fore.YELLOW} App.{Style.RESET_ALL}")

    # Waiting to press Enter
    input(f" {APP_LOGO} Press the Enter key to continue ...! 🔄 ")
    # Authentication & Registration
    authenticated = False
    while not authenticated:
        clear()
        # Load registered-user data from pkl file
        user = load_data_from_file(CONFIG_FILE)
        if user is not None:
            # User is authenticated, do something
            if login(user):
                authenticated = True
        else:
            # Register to use the app
            user = register()
            if user is not None:
                # Save registered-user data to pkl file
                save_data_to_file(user, CONFIG_FILE)
                authenticated = True

    # Waiting to press Enter
    sleep(2)
    input(f" {APP_LOGO} Press the Enter key to continue ...! 🔄 ")

    # *** Main Menu ***
    clear()
    print(f" {APP_LOGO} {Fore.GREEN}Hi {Fore.YELLOW + user.username + Fore.GREEN}, Welcome to {APP_NAME + Fore.GREEN} App.{Style.RESET_ALL}")
    waiting()
    input(f" {APP_LOGO} Press the Enter key to continue ...! 🔄 ")
    try:
        while True:
            clear()
            # Load Contacts from pkl file
            contacts = load_data_from_file(CONTACTS_FILE)
            contacts = list() if contacts is None else list(contacts)
            print(f"{Fore.YELLOW} ⚠️  You can press Ctrl+C to exit the app.{Style.RESET_ALL}")
            input(f" {APP_LOGO} {Fore.GREEN}{len(contacts)}{Style.RESET_ALL}-Contacts is loaded successfully.\n Press the Enter key to continue ...! 🔄 ")

            clear()
            # Choose an option
            number = choice(options= OPTIONS, title= "Phone Book")
            sleep(0.5)
            if number == 0:
                add_contact(contacts)
            elif number == 1:
                edit_contact(contacts)
            elif number == 2:
                delete_contact(contacts)
            elif number == 3:
                search_contact(contacts)
            elif number == 4:
                clear()
                display_contacts(contacts)
            else:
                exit_phone_book()

            # Waiting to press Enter
            sleep(2)
            input(f" {APP_LOGO} Press the Enter key to continue ...! 🔄 ")

    except KeyboardInterrupt:
        exit_phone_book()

if __name__ == "__main__":
    main()