from string import ascii_letters

class enigma:
    def __init__ (self, steckerbrett = {" ":" "}, alpha=None, bravo=None, charlie=None):
        self.alphabet = list(ascii_letters.lower())
        self.steckerbrett = steckerbrett
        if alpha != None and bravo != None and charlie != None and type(steckerbrett) is dict:
            self.alpha = alpha
            self.bravo = bravo
            self.charlie = charlie
        else:
            if type(steckerbrett) is not dict:
                self.steckerbrett = {" ":" "}
            
            rotors = [alpha, bravo, charlie]
            i = 0
            for rotor in rotors:
                if rotor == None and type(rotor) is not int and type(rotor) is not float:
                    rotor = 0
                    rotors[i] = rotor
                i += 1
            self.alpha = rotors[0]
            self.bravo = rotors[1]
            self.charlie = rotors[2]
            
        for letter in list(self.steckerbrett.keys()):
            if letter in self.alphabet:
                self.alphabet.remove(letter)
                self.alphabet.remove(self.steckerbrett[letter])
                self.sterckerbrett.update({self.steckerbrett[letter]:letter})
        
        self.reflector = list(reversed(self.alphabet))

    def permutate(self, rotor):
        new_alphabet = ''.join(self.alphabet)
        new_alphabet = list(new_alphabet)

        for i in range(rotor):
            new_alphabet.insert(0, new_alphabet[-1])
            new_alphabet.pop(-1)
        
        return new_alphabet

    def inverse_permutation(self,rotor):
        new_alphabet = ''.join(self.alphabet)
        new_alphabet = list(new_alphabet)

        for i in range(rotor):
            new_alphabet.append(new_alphabet[0])
            new_alphabet.pop(0)
        
        return new_alphabet

    def encrypt_text(self, text):
        encrypted_text = []
        text = text.lower()
        text.split()
        for letter in text:
            if letter in self.steckerbrett:
                encrypted_text.append(self.steckerbrett[letter])
            else:
                temp_letter = self.permutate(self.alpha)[self.alphabet.index(letter)]
                temp_letter = self.permutate(self.bravo)[self.alphabet.index(temp_letter)]
                temp_letter = self.permutate(self.charlie)[self.alphabet.index(temp_letter)]
                temp_letter = self.reflector[self.alphabet.index(temp_letter)]
                temp_letter = self.inverse_permutation(self.charlie)[self.alphabet.index(temp_letter)]
                temp_letter = self.inverse_permutation(self.bravo)[self.alphabet.index(temp_letter)]
                temp_letter = self.inverse_permutation(self.alpha)[self.alphabet.index(temp_letter)]
                encrypted_text.append(temp_letter)
            
            self.alpha += 1
            if self.alpha % 26 == 0 and self.alpha > 25:
                self.bravo +=1
                self.alpha = 0
                if self.bravo % 26 == 0 and self.alpha % 26 != 0 and self.bravo > 25:
                    self.charlie += 1
                    self.bravo = 1
        
        for i in encrypted_text:
            print(i, end="")
    


Enigma = enigma(bravo=36)
Enigma.encrypt_text("rrvr zno ra fpdfzvz gfltndbi mslp azcl")