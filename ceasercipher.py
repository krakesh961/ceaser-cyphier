alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(new_text,new_shift):
    cipher_new=''
    for letters in new_text:
        postiton=alphabet.index(letters)
        new_position=postiton+new_shift
        new_letter=alphabet[new_position]
        cipher_new+=new_letter
    print(cipher_new)
def decrypt(new_text,new_shift):
    cypher_new=''
    for letters in new_text:
        position=alphabet.index(letters)
        new_position=position-new_shift
        new_letter=alphabet[new_position]
        cypher_new+=new_letter
    print(cypher_new)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift=shift%26
if direction=="encode":
    encrypt(new_text=text,new_shift=shift)
elif direction=="decode":
    decrypt(new_text=text,new_shift=shift)
else:
    print('enter correct word')
