alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z']

def encyption(message,position):
    cipher_text=""
    for char in message:
        new_position=(alphabets.index(char)+position)%26
        cipher_text=cipher_text+alphabets[new_position]
    return (cipher_text)
def decryption(message,position):
    plain_text=""
    for char in message:
        new_position=(alphabets.index(char)-position)%26
        plain_text=plain_text+alphabets[new_position]
    return plain_text
flag=False
while not flag:
    input_command=input("type 'encrypt' for encryption,type 'decrypt' for decryption:\n").lower()
    input_message=input("type your message:\n").lower()
    swift_position=int(input("enter swift key:\n"))

    if input_command=="encrypt":
        text=encyption(message=input_message,position=swift_position)
        print(f"here's the text after encryption: {text}")
    elif input_command=="decrypt":
        text=decryption(message=input_message,position=swift_position)
        print(f"here's the text after decryption: {text}")
    play_again=input("if you want play again type'yes',if not then type 'no':\n").lower()
    if play_again=="no":
        flag=True
        print("goodBye!!")
    else:
        flag=False