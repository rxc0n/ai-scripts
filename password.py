import random
import string

def generate_random_password(length=12, use_uppercase=True, use_digits=True, use_special=True, encrypt_letters=False):
    characters = ''
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if not (use_uppercase or use_digits or use_special):
        characters = string.ascii_letters  # Default to letters only if no other options are selected

    password = ''.join(random.choice(characters) for i in range(length))

    if encrypt_letters:
        password = encrypt(password)

    security_percentage = calculate_security_percentage(password, use_uppercase, use_digits, use_special)
    return password, security_percentage

def generate_and_save_passwords(file_path, num_passwords, length=12, use_uppercase=True, use_digits=True, use_special=True, encrypt_letters=False):
    with open(file_path, 'w') as file:
        for _ in range(num_passwords):
            random_password, security_percentage = generate_random_password(length, use_uppercase, use_digits, use_special, encrypt_letters)
            file.write(f'Password: {random_password}, Security Percentage: {security_percentage}%\n')

def calculate_security_percentage(password, use_uppercase, use_digits, use_special):
    total_characters = len(string.ascii_letters) + len(string.digits) + len(string.punctuation)
    used_characters = len(set(password))

    if use_uppercase:
        used_characters += len(set(password).intersection(set(string.ascii_uppercase)))
    if use_digits:
        used_characters += len(set(password).intersection(set(string.digits)))
    if use_special:
        used_characters += len(set(password).intersection(set(string.punctuation)))

    security_percentage = (used_characters / total_characters) * 100
    return round(security_percentage, 2)

def encrypt(text):
    # Simple substitution cipher for demonstration purposes
    alphabet = string.ascii_lowercase
    key = ''.join(random.sample(alphabet, len(alphabet)))
    translation_table = str.maketrans(alphabet, key)
    encrypted_text = text.translate(translation_table)
    return encrypted_text

# Example usage
file_path = 'passwords.txt'
num_passwords = 5

generate_and_save_passwords(file_path, num_passwords, length=16, use_uppercase=True, use_digits=True, use_special=True, encrypt_letters=True)
print(f'{num_passwords} passwords generated and saved to {file_path}')
