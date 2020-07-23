## This program works to encode and decode messaages in the caesar cipher

alphabetl = 'abcdefghijklmnopqrstuvwxyz'
alphabetu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '1234567890!?.,\' '

#encode function
def encode():
    print("What do you want the key to be?")
    ekey = input('> ')
    encoded = ""
    x = 0
    for symbol in plaintext:
        if symbol in alphabetl:
            location = alphabetl.find(plaintext[x]) + int(ekey)
            if location >= 26:
                location = location % 26
            encoded = encoded + alphabetl[location]
        elif symbol in alphabetu:
            location = alphabetu.find(plaintext[x]) + int(ekey)
            if location >= 26:
                location = location % 26
            encoded = encoded + alphabetu[location]
        elif symbol in symbols:
            location = symbols.find(plaintext[x])
            encoded = encoded + symbols[location]
        else:
            print("That is not a valid character, please try again.")
            exit()
        x = x + 1
    print("\nHere is your ciphertext: \n" + str(encoded))


#decode function1
def decode():
    print('If you know the key you would like to use, enter it now(0-25). If you want to brute force, type \'bf\'')
    dkey = input('> ')
    if dkey == 'bf':
        dkey = 0
        while dkey < 26:
            decoded = ""
            x = 0
            for symbol in ciphertext:
                if symbol in alphabetl:
                    location = alphabetl.find(ciphertext[x]) - dkey
                    if location >= 26:
                        location = location % 26
                    decoded = decoded + alphabetl[location]
                elif symbol in alphabetu:
                    location = alphabetu.find(ciphertext[x]) - dkey
                    if location >= 26:
                        location = location % 26
                    decoded = decoded + alphabetu[location]
                elif symbol in symbols:
                    location = symbols.find(ciphertext[x])
                    decoded = decoded + symbols[location]
                else:
                    print("That is not a valid character, please try again.")
                    exit()
                x = x + 1
            print("Key " + str(dkey) + ': ' + str(decoded))
            dkey = dkey + 1
    elif dkey <= '25':
        dkey = int(dkey)
        decoded = ""
        x = 0
        for symbol in ciphertext:
            if symbol in alphabetl:
                location = alphabetl.find(ciphertext[x]) - dkey
                if location >= 26:
                    location = location % 26
                decoded = decoded + alphabetl[location]
            elif symbol in alphabetu:
                location = alphabetu.find(ciphertext[x]) - dkey
                if location >= 26:
                    location = location % 26
                decoded = decoded + alphabetu[location]
            elif symbol in symbols:
                location = symbols.find(ciphertext[x])
                decoded = decoded + symbols[location]
            else:
                print("That is not a valid character, please try again.")
                exit()
            x = x + 1
        print("String deciphered using key " + str(dkey) + ": " + str(decoded))
        dkey = dkey + 1
    else:
        print('That wasn\'t an option')
        exit()


# user guide
print('''

 *************DISCLAIMER*************
This program does not encrypt or decrypt
numbers or special characters, except for
common punctuation characters such as:
!  ?  .  ,  \'

These charaters will be left as-is.

''')
print('Would you like to Decrypt or Encrypt?')
answer = input('> ')

#the if statement that guides the user through the process
if answer == 'D' or answer == 'Decrypt' or answer == 'd' or answer == 'decrypt':
    print('\nEnter the ciphertext.')
    ciphertext = input('> ')
    decode()

elif answer == 'E' or answer == 'Encrypt' or answer == 'e' or answer == 'encrypt':
    print('\nEnter the plaintext.')
    plaintext = input('> ')
    encode()

else:
    print ('\nThat was not an option, exiting...')
    exit()
