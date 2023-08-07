# This project does password encryption, and also uses a flash drive as a key, which contains an encrypted secret key to decrypt AES.


## How it works?

When you run the program, it will ask you to insert a flash drive if no flash drive was found. (There should not be 2 flash drives, only one.) After that, the program will create a secret key and also an IV key.

Then you need to enter the password, the name of the service to which the password refers, and the name of the pet lol (For precise security), after which, it will create a file that stores in itself: Pet name, password, service.

If you need to decrypt files: Run the program, plug in the flash drive, press 2 and then enter the name of the pet that was used to create absolutely all files with passwords. You will get a list of services. Selected the service number - the password is automatically copied to the clipboard.

## NOTE: ONLY WORKS ON WINDOWS SYSTEMS.

What I like about this project is if you copy all the data from the flash drive, given the key, etc. to another flash drive - the program will not be able to decrypt, because the information in the key does not match the information in the new flash drive. But the information in the key is encrypted thanks to the IV file. And thanks to the same file, the data is encrypted.
