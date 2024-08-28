from PIL import Image


def embed_message(image_path, output_path, message):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Ensure the message can be embedded
    if len(binary_message) > img.size[0] * img.size[1]:
        raise ValueError("Message is too long to be hidden in this image.")

    # Embed the binary message into the image
    message_index = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if message_index < len(binary_message):
                # Get the pixel value
                pixel = list(pixels[i, j])

                # Modify the LSB of the pixel's red value
                pixel[0] = (pixel[0] & ~1) | int(binary_message[message_index])
                message_index += 1

                # Update the pixel in the image
                pixels[i, j] = tuple(pixel)
            else:
                break

    img.save(output_path)
    print(f"Message embedded successfully in {output_path}")


# Example usage
if __name__ == "__main__":
    image_path = 'images/image-01.jpg'
    output_path = 'stego-images/stego_image-01.png'
    message = 'troops will reach by 21th Aug'  # Message to be hidden

    embed_message(image_path, output_path, message)
