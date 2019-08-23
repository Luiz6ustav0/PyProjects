# Caesar Cypher - Test Project

"""We are going to define two functions taking two parameters each,
one to encrypt and the other to decrypt messages.
In case you don't know, the Caeser Cypher method to encrypt
is a fairly simple one where we shift all letters by a certain
offset and send the result as the message. If you need to decrypt,
all you need to do is know the offset, that's also why it's not very
secure anymore because computers can easily check the 26ish possibilities
in the alphabet and decrypt any message""" 

import random # we are using it to give files random names


alphabet = 'abcdefghijklmnopqrstuvwxyz'      # we are going to use this in our functions to shift the letters
punctuation = '!.,?-_><:|~^@#$%1234567890 '  # makes sure that we don't end up messing up because of the 
                                             # punctuation, special signs or spaces


def encrypt(message, offset):

    offset = int(offset)
    tes = message.lower()

    encrypted_message = ''
    file_name = 'New_encryption' + str(random.randint(0, 1001)) + ".txt"

    with open(file_name, 'w') as encrypt_file:
        for i in tes:
            if i not in punctuation:
                index = alphabet.find(i)
                encrypted_message += alphabet[(index - offset) % 26]
            else:
                encrypted_message += i

        encrypt_file.write("Offset: {z} \nEncrypted message: {message}".format(z=offset, message=encrypted_message))

    print("\nFile Written.\n")


def decrypt(message, offset):

    offset = int(offset)
    decrypted_message = ''
    file_name = "Decryption_file{0}.txt".format(str(random.randint(0, 1001)))

    with open(file_name, 'w') as decrypt_file:  # creates a new file and writes the decrypted message to it
        for i in message:
            if i not in punctuation:
                index = alphabet.find(i)
                decrypted_message += alphabet[(index + offset) % 26]
            else:
                decrypted_message += i
        decrypt_file.write("Offset: {z} \nMessage: {message} \nDecrypted message: "
                           "{decrypt} \n\n".format(z=offset, message=message, decrypt=decrypted_message))

    print("\nFile written.\n")


def brute_f_decrypt(message):
    # this is the function we call when we don't know the offset, it's gonna print all the possible offsets in
    # the alphabet and we are just going to check which one makes sense

    file_name = "Brute_Force_Decryption_file{0}.txt".format(str(random.randint(0, 1001)))  # random name for the file

    with open(file_name, 'w') as brute_file:  # starts decryption process and write it to the file
        for z in range(0, len(alphabet)+1):
            try_decrypted_message = ''
            for i in message:
                if i not in punctuation:
                    index = alphabet.find(i)
                    try_decrypted_message += alphabet[(index + z) % 26]
                else:
                    try_decrypted_message += i
            brute_file.write("Offset: {z} \nMessage: {message}\n\n".format(z=z, message=try_decrypted_message))

    print("\nFile Written.\n")


def user_choice(choice):

    if choice == '1':
        print("Ok, type the message you would like to encrypt and I'll ask for the offset later.")
        user_message = input("Message: ")
        print("\n\nOk, we got your message, now, tell me the offset you want to use: ")
        offset = input("Offset: ")

        encrypt(user_message, offset)
        print("File saved. Check current folder and look for 'new_encryption'")

    elif choice == '2':
        print("Ok, type the message you would like to decrypt...")
        user_message = input("Message: ")
        print("\n\nOk, we got your message, now, type 1 if you know the offset or 2 if you want us to decrypt through "
              "brute force")
        choice2 = input("Option 1 or 2: ")
        if choice2 == '1':
            offset = input("Great, so tell me the message offset and we will break it to you: ")
            decrypt(user_message, offset)
            print("\nFile saved. Check current folder and look for the new decryption file")

        elif choice2 == '2':
            print("\nOk... brute force decryption.\n")
            brute_f_decrypt(user_message)
            print("\nFile saved. Check current folder and look for the new brute force decryption file.")

        else:
            print("We did not understand your input, try again.")

    else:
        print("We did not understand your input, try again.")


choice_test = input("Type 1 if you want to encrypt a message or type 2 if you want to decrypt a message: ")

test_message = 'Hello world!'

user_choice(choice_test)


# test_d = encrypt(test_message, 5)

# print(test_d)

# print(brute_f_decrypt(test_d))

# print('\n{}'.format(decrypt(test_d, 5)))
