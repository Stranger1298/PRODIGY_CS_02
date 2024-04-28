from PIL import Image

def encrypt_image(input_path, output_path, key):
    original_image = Image.open(input_path)
    width, height = original_image.size
    encrypted_image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            original_pixel = original_image.getpixel((x, y))
            encrypted_pixel = tuple([(p ^ key) for p in original_pixel])
            encrypted_image.putpixel((x, y), encrypted_pixel)
    encrypted_image.save(output_path)
    print("Image encrypted successfully.")

def decrypt_image(input_path, output_path, key):
    encrypted_image = Image.open(input_path)
    width, height = encrypted_image.size
    decrypted_image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            encrypted_pixel = encrypted_image.getpixel((x, y))
            decrypted_pixel = tuple([(p ^ key) for p in encrypted_pixel])
            decrypted_image.putpixel((x, y), decrypted_pixel)
    decrypted_image.save(output_path)
    print("Image decrypted successfully.")

def main():
    input_image_path = "Task-2\Images\pexels-poppy-martinez-571476080-17394240.jpg" 
    encrypted_image_path = "IMG-20240305-WA0016.jpg" 
    decrypted_image_path = "IMG-20240305-WA0016.jpg"
    key = int(input("Enter the encryption key (integer): "))
    encrypt_image(input_image_path, encrypted_image_path, key)
    decrypt_image(encrypted_image_path, decrypted_image_path, key)

if __name__ == "__main__":
    main()