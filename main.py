def encode(user_input):  # Luke Sandoval
    encoded_list = [int(user_input[i]) + 3 for i in range(len(user_input))]  # create list with each element + 3
    encoded_pass = [str(element) for element in encoded_list]  # conv each element into str
    encoded_pass = ''. join(encoded_pass)  # join elements into str
    return encoded_pass

def decode(user_input):
    pass

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