import random
import string

def generate_password(length):
    """Generate a random password."""
    if length < 4:  # Ensure the password length is at least 4
        raise ValueError("Password length should be at least 4 characters")
    
    # Define the character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Ensure the password includes at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the rest of the password length with a mix of all characters
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=length-4)
    
    # Shuffle the list to avoid any predictable patterns
    random.shuffle(password)
    
    # Convert list to string and return
    return ''.join(password)

# Get password length from user input
try:
    password_length = int(input("Enter the desired length for the password (minimum 4): "))
    if password_length < 4:
        raise ValueError("Password length should be at least 4 characters")
    print(f"Generated password: {generate_password(password_length)}")
except ValueError as e:
    print(f"Invalid input: {e}")
