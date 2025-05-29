import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
import numpy as np

file_path=""

def browse_file():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Select Image File",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if file_path:
        label_path.config(text=file_path)

        # Optionally show the image (resized for display)
        img = Image.open(file_path)
        img = img.resize((250, 250))
        img_tk = ImageTk.PhotoImage(img)
        label_image.config(image=img_tk)
        label_image.image = img_tk  # Keep reference to avoid garbage collection



def encrypt_image(key):
    if file_path!="":
        img = Image.open(file_path)  # Load image
        img_array = np.array(img)           # Convert to numpy array
    # Convert to int16 to avoid overflow, then back to uint8
    encrypted_array = (img_array.astype(np.int16) + key) % 256
    encrypted_array=encrypted_array.astype(np.uint8)
    
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save("encrypted_image1.jpg")

def decrypt_image( key):
    if file_path!="":
        img = Image.open(file_path)  # Load image
        img_array = np.array(img)           # Convert to numpy array
    # Convert to int16 to avoid overflow, then back to uint8
    decrypted_array = (img_array.astype(np.int16) - key) % 256
    decrypted_array=decrypted_array.astype(np.uint8)
    
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save("decrypted_image1.jpg")


def encrypt_button():
    encrypt_image(int(key_input.get()))

def decrypt_button():
    decrypt_image(int(key_input.get()))



def swap_pixels_encrypt():
    if file_path!="":
        img = Image.open(file_path)  # Load image
        img_array = np.array(img)           # Convert to numpy array
    flat = img_array.reshape(-1, 3)  # Flatten image to a 2D array (pixels x RGB)

   
    for i in range(len(flat)-1,0, -2):
        flat[i], flat[len(flat)-1-i] = flat[len(flat)-1-i].copy(), flat[i].copy()  # Swap adjacent pixels
    encrypted_array=flat.reshape(img_array.shape)

    
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save("encrypted_swap.jpg")




def swap_pixels_decrypt():
    if file_path!="":
        img = Image.open(file_path)  # Load image
        img_array = np.array(img)           # Convert to numpy array
    # Decryption is identical to encryption for symmetric swapping
    return swap_pixels_encrypt(img_array)



# Create GUI
root = tk.Tk()
root.title("Image Pixel manipulator")
root.geometry("800x600")

# Button to upload image
btn_upload = Button(root, text="Browse Image", command=browse_file)
btn_upload.pack(pady=10)

# Label to show file path
label_path = Label(root, text="No file selected")
label_path.pack(pady=5)

# Label to display image
label_image = Label(root)
label_image.pack()

# Label + Entry box for user input (like encryption key)
label_input = Label(root, text="Enter a shift key value:")
label_input.pack()
key_input = entry_shift = tk.Entry(root, width=10)
key_input.pack()

# Button to print entry value (you can link this to encryption)
btn_submit = Button(root, text="Encrypt", command=encrypt_button)
btn_submit.pack(pady=10)


btn_submit2 = Button(root, text="Decrypt", command=decrypt_button)
btn_submit2.pack(pady=10)


btn_submit3 = Button(root, text="Pixel Swap", command=swap_pixels_encrypt)
btn_submit3.pack(pady=10)

label = Label(root, text="By : Souhardya Saha")
label.pack()
# Start GUI loop
root.mainloop()
