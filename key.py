from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os
import string
import shutil
import sys
import secrets
from hask import DefineUsb
from Copy import SetToClip

class CryptorPasswords:
    def __init__(self,usb_info):
        
        self.flash_drivers = []
        self.scanned = False
        self.gen_name = None
        self.usb_info = usb_info
        self.path_key = f'{self.usb_info.FlashLatter}\\key.iv'
        self.Info_1 = usb_info.Info_1
        self.key = None
        self.iv = None
        self.encrypted_data = None
        self.decrypted_data = None
        self.GenName()
        self.Main()
    def GenName(self):
        symbols = ['L', '%', '^','()']

        password = ""
        for _ in range(25):
            password += secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.ascii_uppercase)
        password += secrets.choice(string.digits)
        password += secrets.choice(symbols)
        self.gen_name = password
    def Main(self):
        self.load_key_iv()

        choice = input("Выберите действие (1 - зашифровать, 2 - дешифровать): ")

        if choice == '1':
            self.password = input("Введите пароль для зашифровки: ")
            if self.password == '':
                sys.exit()
            self.service = input("Введите имя сервиса: ")
            self.pet_name = input("Введите имя питомца: ")
            self.encrypt_password()
            path_flash = f'{self.usb_info.FlashLatter}\\{self.gen_name}'
            with open(f'{path_flash}.enc', 'wb') as f:
                f.write(self.encrypted_data)
            print("Пароль успешно зашифрован и сохранен.")
            os.system('cls')



        elif choice == '2':
            pet = input('Enter pets name: ')
            path_flash_of_files = f'{self.usb_info.FlashLatter}\\'
            service_files = [filename for filename in os.listdir(path_flash_of_files) if filename.endswith('.enc')]
            path_flash = None
            for i, filename in enumerate(service_files, start=1):
                path_flash = f'{self.usb_info.FlashLatter}\\{filename}'

                with open(path_flash, 'rb') as f:
                    self.encrypted_data = f.read()
                    self.decrypt_password()
                    if pet != self.pet_name:
                        sys.exit()
            print("Выберите сервис для дешифровки:")
            for i, filename in enumerate(service_files, start=1):
                path_flash = f'{self.usb_info.FlashLatter}\\{filename}'
                with open(path_flash, 'rb') as f:
                    self.encrypted_data = f.read()
                    self.decrypt_password()
                print(f"{i}. {self.service}")


            selection = int(input())
            selected_service = service_files[selection - 1]
            path_flash = f'{self.usb_info.FlashLatter}\\{selected_service}'
            with open(path_flash, 'rb') as f:
                self.encrypted_data = f.read()
            self.decrypt_password()
            SetToClip(self.password)
            print('Copied to clipboard!')
            os.system('cls')
        else:
            sys.exit()

    def load_key_iv(self):
        with open(self.path_key, 'rb') as f:
            data = f.read()
            self.key = data[:16]
            self.iv = data[16:]

    def encrypt_password(self):
        self.cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        data = f"{self.password}@{self.service}@{self.pet_name}@{self.Info_1}"
        self.encrypted_data = self.cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    
    def decrypt_password(self):
        try:
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            self.decrypted_data = unpad(cipher.decrypt(self.encrypted_data), AES.block_size).decode('utf-8')
            self.password, self.service, self.pet_name,self.Info_1 = self.decrypted_data.split('@')
        except:
            print('Bro, are you trying to hack this file??')
            os._exit(0)
usb_info = DefineUsb()
while True:
    CryptorPasswords(usb_info)