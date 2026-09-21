import string
import random

password = []

characters = string.ascii_letters

def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()

        if answer == 'y' or answer == 'n':
            return answer
        else:
            print('Please enter y or n')

include_numbers = ask_yes_no('Do you include numbers? (y/n): ')
include_symbols = ask_yes_no('Do you include symbols? (y/n): ')

if include_numbers == 'y':
    password.append(random.choice(string.digits))

if include_symbols == 'y':
    password.append(random.choice(string.punctuation))

while True:
    try:
        password_length = int(input('Enter password length: '))
        if password_length > 0:
            if password_length < len(password):
                print(f'Password length must be at least {len(password)}')
            else:
                remaining = password_length - len(password)
                for i in range(remaining):
                    password.append(random.choice(characters))
                random.shuffle(password)
                password = ''.join(password)
                print(password)
                break
        else:
            print('Password length must be greater than 0')
    except ValueError:
        print('Invalid password length')