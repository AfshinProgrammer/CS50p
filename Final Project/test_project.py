# Afshin Masoudi
# CS50p/Final Project/Jarvis Phone Book
# cmd : pytest ./test_project.py

from colorama import Fore, Style
import pytest, pickle, os, sys
from unittest.mock import call, patch
from project import login, register, waiting, is_valid_name, is_valid_number, is_valid_username, is_valid_password, save_data_to_file, load_data_from_file, choice
from project import add_contact, select_contact, edit_contact, delete_contact, search_contact, display_contacts, exit_phone_book
from project import APP_LOGO, User, Contact, OPTIONS, max_attempts

def test_user():
    # Test valid usernames
    u1 = User()
    u1.username = "john_doe"
    assert u1.username == "john_doe"
    u2 = User()
    u2.username = "jane123"
    assert u2.username == "jane123"
    # Test invalid usernames
    u3 = User()
    with pytest.raises(ValueError):
        u3.username = "j"
    u4 = User()
    with pytest.raises(ValueError):
        u4.username = "john.doe"

    # Test valid passwords
    p1 = User()
    p1.password = "Password123"
    assert p1.password == "Password123"
    # Test invalid passwords
    p3 = User()
    with pytest.raises(ValueError):
        p3.password = "password"

def test_contact():
    # Test initialization with no arguments
    contact = Contact()
    assert contact.name is None
    assert contact.phone is None

    # Test valid name
    contact = Contact()
    contact.name = "John Doe"
    assert contact.name == "John Doe"

    # Test invalid name
    contact = Contact()
    with pytest.raises(ValueError):
        contact.name = "J"
    assert contact.name is None

    # Test valid phone number
    contact = Contact()
    contact.phone = "+1 (555) 123-4567"
    assert contact.phone == "+1 (555) 123-4567"

    # Test invalid phone number
    contact = Contact()
    with pytest.raises(ValueError):
        contact.phone = "12345"
    assert contact.phone is None


    # Test string representation
    contact = Contact()
    contact.name = "John Doe"
    contact.phone = "+1 (555) 123-4567"
    assert str(contact) == "🧑 John Doe - ☎️  +1 (555) 123-4567"

@pytest.mark.parametrize("time, iteration", [(5, 2), (1, 1), (10, 3)])
def test_waiting(time, iteration, capfd):
    expected_output = ""
    captured_output = capfd.readouterr().out.strip()
    assert captured_output == expected_output

    waiting(time, iteration)
    assert True

def test_is_valid_username():
    # Test valid usernames
    assert is_valid_username("john_doe") == True
    assert is_valid_username("jane123") == True

    # Test invalid usernames
    assert is_valid_username("j") == False
    assert is_valid_username("john.doe") == False

def test_is_valid_password():
    # Test valid passwords
    assert is_valid_password("Password123") == True
    assert is_valid_password("Abcd1234") == True

    # Test invalid passwords
    assert is_valid_password("password") == False
    assert is_valid_password("password1234") == False
    assert is_valid_password("PASSWORD1234") == False
    assert is_valid_password("1234456789") == False
    assert is_valid_password("Abc123") == False

def test_is_valid_name():
        # Test valid name
        assert is_valid_name("John Doe") == True

        # Test invalid name
        assert is_valid_name("") == False
        assert is_valid_name("J") == False
        assert is_valid_name("John Doe John Doe John Doe John Doe") == False
        assert is_valid_name("John 123") == False

def test_is_valid_number():
        # Test valid phone numbers
        assert is_valid_number("+1 (555) 123-4567") == True
        assert is_valid_number("123-456-7890") == True
        assert is_valid_number("123.456.7890") == True
        assert is_valid_number("+91 8765432109") == True

        # Test invalid phone numbers
        assert is_valid_number("") == False
        assert is_valid_number("12345") == False
        assert is_valid_number("+1 (555) 123-4567 ext. 1234") == False
        assert is_valid_number("+1 (555) 1234-567") == False
        assert is_valid_number("123-456--7890") == False
        assert is_valid_number("+44 20 7123 1234") == False

def test_save_data_to_file():
    # Create test data
    data = []
    contact_1 = Contact()
    contact_1.name = "Maria Garcia"
    contact_1.phone = "+34 612 345 6785"
    data.append(contact_1)
    contact_2 = Contact()
    contact_2.name = "Ahmed Khan"
    contact_2.phone = "+92 333 123 4567"
    data.append(contact_2)
    contact_3 = Contact()
    contact_3.name = "Sophie Martin"
    contact_3.phone = "+33 612 304 5678"
    data.append(contact_3)

    path = "./Repository/data.pkl"

    # check if saved data matches original data
    assert save_data_to_file(data, path) == True
    assert os.path.exists(path) == True

    with open(path, "rb") as file:
        loaded_data = pickle.load(file)
        assert loaded_data[0].name == data[0].name
        assert loaded_data[1].phone == data[1].phone
        assert loaded_data[2].name == data[2].name
        assert loaded_data[2].phone == data[2].phone

    # delete file
    os.remove(path)

def test_load_data_from_file():
    # Create test data
    data = {"name": "John", "age": 30}
    tmpdir = "./"
    # Save data to file
    file_path = os.path.join(tmpdir, "test_load_data.pickle")
    with open(file_path, "wb") as file:
        pickle.dump(data, file)

    # Test loading data from invalid path
    invalid_path = os.path.join(tmpdir, "invalid_dir", "test_load_data.pickle")
    assert load_data_from_file(invalid_path) == None

    # Test loading data from file
    assert load_data_from_file(file_path) == data

    # Remove test file
    os.remove(file_path)

def test_login():
    # Create a user object with valid credentials
    user = User()
    user.username = "TestUser"
    user.password = "TestPassword1234"

    with patch('builtins.input', side_effect=["TestUser", "TestPassword1234"]):
        assert login(user) == True

    with patch('builtins.input', side_effect=["TestUser", "wrongpassword", ""] * max_attempts):
        assert login(user) == False

    with patch('builtins.input', side_effect=KeyboardInterrupt):
        with pytest.raises(SystemExit):
            login(user)

def test_register():
    with patch('builtins.input', side_effect=["TestUser", "TestPassword1234"]):
        user = register()
        assert user is not None
        assert user.username == "TestUser"
        assert user.password == "TestPassword1234"

    with patch('builtins.input', side_effect=["", "TestPassword1234", ""] * max_attempts):
        user = register()
        assert user is None

    with patch('builtins.input', side_effect=["TestUser", "", ""] * max_attempts):
        user = register()
        assert user is None

    with patch('builtins.input', side_effect=KeyboardInterrupt):
        with pytest.raises(SystemExit):
            register()

def test_choice():
    with patch('keyboard.read_key', side_effect=['down', 'down', 'down', 'down', 'enter']):
        # Test if function returns the correct index when the user selects an option
        assert choice(options= OPTIONS, title= "Phone Book") == 4

    with patch('keyboard.read_key', side_effect=['invalid_key', 'down', 'enter']):
        # Test if function returns the correct index when the user types an invalid key
        assert choice(options= OPTIONS, title= "Phone Book") == 1

def test_select_contact():
    # Create some sample contacts
    contact_1 = Contact()
    contact_1.name = "Bruno Mars"
    contact_1.phone = "+1-123-456-7890"
    contact_2 = Contact()
    contact_2.name = "Ed Sheeran"
    contact_2.phone = "+1-321-654-0987"
    contact_3 = Contact()
    contact_3.name = "Deep Purple"
    contact_3.phone = "+1-231-564-8709"
    contacts = [contact_1, contact_2, contact_3]

    with patch('keyboard.read_key', side_effect=['down', 'down', 'enter']):
        # Test if function returns the correct index when the user selects an option
        assert select_contact(contacts, title="Select a contact") == 2

    with patch('keyboard.read_key', side_effect=['invalid_key', 'down', 'enter']):
        # Test if function returns the correct index when the user types an invalid key
        assert select_contact(contacts, title="Select a contact") == 1

def test_add_contact():
    # Create a list of contacts to pass to the function
    contacts = []
    # Valid input
    with patch("builtins.input", side_effect=["John Doe", "+1-123-456-7890"]):
        with patch("project.save_data_to_file", return_value= True):
            # Call the function and assert that it returns True
            assert add_contact(contacts) == True
            # Assert that the contact was added to the list
            assert len(contacts) == 1
            assert isinstance(contacts[0], Contact)
            assert contacts[0].name == "John Doe"
            assert contacts[0].phone == "+1-123-456-7890"

    # Save Error
    with patch("builtins.input", side_effect=["Bruno Mars", "+1-123-456-7890"]):
        with patch("project.save_data_to_file", return_value= False):
            # Call the function and assert that it returns False
            assert add_contact(contacts) == False
            # Assert that the contact was added to the list
            assert len(contacts) == 2

    # Keyboard interrupt
    with patch("builtins.input", side_effect=KeyboardInterrupt):
        # Call the function and assert that it returns False
        assert add_contact(contacts) == False
        # Assert that the contact was not added to the list
        assert len(contacts) == 2

    # Invalid Name input
    with patch("builtins.input", side_effect=["John 123", "+1-323-457-7850", "e"] * max_attempts):
        # Call the function and assert that it returns False
        assert add_contact(contacts) == False
        # Assert that the contact was not added to the list
        assert len(contacts) == 2

    # Invalid Number input
    with patch("builtins.input", side_effect=["John Doe", " ", "e"] * max_attempts):
        # Call the function and assert that it returns False
        assert add_contact(contacts) == False
        # Assert that the contact was not added to the list
        assert len(contacts) == 2

def test_edit_contact():
    # Emty contacts
    contacts = []
    assert edit_contact(contacts) is False

    # Cancelled selection
    contact = Contact()
    contact.name = "John"
    contact.phone = "+1-123-456-7890"
    contacts = [contact]

    # Successful edit
    with patch('project.select_contact', return_value= 0):
        with patch('builtins.input', side_effect= ["+1-198-765-4321", "e"]):
            with patch('project.save_data_to_file', return_value= True):
                assert edit_contact(contacts) is True
                assert contacts[0].phone == "+1-198-765-4321"

    # Selection error
    with patch('project.select_contact', return_value= -1):
            assert edit_contact(contacts) is False

    # invalid phone
    with patch('project.select_contact', return_value= 0):
        with patch('builtins.input', side_effect= ["invalid", "e"] * max_attempts):
            assert edit_contact(contacts) is False

    # Keyboard interrupt
    with patch('project.select_contact', return_value= 0):
        with patch("builtins.input", side_effect= KeyboardInterrupt):
            assert edit_contact(contacts) == False

def test_delete_contact():
    # Empty book
    contacts = []
    assert delete_contact(contacts) is False

    contact_1 = Contact()
    contact_1.name = "John"
    contact_1.phone = "+1-123-456-7890"
    contact_2 = Contact()
    contact_2.name = "Mary"
    contact_2.phone = "+1-132-546-0789"
    contacts = [contact_1, contact_2]

    # Successful edit
    with patch('project.select_contact', return_value= 0):
        with patch('project.save_data_to_file', return_value= True):
            assert delete_contact(contacts) is True
            assert len(contacts) == 1
            assert contacts[0].name == "Mary"

    # Cancelled selection
    with patch('project.select_contact', return_value= -1):
        with patch('project.save_data_to_file', return_value= True):
            assert delete_contact(contacts) is False

    # Save Error
    with patch('project.select_contact', return_value= 0):
        with patch('project.save_data_to_file', return_value= False):
            assert delete_contact(contacts) is False

def test_search_contact():
    # Empty book
    contacts = []
    assert search_contact(contacts) == []

def test_display_contacts(capsys):
    # Empty book
    contacts = []
    assert display_contacts(contacts) is False

    # All contacts
    contact_1 = Contact()
    contact_1.name = "John"
    contact_1.phone = "+1-123-456-7890"
    contact_2 = Contact()
    contact_2.name = "Jane"
    contact_2.phone = "+1-198-765-4321"
    contacts = [contact_1, contact_2]

    assert display_contacts(contacts) is True
    captured = capsys.readouterr()
    assert "+-------------+-----------------+\n| Full Name   | Phone Number    |\n+=============+=================+\n| John        | +1-123-456-7890 |\n| Jane        | +1-198-765-4321 |\n+-------------+-----------------+" in captured.out

def test_exit_phone_book(monkeypatch):
    inputs = ["y"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    with patch.object(sys, 'exit') as mock_exit:
        exit_phone_book()
        assert mock_exit.mock_calls == [call(f" {APP_LOGO} It was great talking with you.\n {Fore.GREEN}Have a wonderful day!{Style.RESET_ALL} 🔚 ")]
