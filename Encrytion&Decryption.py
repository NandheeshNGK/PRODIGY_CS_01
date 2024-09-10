# Function to encrypt the text using Caesar Cipher
def encrypt(text, shift):
    result = ""  # This will store the encrypted text
    for char in text:  # Loop through each character in the text
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97  # Determine if the letter is uppercase or lowercase
            # Encrypt the character by shifting it within the alphabet range
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # If it's not a letter, just add it unchanged
    return result  # Return the final encrypted message

# Function to decrypt the text using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)  # Decrypt by shifting in the opposite direction

# Main function to run the program
def main():
    print("Caesar Cipher Program")  # Display the program title
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").upper()  # Ask the user for their choice
    message = input("Enter your message: ")  # Ask the user for the message

    # Input validation for the shift value
    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))  # Ask for the shift value
            if 1 <= shift <= 25:
                break  # Break out of the loop if the shift value is valid
            else:
                print("Shift value must be between 1 and 25. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 25.")

    # Perform encryption or decryption based on the user's choice
    if choice == 'E':  # If the user chose to encrypt
        encrypted_message = encrypt(message, shift)  # Call the encrypt function
        print(f"Encrypted Message: {encrypted_message}")  # Show the encrypted message
    elif choice == 'D':  # If the user chose to decrypt
        decrypted_message = decrypt(message, shift)  # Call the decrypt function
        print(f"Decrypted Message: {decrypted_message}")  # Show the decrypted message
    else:
        print("Invalid choice. Please select 'E' for encryption or 'D' for decryption.")  # Handle invalid input

# This code runs when the script is executed
if __name__ == "__main__":
    main()
