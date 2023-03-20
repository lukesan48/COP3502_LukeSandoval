def encode(user_input):
    encoded_list = [(int(user_input[i]) + 3) % 10 for i in range(len(user_input))]
    encoded_pass = [str(element) for element in encoded_list]
    encoded_pass = ''. join(encoded_pass)
    return encoded_pass

def decode(user_input):  # Trevor Robertson
    decoded_pass = ""
    for num in user_input:
        decoded_pass = decoded_pass + str((int(num) - 3) % 10)
    return decoded_pass

def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

if __name__ == "__main__":
    option = 0
    while option != 3:
        menu()
        option = int(input("Please enter an option: "))  # prompt user for option
        if option == 1:
            user_input = str(input("Please enter your password to encode: "))
            encoded_pass = encode(user_input)  # encode user_input
            print("Your password has been encoded and stored!")
            print()
        elif option == 2:
            decoded_pass = decode(encoded_pass)  # decode the encoded user_input
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}.")
            print()
        elif option == 3:
            break