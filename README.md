# Password Encryption with Flash Drive Key

This project focuses on enhancing security by employing password encryption. It introduces a unique approach by utilizing a flash drive as a key. The flash drive contains an encrypted secret key that is necessary for decrypting AES-encrypted data.

## How It Works

Upon launching the program, it will prompt you to insert a specific flash drive. Note that only a single flash drive should be connected at a time. The program will then proceed to generate a secret key along with an Initialization Vector (IV) key.

Next, you'll be prompted to enter your password, the corresponding service's name, and an amusing name for a pet (chosen for added security). This information will be used to create a file that stores the pet's name, the password, and the associated service.

For decryption, follow these steps:
1. Run the program using: ```python key.py```
2. Insert the designated flash drive.
3. Choose option 2 from the menu.
4. Enter the pet's name, which was used to generate all password-related files.
5. A list of services will be displayed. Select a service by its corresponding number, and the password will be automatically copied to your clipboard.

## Compatibility

Please be aware that this program is designed exclusively for Windows systems.

## Key Security Features

One of the remarkable aspects of this project is its ability to maintain data security even when transferring all information from the original flash drive, including the key, to another flash drive. This measure ensures that the program cannot decrypt data with the new flash drive, as the key's information will not match. The encrypted information within the key is further secured by the IV file. Consequently, both the data and key remain highly protected.

