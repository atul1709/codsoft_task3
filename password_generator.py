import string
import random

def generate_password(length):
    """
    Generates a random password of the specified length.
    
    Parameters:
    length (int): The desired length of the password
    
    Returns:
    str: The generated password
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Prompt the user for the desired password length
    password_length = int(input("Enter the desired length of the password: "))
    
    # Generate the password
    password = generate_password(password_length)
    
    # Display the generated password
    print(f"Your new password is: {password}")

if __name__ == "__main__":
    main()