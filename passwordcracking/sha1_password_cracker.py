import hashlib

def convert_text_to_sha1(text):
    # Generate the SHA1 hash of the input text
    digest = hashlib.sha1(text.encode()).hexdigest()
    return digest


def main():
    user_sha1 = input("Enter your SHA1 to crack: ")

    # Strip and lowercase to standardize the input
    cleaned_user_sha1 = user_sha1.strip().lower()

    # Ensure the input is a valid SHA1 hash (40 characters long)
    if len(cleaned_user_sha1) != 40:
        print("Invalid SHA1 hash length.")
        return

    # Try to find the matching password from the file
    try:
        with open('passwords.txt', 'r') as f:  # Ensure you have the correct file path
            for line in f:
                password = line.strip()
                converted_sha1 = convert_text_to_sha1(password)

                # Compare the SHA1 hash of the password with the user input
                if cleaned_user_sha1 == converted_sha1:
                    print(f"Password Found: {password}")
                    return

        # If no match was found
        print("Could not find the password.")

    except FileNotFoundError:
        print("Error: The file 'passwords.txt' was not found.")


if __name__ == "__main__":
    main()
