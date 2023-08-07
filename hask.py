import re
import time
import wmi
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os
import string
import secrets
class DefineUsb:
    def __init__(self):
        self.c=wmi.WMI()
        self.flash_drivers = []
        self.strFlashDriver = None
        self.scanned = False
        self.flash_driver_displayed = False
        self.model = None
        self.FlashLatter = None
        self.KeyName = 'Key'
        self.path_key = None
        self.key = None
        self.iv = None
        
        self.ScanUsb()
        self.GetModel()
        self.FindLater()
        self.createKeyOnUsb()
        


    def ScanUsb(self):
        while not self.scanned:
            for drive in self.c.Win32_DiskDrive():
                    if "Removable Media" in drive.MediaType:
                        self.flash_drivers.append(drive)
                        self.scanned = True
                        break
            if not self.scanned and not self.flash_driver_displayed:
                print('Wairing for usb key....')
                self.flash_driver_displayed = True
            time.sleep(1)

    def FindLater(self):
        for disk in self.c.query(f'SELECT * FROM Win32_DiskDrive WHERE Model LIKE "{self.model}"'):
            deviceID = disk.DeviceID

            for partition in self.c.query('ASSOCIATORS OF {Win32_DiskDrive.DeviceID="' + deviceID + '"} WHERE AssocClass = Win32_DiskDriveToDiskPartition'):

                for logical_disk in self.c.query('ASSOCIATORS OF {Win32_DiskPartition.DeviceID="' + partition.DeviceID + '"} WHERE AssocClass = Win32_LogicalDiskToPartition'):
                    self.FlashLatter = logical_disk.DeviceID

    def GetModel(self):
        for flash_drive in self.flash_drivers:
            self.strFlashDriver = str(flash_drive)
            model_match = re.search(r"Model = \"(.*?)\";", self.strFlashDriver)
            device_id = re.search(r"DeviceID = \"(.*?)\";", self.strFlashDriver)
            PNPDeviceID = re.search(r"PNPDeviceID = \"(.*?)\";", self.strFlashDriver)
            if model_match:
                self.model = model_match.group(1)
                self.Info_1 = device_id.group(1)
                self.Info_2 = PNPDeviceID.group(1)
                print('Loading...')

    def createKeyOnUsb(self):
        file_path = f'{self.FlashLatter}\\{self.KeyName}'
        if os.path.exists(file_path):
            self.path_key = f'{self.FlashLatter}\\key.iv'
            self.load_key_iv()
            with open(file_path,'rb') as file:
                self.strFlashDriver = file.read()
                self.decrypt_key()

                for content in self.flash_drivers:
                    content_of_flash = str(content)
                    if content_of_flash in self.strFlashDriver:
                        model_match = re.search(r"Model = \"(.*?)\";", content_of_flash)
                        if model_match:
                            print('Key is valid.')
                    else:
                        print('Key Not Match')
                        os._exit(0)
        else:
            self.path_key = f'{self.FlashLatter}\\key.iv'
            self.generate_key_iv()
            self.save_key_iv()
            try:
                with open(file_path,'wb') as file:
                    self.encrypt_key()
                    file.write(self.strFlashDriver)
                print('Done')
            except Exception as e:
                print("Error:", str(e))
                os._exit(0)
    def load_key_iv(self):
        with open(self.path_key, 'rb') as f:
            data = f.read()
            self.key = data[:16]
            self.iv = data[16:]
    def generate_key_iv(self):
        self.key = get_random_bytes(16)
        self.iv = get_random_bytes(16)
    def save_key_iv(self):
        with open(self.path_key, 'wb') as f:
            f.write(self.key + self.iv)
    def encrypt_key(self):
        self.cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        data = self.strFlashDriver
        self.strFlashDriver = self.cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    def decrypt_key(self):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted_data = unpad(cipher.decrypt(self.strFlashDriver), AES.block_size).decode('utf-8')
        self.strFlashDriver = decrypted_data