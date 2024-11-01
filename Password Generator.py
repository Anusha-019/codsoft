import string
import random

def generate_password(length, complexity):
    if complexity == 'l':
        characters = string.ascii_letters
    elif complexity == 'm':
        characters = string.ascii_letters + string.digits
    elif complexity == 'h':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length must be at least 1.")
            return
        
        complexity = input("Enter the desired complexity (low(l), medium(m), high(h)): ").strip().lower()
        if complexity not in ['l', 'm', 'h']:
            print("Invalid complexity level. Choose from 'low', 'medium', or 'high'.")
            return
        
        password = generate_password(length, complexity)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
