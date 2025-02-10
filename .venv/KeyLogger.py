class Key_Logger:
    def encryption(self,array):
        array_encryption = []
        for word in array:
            nem = ord(word)+2
            nem = (nem ** 2)//65
            if nem > 122:
                nem -= 57
            array_encryption.append(chr(nem))
        return array_encryption


