from PIL import Image
import numpy as np

img = Image.open("img1.jpg")  # Load image
img_array = np.array(img)           # Convert to numpy array

#print(img_array)  # list of nested 2D lists

def encrypt_image(img_array, key):
    # Convert to int16 to avoid overflow, then back to uint8
    encrypted_array = (img_array.astype(np.int16) + key) % 256
    return encrypted_array.astype(np.uint8)


def decrypt_image(img_array, key):
    # Convert to int16 to avoid overflow, then back to uint8
    encrypted_array = (img_array.astype(np.int16) - key) % 256
    return encrypted_array.astype(np.uint8)

# key adding encryptions

# encrypted_img = Image.fromarray(encrypt_image(img_array, key=10))
# encrypted_img.save("encrypted_image1.jpg")



# decrypted_img = Image.fromarray(decrypt_image(np.array(encrypted_img), key=10))
# decrypted_img.save("decrypted_image1.jpg")


# swapping pixels


def swap_pixels_encrypt(img_array):
    flat = img_array.reshape(-1, 3)  # Flatten image to a 2D array (pixels x RGB)

   
    for i in range(len(flat)-1,0, -2):
        flat[i], flat[len(flat)-1-i] = flat[len(flat)-1-i].copy(), flat[i].copy()  # Swap adjacent pixels
    return flat.reshape(img_array.shape)

def swap_pixels_decrypt(img_array):
    # Decryption is identical to encryption for symmetric swapping
    return swap_pixels_encrypt(img_array)

# Encrypt
encrypted_array = swap_pixels_encrypt(img_array)
encrypted_img = Image.fromarray(encrypted_array)
encrypted_img.save("encrypted_swap.jpg")

# Decrypt
decrypted_array = swap_pixels_decrypt(encrypted_array)
decrypted_img = Image.fromarray(decrypted_array)
decrypted_img.save("decrypted_swap.jpg")