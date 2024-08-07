import numpy as np
import pywt
import pickle
import cv2
from PIL import Image
from Encrypter import encrypt as aes_encrypt
from Decrypter import decrypt as aes_decrypt

# Load image using PIL to strip incorrect sRGB profile
image_path = '2.png'  # Path to your uploaded image
image_pil = Image.open(image_path)
image_pil = image_pil.convert("RGB")  # Convert to RGB and strip profile
image = np.array(image_pil).astype(np.float64)  # Convert to numpy array

if image is None:
    raise ValueError("Image not loaded. Please check the path.")

# Function to pad image dimensions to be even
def pad_image(image):
    padded_image = np.pad(image, ((0, image.shape[0] % 2), (0, image.shape[1] % 2), (0, 0)), mode='constant')
    return padded_image

# Function to unpad image dimensions to original
def unpad_image(image, original_shape):
    return image[:original_shape[0], :original_shape[1], :]

# Pad image dimensions if necessary
original_shape = image.shape
image_padded = pad_image(image)

# Perform 2D DWT on each channel separately
coeffs = [pywt.dwt2(image_padded[:, :, i], 'haar') for i in range(3)]
cA = [coeff[0] for coeff in coeffs]
cH = [coeff[1][0] for coeff in coeffs]
cV = [coeff[1][1] for coeff in coeffs]
cD = [coeff[1][2] for coeff in coeffs]

# AES Encryption
key = 'password'  # Key
cH_aes_encrypted = [aes_encrypt(cH[i], key) for i in range(3)]

# Store the AES encrypted value as a binary file
with open('cipher_aes.txt', 'wb') as file:
    pickle.dump(cH_aes_encrypted, file)

print(f"AES encrypted value has been written to cipher_aes.txt")

# AES Decryption
with open('cipher_aes.txt', 'rb') as file:
    cH_aes_encrypted = pickle.load(file)

cH_decrypted = [aes_decrypt(cH_aes_encrypted[i], key) for i in range(3)]

# Ensure the decrypted cH is in the same format as the original
cH_decrypted = [np.array(cH_decrypted[i], dtype=np.float64) for i in range(3)]

# Reconstruct the image using decrypted cH
coeffs_decrypted = [(cA[i], (cH_decrypted[i], cV[i], cD[i])) for i in range(3)]
image_reconstructed_padded = np.stack([pywt.idwt2(coeffs_decrypted[i], 'haar') for i in range(3)], axis=-1)

# Unpad image to original dimensions
image_reconstructed = unpad_image(image_reconstructed_padded, original_shape)

# Ensure values stay within the acceptable range
image_reconstructed = np.clip(image_reconstructed, 0, 255).astype(np.uint8)

# Save reconstructed image
reconstructed_image_path = 'reconstructed_image.png'
cv2.imwrite(reconstructed_image_path, cv2.cvtColor(image_reconstructed, cv2.COLOR_RGB2BGR))

# Output
for i, channel in enumerate(['Blue', 'Green', 'Red']):
    print(f"\n{channel} channel cH (Encrypted): stored in cipher_aes.txt")
    print(f"\nOriginal {channel} channel cH:")
    print(cH[i])
    print(f"\nDecrypted {channel} channel cH:")
    print(cH_decrypted[i])

print("\nOriginal Image Shape:", original_shape)
print("Reconstructed Image Shape:", image_reconstructed.shape)
