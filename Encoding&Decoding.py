import base64

def encode(text: str) -> str:
    '''Encodes a string using base64 encoding.

    Args:
        text: The string to encode.

    Returns:
        The encoded string.
    '''
    encoded_bytes=base64.b64encode(text.encode("utf-8"))
    print("Encoded bytes:",encoded_bytes)
    encoded_text = encoded_bytes.decode()
    return encoded_text

def decode(encoded_text: str) -> str:
    '''Decodes a string encoded using base64 encoding.

    Args:
        encoded_text: The string to decode.

    Returns:
        The decoded string.
    '''
    decoded_bytes=base64.b64decode(encoded_text.encode("utf-8"))
    print("Decoded bytes:",decoded_bytes)
    decoded_text = decoded_bytes.decode()
    return decoded_text

if _name_ == "_main_":
    while True:
        choice = input("Choose an action (encode/ decode/ quit) : ")

        if choice == 'encode':
            text = input("Enter text to encode: ")
            encoded_text = encode(text)
            print(f"Encoded text: {encoded_text}")

        elif choice == 'decode':
            encoded_text = input("Enter encoded text: ")
            decoded_text = decode(encoded_text)
            print(f"Decoded text: {decoded_text}")

        elif choice == 'quit':
            print("------------------------")
            break

        else:
            print("Invalid choice. Please try again.")
