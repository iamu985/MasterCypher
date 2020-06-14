import string
import math
import pyperclip as pc
print('Importing modules from MasterCypher success')

class MasterCypher():
    
    def __init__(self, script, keys, numb_wheels):
        self.script = script
        self.keys = keys
        self.mode = mode
        self.numb_wheels = numb_wheels
        self.alpha = list(string.ascii_lowercase)
        self.alpha_numb = [i for i in range(len(self.alpha))]
        self.wheels = {'a':[], 'b':[], 'c':[], 'd':[], 'e':[], 'f':[], 'g':[], 'h':[], 'i':[],  'j':[]}
        self.heads = list(self.wheels.keys())
        self.position = []
        self.position_of_cipher = []
        self.cipher_text = []
        print('Setup Complete')
        

    def get_pincode(self):
        code = self.keys.split(',')
        pincode = []
        for c in code:
            pincode.append(int(c))
        return pincode
    

    def get_formatted_script(self):
        formatted_text = list(self.script.lower().replace(' ', ''))
        print('Sent Formatted Script')
        return formatted_text

    def fetch_wheels(self, mode):
        pincode = MasterCypher(self.script, self.keys, self.numb_wheels).get_pincode()
        for k in range(len(pincode)):
            for a in self.alpha_numb:
                if mode == 'encode':
                    value = a + pincode[k]
                if mode == 'decode':
                    value = a - pincode[k]

                if value > len(self.alpha_numb)-1:
                    value = value - 26
                self.wheels[self.heads[k]].append(value)
        print('Wheels fetched')
        return self.wheels

    def fetch_position(self):
        position = []
        pincode = MasterCypher(self.script, self.keys, self.numb_wheels).get_pincode()
        format_script = MasterCypher(self.script, self.keys, self.numb_wheels).get_formatted_script()
        for f in range(len(format_script)):
            for a in range(len(self.alpha)):
                if format_script[f] == self.alpha[a]:
                    position.append(a)
        print('Position fetched')
        return position

    def fetch_position_cipher(self, mode):
        pincode = MasterCypher(self.script, self.keys, self.numb_wheels).get_pincode()
        position_cipher = []
        position =MasterCypher(self.script, self.keys, self.numb_wheels).fetch_position()
        get_wheels = MasterCypher(self.script, self.keys, self.numb_wheels).fetch_wheels(mode)
        for pos in range(len(position)):
            operator = math.floor(pos/self.numb_wheels)
            wheel_index = pos - self.numb_wheels * operator
            run_wheel = get_wheels[self.heads[wheel_index]]
            position_cipher.append(run_wheel[position[pos]])
        print('cipher position fetched')
        return position_cipher

    def reverse(self, cipher_list):
        ultimate_cipher = []
        for i in range(len(cipher_list)):
            ultimate_cipher.append(cipher_list[-(i+1)])
        return ultimate_cipher

    def write(self, mode):
        if mode == 'encode':
            cipher_text = []
            pincode = MasterCypher(self.script, self.keys, self.numb_wheels).get_pincode()
            position_of_cypher = MasterCypher(self.script, self.keys, self.numb_wheels).fetch_position_cipher(mode)
            for position in position_of_cypher:
                cipher_text.append(self.alpha[position])
            final_cipher = MasterCypher(self.script, self.keys, self.numb_wheels).reverse(cipher_text)
            print('Encoding complete!')
            ciphered = ''.join(final_cipher)
            pc.copy(ciphered)
            return ciphered 

        if mode == 'decode':
            decoded_text = []
            pincode = MasterCypher(self.script, self.keys, self.numb_wheels).get_pincode()
            reverse_text = ''.join(MasterCypher(self.script, self.keys, self.numb_wheels).reverse(self.script))
            position_of_cypher = MasterCypher(reverse_text, self.keys, self.numb_wheels).fetch_position_cipher(mode)
            for position in position_of_cypher:
                decoded_text.append(self.alpha[position])
            print('Decoding Complete')
            deciphered = ''.join(decoded_text)
            pc.copy(deciphered)
            return deciphered


if __name__ == '__main__':
    text = input('Text: ')
    numb_of_wheels = int(input('Wheels: '))
    pin = input('Keys: ')
    mode = input('Mode (encode/decode): ')
    cypher = MasterCypher(text, pin, numb_of_wheels)
    result = cypher.write(mode)
    print(f'Cipher: {result}')
    

