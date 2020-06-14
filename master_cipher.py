import string
import math
import pyperclip as pc
print('Importing modules from MasterCypher success')

class MasterCypher():
    '''
    =========================
    Definition of some terms:
    =========================
        |--------------------------------------------------------------------------------------------------------------------------
        |>>> WHEELS:
        |--------------------------------------------------------------------------------------------------------------------------
        |    is the set of cyphered alphabets that is cyphered through key
        |    For example if the key = 3
        |    then all the letters of in the wheel will be transposed by +3
        |    so a=d, b=e, c=f and so on.
        |    since this script takes on the numerical value with index 0;
        |    0=3, 1=4, 2=4 and so,
        |    Each wheel has its own name given to it randomly and it only initializes when the user passes the number of wheels that they 
        |    want to use.
        |    NOTE: [There are 10 sets of wheels and the user might take any set be it 3, 4, 5 or even 2 or 1]
        | -------------------------------------------------------------------------------------------------------------------------
        |>>> KEYS:
        |--------------------------------------------------------------------------------------------------------------------------
        |    is the set of numbers passed to the program that will be used to transpose individual wheels.
        |    This program consists of 10 wheels so the sets of keys also collectively called PINCODE/S falls under the range.
        |    But there arent any limitation the the range of the individual key meaning you can transpose the letters up or down to
        |    any position from (3-25) 25 because the start index is 0.
        |    There is a specific format of passing PINCODE/S though. The PINCODE/S is to be passed seperated by commas (,).
        |    For instance,
        |    The number of wheels = 4
        |    pincodes = 2, 4, 5, 3
        |    NOTE: [number of wheels to use and length of pincodes must be the same]
        |============================================================================================================================
        
        HOW DOES THE CIPHER WORK:   
            To say the very least the cipher in itself is not so complex at all infact the basic idea is very simplistic.
            Its just a SUBSTITUTION CIPHER but what makes it interesting is the use of different keys and different wheels.
            If I had to explain in a simple way I can do so with an example:
            Say the text is 'hello world' pretty basic secret message.
            Now the cipher asks for the number of wheels for simplicity lets assume the number of wheels to be 3
            Then the cipher asks for the sets of keys again for simplicity lets assume that the key is '1, 2, 3'
            
            The cipher first goes through the pincodes given by the user in this case 1, 2, 3 and transposes the list of alphabets to 
            respectice keys;
            for 1: a=b, b=c, c=d and so on
            for 2: a=c, b=d, c=e and so on
            for 3: a=d, b=e, c=f and so on
            
            then it appends the values of the now transposed set of alphabets to its respective names in a pre-defined dictionary.
            The it loops over in a range of length of the secret text in this case 'helloworld' which is 10;
            
            for loop 1:
                >>> letter = 'h' and it goes through the first wheel which is transposed by +1 so h=i
             for loop 2:
                >>> letter = 'e' and it goes through the second wheel which is transposed by +2 so e=g
              for loop 3:
                >>> letter = 'l' and it goes through the third wheel which is transposed by +3 so l=o
               for loop 4:
                >>> letter = l and it goes through the first wheel which is transposed by +1 so l=m
                for loop 5:
                    >>> letter = 'o' and it goes through the second wheel which is transposed by +2 so o=q
               
               .......
               The loop continues till the length of the secret text in each iteration or loop the wheel changes as shown in the example
               above.
             
             Lastly the secret ciphered text is reversed this is done for the purpose of blanketting the cipher a step more.
             Oh for the above example the cipher becomes 'eotpzqmogi' ====>>> the cipher is the returned after being reversed
           
            
            
    BASIC SUMMARY TO USE THE SCRIPT:
    > Pincode writing format (1, 2, 23, 21, 16)
    > There is no limitation to the length of the message that can be passed.
    > Number of wheels must be equal to the number of keys
    > Length of the wheels should not exceed more than 10 same goes for the number of keys
    > By default the mode is set to 'encode'
    > The keys can be repeated as many times as you like || for eg: {1, 2, 2, 2, 23, 12, 12, 4}
    > The secret text passed would be stripped of any whitespaces and the program returns non-spaced text or stringoftextlikethis.
    
    The above example was just a simplistic view of looking at things. There are 10 wheels with each having its own keys and the keys 
    alone has 26 possibilities with repetition.
    
    =================================================================================================================================
    
    '''
    def __init__(self, script, keys, numb_wheels):
        '''Initializing the program'''
        self.script = script #secret message
        self.keys = keys #string of unformatted keys eg:{'1, 23, 13, 12'}
        self.mode = mode 
        self.numb_wheels = numb_wheels #calling the number of wheels to be used
        self.alpha = list(string.ascii_lowercase)
        self.alpha_numb = [i for i in range(len(self.alpha))]
        self.wheels = {'ijoev':[], 'cgytu':[], 'aikvj':[], 'dhshx':[], 'lujcl':[], 'xymwh':[], 'mosmi':[], 'zkgsz':[], 'aymeh':[],  'tknax':[]}
        self.heads = list(self.wheels.keys()) #stores the unique key names of the wheel dictionary
        self.position = []
        self.position_of_cipher = []
        self.cipher_text = []
        print('Setup Complete')
        

    def get_pincode(self):
        '''Formats the pincode from string to a list from '1,2,3,4' to [1, 2, 3, 4]'''
        code = self.keys.split(',')
        pincode = []
        for c in code:
            pincode.append(int(c))
        return pincode
    

    def get_formatted_script(self):
        '''Strips the whitespaces from the secret message'''
        formatted_text = list(self.script.lower().replace(' ', ''))
        print('Sent Formatted Script')
        return formatted_text

    def fetch_wheels(self, mode):
        '''Fetches the wheel required and tranposes it to the given respective key'''
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
        '''Gets the list of position of the letters of the secret text from the alphabet set a=0, b=1, c=2 like so.''' 
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
        '''Gets the position of the ciphered letters from the wheels'''
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
        '''Function to reverse the cipher text'''
        ultimate_cipher = []
        for i in range(len(cipher_list)):
            ultimate_cipher.append(cipher_list[-(i+1)])
        return ultimate_cipher

    def write(self, mode):
        '''Actual encoding or decoding done by this function, return the deccoded or encoded text'''
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
    

