alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~" * 2

def encrypt(text, password):
    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = index + password
            result += alphabet[new_index]
        else:
            result += char
    
    return result

def decrypt(text, password):
    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = index - password
            result += alphabet[new_index]
        else:
            result += char
    
    return result


if __name__ == "__main__":
    while True:
        print("1. Encrypt")
        print("2. decrypt")
        n = int(input("Enter: "))

        match n:
            case 1:
                print(encrypt(input("Enter text: "), int(input("Enter password"))))
            case 2:
                print(decrypt(input("Enter text: "), int(input("Enter password"))))
            case _:
                print("Error")



