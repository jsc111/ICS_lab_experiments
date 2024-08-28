from PIL import Image

def extract_message(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    binary_message = ''
    for i in range(img.size[0]):
        for j in range(img.size[1]):

            pixel = pixels[i, j]

            binary_message += str(pixel[0] & 1)

    # Convert the binary message to text
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '00000000':
            break
        message += chr(int(byte, 2))

    return message

if __name__ == "__main__":
    output_path = 'stego-images/stego_image-01.png'  # Path to the modified image
    extracted_message = extract_message(output_path)
    print(f"Extracted message: {extracted_message}")
