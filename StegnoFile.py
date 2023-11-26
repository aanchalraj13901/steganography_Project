import cv2
import os
import tkinter as tk
from tkinter import filedialog

img_path = ""
img = None
msg = ""
password = ""

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)
    
def encrypt_message():
    global img, msg, img_path, password
    img = cv2.imread(img_path.get())
    msg = message_entry.get()
    password = password_entry.get()

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("Encryptedmsg.png", img)
    os.system("start Encryptedmsg.png")
    success_label.config(text="Encryption successful! \n Encrypted image saved as 'Encryptedmsg.png'.")
    decrypt_message_window()  

def decrypt_message_window():
    global decrypt_window, password_entry_decrypt, result_label_decrypt
    decrypt_window = tk.Toplevel(encrypt_window)
    decrypt_window.title("Message Decryption")

    password_label = tk.Label(decrypt_window, text="Enter password:")
    password_label.pack()

    password_entry_decrypt = tk.Entry(decrypt_window, show="*")
    password_entry_decrypt.pack()

    decrypt_button = tk.Button(decrypt_window, text="Decrypt Message", command=decrypt_message)
    decrypt_button.pack()

    result_label_decrypt = tk.Label(decrypt_window, text="")
    result_label_decrypt.pack()

def decrypt_message():
    global img, msg, password_entry_decrypt, result_label_decrypt
    message = ""
    n = 0
    m = 0
    z = 0

    pas = password 

    if pas == password_entry_decrypt.get():
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        result_label_decrypt.config(text="Decryption successful! \n Decrypted message: " + message)
    else:
        result_label_decrypt.config(text="Invalid password. Decryption failed.")

def browse_image():
    global img_path
    img_path = tk.StringVar()
    img_path.set(filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]))
    image_path_label.config(text="Selected Image: " + os.path.basename(img_path.get()))


encrypt_window = tk.Tk()
encrypt_window.title("Message Encryption")

message_label = tk.Label(encrypt_window, text="Enter secret message: ")
message_label.pack()

message_entry = tk.Entry(encrypt_window)
message_entry.pack()

password_label = tk.Label(encrypt_window, text="Enter password: ")
password_label.pack()

password_entry = tk.Entry(encrypt_window, show="*")
password_entry.pack()

browse_button = tk.Button(encrypt_window, text="Browse Image", command=browse_image)
browse_button.pack()

image_path_label = tk.Label(encrypt_window, text="Selected Image: None")
image_path_label.pack()

encrypt_button = tk.Button(encrypt_window, text="Encrypt Message", command=encrypt_message)
encrypt_button.pack()

success_label = tk.Label(encrypt_window, text="")
success_label.pack()

encrypt_window.mainloop()
