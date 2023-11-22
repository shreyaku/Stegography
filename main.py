import cv2
import os

# Define c globally
c = {}

def encrypt_message(img, msg, password):
    d = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

    return img

def decrypt_message(img, password):
    message = ""
    n = 0
    m = 0
    z = 0

    pas = input("Enter passcode for Decryption: ")
    if password == pas:
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decryption message:", message)
    else:
        print("YOU ARE NOT auth")

# Example usage
img = cv2.imread("car.jpg.jpg.")  # Replace with the correct image path
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

encrypted_img = encrypt_message(img.copy(), msg, password)
decrypt_message(encrypted_img.copy(), password)
