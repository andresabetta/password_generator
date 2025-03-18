import string
import random

def main():
    print("=== Password Generator ===")
    
    while True:
        try:
            char_count = int(input("Enter password length (min 8): "))
            if char_count >=8:
                break
            else:
                print("Minimum length is 8.")
        except ValueError:
            print("Enter a valid number.")

    

    print(password_generator(char_count))

def password_generator(lenght=12):
    letter = string.ascii_letters
    number = string.digits
    special_char = "!@#$%^&*()_+-="
    allchars = letter+number+special_char

    password = [
        random.choice(letter),
        random.choice(number),
        random.choice(special_char)
    ]

    for _ in range(lenght-3):
        password.append(random.choice(allchars))
    
    random.shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    main()